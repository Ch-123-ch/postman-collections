from http.client import responses

import requests


def test_write():
    url="https://jsonplaceholder.typicode.com/posts/1"
    json={"userId":1,
          "id":1,
          "title":"sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
          "body":"quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
          }
    r=requests.get(url,json)

    assert r.status_code==200
    assert r.json()["userId"]==1
    assert r.json()["id"]==1
