from hello import greet


def test_greet():
    result = greet("Git")
    assert result == "Hello, Git"