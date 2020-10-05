# -*- coding: utf-8 -*-

import requests

def main():
    # webhook url
    url = "https://hooks.slack.com/services/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"

    text = "안녕? 나는 너의 날씨벗이야."

    payload = {
        "text": text
    }

    requests.post(url, json=payload)

# 이 스크립트에서 실행할 함수는 main
if __name__ == "__main__":
    main()