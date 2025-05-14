import unittest
from katas.nginx_log_parser import parse_log  # Replace with your actual filename
from typing import Dict

class TestParseLog(unittest.TestCase):

    def test_valid_log_entry(self):
        log = (
            '122.176.223.47 - - [05/Feb/2024:08:29:40 +0000] '
            '"GET /web-enabled/Enhanced-portal/bifurcated-forecast.js HTTP/1.1" 200 1684 '
            '"-" "Opera/9.58 (X11; Linux i686; en-US) Presto/2.12.344 Version/13.00"'
        )

        expected: Dict[str, str] = {
            'client_ip': '122.176.223.47',
            'date': '05/Feb/2024:08:29:40 +0000',
            'http_method': 'GET',
            'path': '/web-enabled/Enhanced-portal/bifurcated-forecast.js',
            'http_version': '1.1',
            'status': '200',
            'response_bytes': '1684',
            'user_agent': 'Opera/9.58 (X11; Linux i686; en-US) Presto/2.12.344 Version/13.00'
        }

        self.assertEqual(parse_log(log), expected)

    def test_invalid_log_format(self):
        invalid_log = 'some random non-log string'
        with self.assertRaises(ValueError):
            parse_log(invalid_log)

    def test_missing_user_agent(self):
        log_missing_ua = (
            '192.168.1.1 - - [10/May/2025:14:32:10 +0000] '
            '"POST /api/data HTTP/2.0" 404 0 "-" "-"'
        )
        expected = {
            'client_ip': '192.168.1.1',
            'date': '10/May/2025:14:32:10 +0000',
            'http_method': 'POST',
            'path': '/api/data',
            'http_version': '2.0',
            'status': '404',
            'response_bytes': '0',
            'user_agent': '-'
        }

        self.assertEqual(parse_log(log_missing_ua), expected)

if __name__ == '__main__':
    unittest.main()
