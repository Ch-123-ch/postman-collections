
import requests


def test_write2():
    url="https://jsonplaceholder.typicode.com/posts/1"

    r=requests.get(url)

    assert r.status_code==200
    assert r.json()["userId"]==1
    assert r.json()["id"]==1
    print("文章测试通过")

    if __name__=="__main__":
        test_write2()
