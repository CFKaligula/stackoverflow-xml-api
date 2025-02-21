# Read Me

## Installation

Requirements:

* Python 3.11

The package installer `uv` is used. Either install this or use your desired package installer and install the dependencies described in the `pyproject.toml`.

To install dependencies with `uv`, run:

```bash
uv sync
```

## Local Setup

### Basic Setup

To run the API in the terminal use the following command:

```bash
python main.py
```

### Setup with Docker

To run the API in a docker container build and run the docker container with the usual commands:

```bash
docker build -t xml-flask-api .
docker run -p 5000:5000 xml-flask-api
```

## Using the API

You can now send an HTTP POST request to `http://127.0.0.1:5000/analyse` with a `url` field in the data field, linking to an XML file.

Example using curl:

```bash
curl http://localhost:5000/xml -d "url=https://merapar-assessment-task.s3.eu-central-1.amazonaws.com/3dprinting-posts.xml" -X POST
```

Example using `request` library in Python:

```python
xml_url = 'https://merapar-assessment-task.s3.eu-central-1.amazonaws.com/arabic-posts.xml'
response = requests.post('http://127.0.0.1:5000/analyse', data={'url': xml_url})
print(response.json())
```
