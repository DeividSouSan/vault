import unittest

import requests


class TestRoutes(unittest.TestCase):
    def test_get_on_index_should_return_200(self):
        response = requests.get("http://localhost:8080/")
        self.assertEqual(response.status_code, 200, "Status code its not 200")

    def test_get_on_html_content_should_return_200(self):
        response = requests.get("http://localhost:8080/html-content")
        self.assertEqual(response.status_code, 200, "Status code its not 200")

    def test_get_on_md_content_should_return_200(self):
        response = requests.get("http://localhost:8080/md-content")
        self.assertEqual(response.status_code, 200, "Status code its not 200")
