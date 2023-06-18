class WebsocketJWTAuthenticationMiddleware:
    def __init__(self,app):
        self.app = app

    async def __call__(self,scope,recieve,send):
        headers_dict = dict(scope['headers'])
        cookies_str
        print(headers_dict)

        return await self.app(scope,recieve,send)
    