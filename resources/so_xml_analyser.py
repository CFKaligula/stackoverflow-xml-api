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
            analysis_dict = self.analyse_xml_file_via_url(xml_url)
        except Exception:
            return {'message': 'URL did not contain a (proper) XML file.'}

        analysis_dict['analyse_date'] = str(dt.datetime.now(tz=dt.timezone.utc))

        return analysis_dict

    @staticmethod
    def analyse_xml_file_via_url(url: str) -> dict:
        # Stream the XML file
        with requests.get(url, stream=True) as response:
            response.raise_for_status()  # Ensure successful request

            result = StackOverflowXMLAnalyser._analyse_xml_string(response.raw)  # type: ignore

        return result

    def analyse_xml_file_via_file_path(file_path: str) -> dict:
        result = StackOverflowXMLAnalyser._analyse_xml_string(file_path)  # type: ignore

        return result

    def _analyse_xml_string(xml_source) -> dict:
        """
        The input parameter `xml_source` can either be raw XML or a filepath to an XML file.
        The XML file is assumed to be a StackOverflow XML data dump.

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

        total_score = 0
        num_accepted = 0
        num_posts = 0
        first_post_date = '?'
        last_post_date = '?'

        # Iterate over XML elements
        for _, row in ET.iterparse(xml_source):
            if score_key not in row.keys():  # not a valid post row
                continue

            num_posts += 1
            total_score += int(row.get(score_key, 0))

            if accepted_key in row.keys():
                num_accepted += 1

            if num_posts == 1:
                first_post_date = row.get(date_key)

            last_post_date = row.get(date_key)
            row.clear()

        return {
            'num_posts': num_posts,
            'num_accepted_posts': num_accepted,
            'average_score': int(round(total_score / num_posts)),
            'first_post_date': first_post_date,
            'last_post_date': last_post_date,
        }
