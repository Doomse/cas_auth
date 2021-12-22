from django.conf import settings
from django.utils import crypto
from requests.api import get
from . import models
from urllib import parse
import requests


def register_username(user):
    if user is None:
        return

    
    
    #Set new password for 'authadmin' account (to be created/reserved at setup)
    password = crypto.get_random_string(32)
    authadmin, _ = models.User.objects.get_or_create(username=settings.AUTH_USERNAME)
    authadmin.set_password(password)
    authadmin.save()


    #Log in on clients that need the username, create user object and log out
    for client in settings.REGISTER_ON_CLIENTS:
        with requests.Session() as s:
            cl_parse = parse.urlsplit(client['URL'])

            url = parse.urlunsplit( (cl_parse.scheme, cl_parse.netloc, client['LOGIN_PATH'], '', '') )
            r1 = s.get(url)

            host_parse = parse.urlsplit(r1.url)

            hostname = 'localhost.local' if host_parse.hostname == 'localhost' else host_parse.hostname #requests does this for localhost cookies
            r2 = s.post(r1.url, headers={'X-CSRFToken': s.cookies.get('csrftoken', domain=hostname)}, data={'username': settings.AUTH_USERNAME, 'password':password})

            hostname = 'localhost.local' if cl_parse.hostname == 'localhost' else cl_parse.hostname #requests does this for localhost cookies
            url = parse.urlunsplit( (cl_parse.scheme, cl_parse.netloc, client['REGISTER_PATH'], '', '') )
            r3 = s.post(url, headers={'X-CSRFToken': s.cookies.get('csrftoken', domain=hostname)}, data={'username': user.username})

            hostname = 'localhost.local' if cl_parse.hostname == 'localhost' else cl_parse.hostname #requests does this for localhost cookies
            url = parse.urlunsplit( (cl_parse.scheme, cl_parse.netloc, client['LOGOUT_PATH'], '', '') )
            r4 = s.get(url)


    #Set unusable password for 'authadmin'
    authadmin.set_unusable_password()
    authadmin.save()