# galeriazyskow/tests/responses/__init__.py

import os

from scrapy.http import Response, Request

def fake_response_from_file(file_name, url=None):
    """
    Create a Scrapy fake HTTP response from a HTML file
    :param file_name: filename from the responses directory
    :param url: the URL of the response
    :return: a scrapy HTTP response which can be used for unittesting
    """
    if not url:
        url = 'http://galeriazyskow.pl/komentarz-pln-pln-bez-wiekszych-zmian-pomimo-dobrych-danych-31-01-2018r/'

    request = Request(url=url)
    if file_name:
        file_path = file_name

    file_content = open(file_path, 'r').read()

    response = Response(url=url, request=request, body=file_content)
    response.encoding = 'utf-8'
    return response
