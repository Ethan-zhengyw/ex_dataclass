# -*- coding: utf-8 -*-

from feishu.types import MsgReq

body = MsgReq(**{
    "receive_id": "xxxxx",
    "msg_type": "text",
    "content": {
        "zh_cn": {
            "title": "title1",
            "content": [
                []
            ]
        },
        "en_us": {}
    }
})

if __name__ == "__main__":
    print(body)

