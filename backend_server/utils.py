import requests


def send_request(url):
    response = requests.get(url)
    return response


def process_response(response):
    # Logic to process the response
    pass


if __name__ == '__main__':
    url = 'https://example.com'
    response = send_request(url)
    process_response(response)
