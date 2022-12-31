# JWT DEMO
## TABLE OF CONTENT 
* [Introduction](#introduction)
* [Techs Used](#tech-used)
* [Initial Setup](#initial-set-up)
* [Authentification](#authentification) 
* [JWT](#jwt-authentication)
* [Cor Headers](#cor-headers)  
* [Registration](#registration)

## INTRODUCTION

Backend API Development for JWT Project

## TECH USED

* Python
* Django Rest Framework
* dj-rest-auth with django-allauth for registration
* simple JWT

## Iniital Set Up

1. Install django rest framework : ``` pip install djangorestframework ```.
2. Add ``` rest_framework ``` to apps.
3. install drf-spectacular to document endpoints and add ```drf_spectacular ``` apps and update urls. 
Include templates and update templates in settings. Add drf-spectacular to REST_FRAMEWORK in settings.py.


## Authentication

1. pip install ``` pip install dj-rest-auth ```

If registration is required following must be installed:

* ```pip install django-allauth``` and add following to apps:

- 'django.contrib.sites'
- 'allauth'
- 'allauth.account'
- 'allauth.socialaccount'
- 'dj_rest_auth'
- 'rest_framework.authtoken'
- 'dj_rest_auth.registration'

- SITE_ID = 1

* must include allauth in main app urls to make use of allauth templates
* dj-rest-auth registration email confirmation urls must be redirected to allauth url.

2. update urls in main app to include dj-rest-frameworj urls.

``` path('dj-rest-auth/', include('dj_rest_auth.urls')), ```
``` path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')) ```

At this stage we are using dj-rest-framework default athentification system which returns a token when hitting the login endpoint.


## JWT Authentication

JsonWebToken authentication implemented using simple jwt as per document [here](#https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

1. ``` pip install djangorestframework-simplejwt ```
2. update REST_AUTH in settings.py by adding ```rest_framework_simplejwt.authentication.JWTAuthentication ```
3. update urls in main.app urls with:
    ```
    from rest_framework_simplejwt.views import (
    TokenObtainPairView,
        TokenRefreshView,
    )
    urlpatterns = [
        ...
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        ...
    ]
    ```

At this stage with have created the login token endpoints which will return token, and refresh token when hitting this endpoint.

4. Customise cookie headers as follows:

```JWT_AUTH_COOKIE = 'my-app-auth'```
```JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'```

```
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    }
```

Setting REST_USE_JWT = True will make the /drf-rest-auth/login return a bearer token is so required.

Notes: The email confirmation view does not exist with dj-rest-auth so it must me redirected to the django-allauth or 
custom template made.
