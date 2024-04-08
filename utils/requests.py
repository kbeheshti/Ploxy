import aiohttp

xcsrf_methods = {"post", "patch", "put", "delete"}


class RequestClient:
    def __init__(self, cookie):
        self.session = aiohttp.ClientSession()
        self.cookie = cookie

    async def request(self, method: str, url: str, **kwargs) -> dict:
        xcsrf_required = method in xcsrf_methods
        res = await self.session.request(method, **kwargs)

        if xcsrf_required:
            self.session.headers["X-CSRF-Token"] = res.headers["X-CSRF-Token"]
            if res.status != 200:
                res = await self.session.request(method, url, **kwargs)

        if res.status != 200:
            res.raise_for_status()
        else:
            return await res.json()
