# XKCD API

A RESTful wrapper for the XKCD API.

## Yet Another XKCD Wrapper

The XKCD team provides access to their excellent comics via a simple [JSON interface](https://xkcd.com/json.html). This interface does not supprt [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing), which means that [SPAs](https://en.wikipedia.org/wiki/Single-page_application) written in languages like JavaScript are typically unable to interact with the interface.

The purpose of this API is to provide a proxy to the XKCD interface with proper CORS support.

