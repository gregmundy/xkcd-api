"""Unit Tests.

A collection of unit tests for the XKCD API.

"""


class TestAPI:
    """API test class.

    For convenience, all unit tests for the XKCD API are encapsulated into
    this class.

    """

    def test_fetch_latest(self, client):
        """Test the ability to fetch the latest XCKD comic."""

        resp = client.simulate_get('/')
        print(resp.json)

    def test_fetch_specific_comic(self, client):
        """Test the ability to fetch a specific XCD comic by its identifier."""

        resp = client.simulate_get('/1')
        print(resp.json)
