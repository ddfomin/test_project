import pytest
import requests

class TestHTTP:
    @pytest.mark.parametrize("post_id", [1, 2, 40, 22])
    def test_get_post(self, base_url, post_id):
        number_post = f"/posts/{post_id}"
        result = requests.get(base_url + number_post)
        assert result.status_code == 200
        assert "title" in result.json()

    @pytest.mark.parametrize("userid", [1, 2, 3, 4])
    def test_create_post(self, base_url, userid):
        result = requests.post(base_url + "/posts", json={"title": "foo", "body": "bar", "userId": f"{userid}"})
        print(result.json())
        assert result.status_code == 201


    def test_404(self, base_url):
        num = 99999
        number_post = f"/posts/{str(num)}"
        result = requests.get(base_url + number_post)
        assert result.status_code == 404