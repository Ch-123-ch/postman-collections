import requests
import pytest


def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {"title": "hello", "body": "world", "userId": 1}
    response = requests.post(url, json=data)

    assert response.status_code == 201
    assert response.json()["title"] == "hello"
    assert response.json()["id"] == 101