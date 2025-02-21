import datetime as dt
import xml.etree.ElementTree as ET

import requests
from flask import request
from flask_restful import Resource


class StackOverflowXMLAnalyser(Resource):
    """
    Flask Resource for analysing XML files from Stack Overflow pages.
    """

    request_url_key = 'url'

    def post(self) -> dict:
        xml_url = request.form[self.request_url_key]

        try:
            xml = self.get_xml_from_url(xml_url)
        except Exception:
            return {'message': 'URL did not contain a (proper) XML file.'}

        analysis_dict = self.analyse_xml(xml)
        analysis_dict['analyse_date'] = str(dt.datetime.now(tz=dt.timezone.utc))

        return analysis_dict

    @staticmethod
    def get_xml_from_url(url: str) -> ET.Element:
        """
        Given an URL to an XML file, returns the XML file converted to an Element from the `xml` library.
        """
        response = requests.get(url)
        response.raise_for_status()

        root: ET.Element = ET.fromstring(response.content.decode())
        return root

    @staticmethod
    def analyse_xml(xml: ET.Element) -> dict:
        """
        Analyses a parsed `xml` Element that is assumed to be a StackOverflow XML file.
        Returns a dictionary with:

        * the total number of posts (`num_posts`)
        * total number of accepted posts (`num_accepted_posts`)
        * average score per post (`average_score`)
        * creation date of the first post (`first_post_date`)
        * creation date of the last post (`last_post_date`)
        """

        date_key = 'CreationDate'
        score_key = 'Score'
        accepted_key = 'AcceptedAnswerId'

        rows = xml.findall('.//row')

        total_score = 0
        num_accepted = 0
        for row in rows:
            total_score += int(row.get(score_key, 0))

            if accepted_key in row.keys():
                num_accepted += 1

        return {
            'num_posts': len(xml),
            'num_accepted_posts': num_accepted,
            'average_score': int(round(total_score / len(xml))),
            'first_post_date': rows[0].get(date_key),
            'last_post_date': rows[-1].get(date_key),
        }
