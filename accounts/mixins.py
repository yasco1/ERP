from django.conf import settings

class JWTSetCookieMixin:
    def finalize_response(self,request,response,*args,**kwargs):
        token = response.data.get("refresh")
        if token:
            response.set_cookie(settings.SIMPLE_JWT['REFRESH_TOKEN_NAME'],
                                response.data.get("refresh"),
                                max_age=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                                httponly=True,
                                samesite=settings.SIMPLE_JWT['JWT_COOKIE_SAMESITE'],
                                )
            response.set_cookie(settings.SIMPLE_JWT['ACCESS_TOKEN_NAME'],
                                response.data.get("access"),
                                max_age=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                                httponly=True,
                                samesite=settings.SIMPLE_JWT['JWT_COOKIE_SAMESITE']
                                )
            # del response.data['refresh']
            # del response.data['access']

        else :
            response.set_cookie(settings.SIMPLE_JWT['REFRESH_TOKEN_NAME'],
                                    "",
                                    max_age=0,
                                    httponly=True,
                                    samesite=""
                                    )
            response.set_cookie(settings.SIMPLE_JWT['ACCESS_TOKEN_NAME'],
                                    "",
                                    max_age=0,
                                    httponly=True,
                                    samesite=""
                                    )

        return super().finalize_response(request,response,*args,**kwargs)

class JWTDeleteCookieMixin:
    def finalize_response(self,request,response,*args,**kwargs):
        response.set_cookie(settings.SIMPLE_JWT['REFRESH_TOKEN_NAME'],
                                "",
                                max_age=0,
                                httponly=True,
                                samesite=""
                                )
        response.set_cookie(settings.SIMPLE_JWT['ACCESS_TOKEN_NAME'],
                                "",
                                max_age=0,
                                httponly=True,
                                samesite=""
                                )
        return super().finalize_response(request,response,*args,**kwargs)