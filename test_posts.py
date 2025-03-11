import requests
import pytest

# Базовый URL API
BASE_URL = "https://jsonplaceholder.typicode.com/posts"


# Фикстура для создания нового поста
@pytest.fixture
def new_post():
    return {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }


def test_create_post(new_post):
    """
    Тест для создания нового поста
    """
    try:
        response = requests.post(BASE_URL, json=new_post)
        response.raise_for_status()
    except requests.RequestException as e:
        pytest.fail(f"Ошибка запроса: {e}")
    assert response.status_code == 201
    assert response.json()["title"] == "foo"
    assert response.json()["body"] == "bar"
    assert response.json()["userId"] == 1


def test_get_all_posts():
    """
    Тест для получения списка постов
    :return:
    """
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
    except requests.RequestException as e:
        pytest.fail(f"Ошибка запроса: {e}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_post_by_id(post_id):
    """
    Тест для получения конкретного поста по ID
    """
    try:
        response = requests.get(f"{BASE_URL}/{post_id}")
        response.raise_for_status()
    except requests.RequestException as e:
        pytest.fail(f"Ошибка запроса: {e}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_update_post_put(post_id):
    """
    Тест для полного обновления поста
    """
    updated_post = {
        "id": post_id,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    try:
        response = requests.put(f"{BASE_URL}/{post_id}", json=updated_post)
        response.raise_for_status()
    except requests.RequestException as e:
        pytest.fail(f"Ошибка запроса: {e}")
    assert response.status_code == 200
    assert response.json()["title"] == "updated title"
    assert response.json()["body"] == "updated body"


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_delete_post(post_id):
    """
    Тест для удаления поста по ID
    """
    try:
        response = requests.delete(f"{BASE_URL}/{post_id}")
        response.raise_for_status()
    except requests.RequestException as e:
        pytest.fail(f"Ошибка запроса: {e}")
    assert response.status_code == 200
    assert response.text == "{}"
