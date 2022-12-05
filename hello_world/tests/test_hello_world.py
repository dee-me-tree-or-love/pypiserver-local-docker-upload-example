from hello_world import __version__, hello


def test_version():
    assert __version__ == "0.1.0"


def test_hello():
    assert hello("foo") == "hello foo"
