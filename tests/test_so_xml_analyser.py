import xml.etree.ElementTree as ET

from resources.so_xml_analyser import StackOverflowXMLAnalyser


def test_load_url():
    """
    Test `get_xml_from_url()`
    """
    xml_url = 'https://merapar-assessment-task.s3.eu-central-1.amazonaws.com/arabic-posts.xml'

    xml = StackOverflowXMLAnalyser.get_xml_from_url(xml_url)

    assert isinstance(xml, ET.Element)
    assert len(xml) == 80


def test_analyse():
    """
    Test `analyse_xml()`
    """
    xml_url = 'https://merapar-assessment-task.s3.eu-central-1.amazonaws.com/arabic-posts.xml'

    xml = StackOverflowXMLAnalyser.get_xml_from_url(xml_url)
    analysis_dict = StackOverflowXMLAnalyser.analyse_xml(xml)

    print(analysis_dict)

    assert analysis_dict == {
        'num_posts': 80,
        'average_score': 3,
        'num_accepted_posts': 7,
        'first_post_date': '2015-07-14T18:39:27.757',
        'last_post_date': '2015-09-14T12:46:52.053',
    }
