import re
from typing import Dict

def parse_log(log: str) -> Dict[str, str]:
    pattern = re.compile(
        r'(?P<client_ip>\S+)\s+-\s+-\s+'
        r'\[(?P<date>[^\]]+)\]\s+'
        r'"(?P<http_method>\S+)\s+(?P<path>\S+)\s+HTTP/(?P<http_version>[\d.]+)"\s+'
        r'(?P<status>\d{3})\s+(?P<response_bytes>\d+)\s+'
        r'"[^"]*"\s+"(?P<user_agent>[^"]+)"'
    )

    match = pattern.match(log)
    if not match:
        raise ValueError("Invalid log format")

    return match.groupdict()


if __name__ == "__main__":
    log_entry = (
        '122.176.223.47 - - [05/Feb/2024:08:29:40 +0000] '
        '"GET /web-enabled/Enhanced-portal/bifurcated-forecast.js HTTP/1.1" 200 1684 '
        '"-" "Opera/9.58 (X11; Linux i686; en-US) Presto/2.12.344 Version/13.00"'
    )

    parsed_log = parse_log(log_entry)
    print("Parsed log data:", parsed_log)
