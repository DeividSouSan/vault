import subprocess
import tempfile
import time
import unittest

import requests


class TestRoutes(unittest.TestCase):
    process: subprocess.Popen
    markdown_text_example = "# Test Header\n\nThis is a test file."

    @classmethod
    def setUpClass(self):
        with tempfile.NamedTemporaryFile(
            suffix=".md", delete=False, mode="w"
        ) as temp_file:
            temp_file.write(TestRoutes.markdown_text_example)
            temp_filepath = temp_file.name

        TestRoutes.process = subprocess.Popen(
            ["python3", "src/main.py", "--file", temp_filepath],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        time.sleep(1)

    @classmethod
    def tearDownClass(self):
        TestRoutes.process.terminate()
        TestRoutes.process.wait()

    def test_get_on_index_should_return_200(self):
        response = requests.get("http://localhost:8080/")
        self.assertEqual(response.status_code, 200, "Status code its not 200")

    def test_get_on_get_content_should_return_200(self):
        response = requests.get("http://localhost:8080/get-content")

        self.assertEqual(
            response.text, TestRoutes.markdown_text_example, "Response text not right"
        )
        self.assertEqual(response.status_code, 200, "Status code its not 200")

    def test_get_on_style_should_return_200(self):
        response = requests.get("http://localhost:8080/style.css")

        self.assertEqual(response.status_code, 200, "Status code its not 200")


if __name__ == "__main__":
    unittest.main()
