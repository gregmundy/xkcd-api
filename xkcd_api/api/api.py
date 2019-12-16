"""Falcon API."""

import falcon

from xkcd_api.resources.xkcd_resource import XKCDResource
from xkcd_api.helpers.cors import CORSComponent

xkcd_resource = XKCDResource()
api = application = falcon.API(middleware=[CORSComponent()])
api.add_route('/{id}', xkcd_resource)
