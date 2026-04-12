from contextlib import nullcontext

import requests

def test_post():
    url="https://jsonplaceholder.typicode.com/posts"
    r=requests.post(url,json={"title":"独立测试",
                              "body":"chen",
                              "userId":66
                              })

    assert r.status_code==201
    assert r.json()["id"] is not None
    assert r.json()["title"]=="独立测试"
    assert r.json()["body"]=="chen"



