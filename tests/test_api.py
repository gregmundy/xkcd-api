"""Unit Tests.

A collection of unit tests for the XKCD API.

"""

import falcon
from expects import expect, be, have_key

VALID_KEYS = [
    'month',
    'num',
    'link',
    'year',
    'news',
    'safe_title',
    'transcript',
    'alt',
    'img',
    'title'
]


class TestAPI:
    """API test class.

    For convenience, all unit tests for the XKCD API are encapsulated into
    this class.

    """

    def test_fetch_latest(self, client):
        """Test the ability to fetch the latest XCKD comic."""

        resp = client.simulate_get('/')
        expect(resp.status).to(be(falcon.HTTP_200))
        for key in VALID_KEYS:
            expect(resp.json).to(have_key(key))

    def test_fetch_specific_comic(self, client):
        """Test the ability to fetch a specific XCD comic by its identifier."""

        resp = client.simulate_get('/1')
        expect(resp.status).to(be(falcon.HTTP_200))
        for key in VALID_KEYS:
            expect(resp.json).to(have_key(key))

        resp = client.simulate_get('/1000000')
        expect(resp.status).to(be(falcon.HTTP_404))
