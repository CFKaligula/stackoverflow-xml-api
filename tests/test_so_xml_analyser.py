from resources.so_xml_analyser import StackOverflowXMLAnalyser


def test_analyse():
    xml_url = 'https://merapar-assessment-task.s3.eu-central-1.amazonaws.com/arabic-posts.xml'

    analysis_dict = StackOverflowXMLAnalyser.analyse_xml_file_via_url(xml_url)

    print(analysis_dict)

    assert analysis_dict == {
        'num_posts': 80,
        'average_score': 3,
        'num_accepted_posts': 7,
        'first_post_date': '2015-07-14T18:39:27.757',
        'last_post_date': '2015-09-14T12:46:52.053',
    }


def test_analyse2():
    xml_url = 'https://merapar-assessment-task.s3.eu-central-1.amazonaws.com/3dprinting-posts.xml'

    analysis_dict = StackOverflowXMLAnalyser.analyse_xml_file_via_url(xml_url)

    print(analysis_dict)

    assert analysis_dict == {
        'num_posts': 497,
        'num_accepted_posts': 65,
        'average_score': 3,
        'first_post_date': '2016-01-12T19:24:29.457',
        'last_post_date': '2021-02-21T09:29:40.710',
    }


def test_very_large():
    xml_file_path = r'C:\Users\caspe\Downloads\superuser.xml\Posts.xml'

    analysis_dict = StackOverflowXMLAnalyser.analyse_xml_file_via_file_path(xml_file_path)

    print(analysis_dict)

    assert analysis_dict == {
        'num_posts': 1245418,
        'num_accepted_posts': 205218,
        'average_score': 3,
        'first_post_date': '2009-07-15T06:27:46.723',
        'last_post_date': '2024-03-21T08:14:33.287',
    }
