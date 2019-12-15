"""Falcon API."""

import falcon

from xkcd_api.resources.xkcd_resource import XKCDResource

xkcd_resource = XKCDResource()
api = application = falcon.API()
api.add_route('/{id}', xkcd_resource)
