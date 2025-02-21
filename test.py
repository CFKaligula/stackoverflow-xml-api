import requests

base_url = 'http://127.0.0.1:5000'
xml_url = 'https://merapar-assessment-task.s3.eu-central-1.amazonaws.com/3dprinting-posts.xml'
xml_url = 'https://merapar-assessment-task.s3.eu-central-1.amazonaws.com/arabic-posts.xml'
response = requests.post(f'{base_url}/analyze', data={'url': xml_url})
print(response.content)
