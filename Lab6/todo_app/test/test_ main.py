from fastapi.testclient import TestClient

from ..src.main import app, hello_world

client = TestClient(app)

books = [
    {
        "id": 1,
        "title": "The sun Also Rises",
        "author": "Ernest Hemingway",
        "category": "fiction",
    },
    {
        "id": 2,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "category": "fiction",
    },
    {
        "id": 3,
        "title": "Skin in the Game",
        "author": "Nassem Talib",
        "category": "non-fiction"
    }
]


def test_first_api():
    assert hello_world() == {"msg": "hello world"}
    print(hello_world())


def test_read_main():
    response = client.get("/books/3")
    assert response.status_code == 200
    assert response.json() == {
        "id": 3,
        "title": "Skin in the Game",
        "author": "Nassem Talib",
        "category": "non-fiction"
    }


def test_path():
    response = client.get("/book/msg")
    assert response.status_code == 200
    assert response.json() == {"msg": "msg"}


def test_query():
    response = client.get("/books/?title=little")
    assert response.status_code == 200
    assert response.json() == {"msg": "little"}


def test_both():
    response = client.get("/both/msg/?title=little")
    assert response.status_code == 200
    assert response.json() == {"msg": "little msg"}


def test_post():
    response = client.post("/book", json={
        "id": 5,
        "title": "title5",
        "description": "description5",
        "category": "category5"
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": 5,
        "title": "title5",
        "description": "description5",
        "category": "category5"
    }


def test_put():
    response = client.put("/books/3", json={
        "id": 3,
        "title": "title3",
        "description": "description3",
        "category": "category3"
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": 3,
        "title": "title3",
        "description": "description3",
        "category": "category3"
    }


def test_delete():
    response = client.delete("/book/3")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "title": "The sun Also Rises",
            "author": "Ernest Hemingway",
            "category": "fiction",
        },
        {
            "id": 2,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "category": "fiction",
        },
        {
            'id': 5,
            'title': 'title5',
            'description': 'description5',
            'category': 'category5'}
    ]