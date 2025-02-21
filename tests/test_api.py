import datetime

import pytest

from main import app  # Import your Flask app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_so_xml_analyser(client):
    xml_url = 'https://merapar-assessment-task.s3.eu-central-1.amazonaws.com/arabic-posts.xml'
    response = client.post('analyse', data={'url': xml_url})

    response_json = response.get_json()
    analyse_date = response_json.pop('analyse_date')

    assert response.status_code == 200
    # assert analyse date is close to current time
    assert (datetime.datetime.fromisoformat(analyse_date) - datetime.datetime.now(tz=datetime.timezone.utc)) < datetime.timedelta(minutes=1)

    assert response_json == {
        'average_score': 3,
        'first_post_date': '2015-07-14T18:39:27.757',
        'last_post_date': '2015-09-14T12:46:52.053',
        'num_accepted_posts': 7,
        'num_posts': 80,
    }
