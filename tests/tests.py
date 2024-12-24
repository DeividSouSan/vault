import unittest

import requests


class TestServer(unittest.TestCase):
    def test_get_on_server_should_return_200(self):
        response = requests.get("http://localhost:8080/")
        self.assertEqual(response.status_code, 200, "Status code its not 200")
