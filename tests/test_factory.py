from accomodation_website import create_app


def test_config():
    assert not create_app().testing
