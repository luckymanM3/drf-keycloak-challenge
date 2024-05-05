from django.contrib.auth.models import Group
from django.db import transaction
from mozilla_django_oidc import auth
import requests
import json
import jwt


class OIDCAuthenticationBackend(auth.OIDCAuthenticationBackend):

    def create_user(self, claims):
        user = super(OIDCAuthenticationBackend, self).create_user(claims)

        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.save()

        self.update_groups(user, claims)

        return user

    def update_user(self, user, claims):
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.save()
        self.update_groups(user, claims)

        return user

    def update_groups(self, user, claims):
        """
        Transform roles obtained from keycloak into Django Groups and
        add them to the user. Note that any role not passed via keycloak
        will be removed from the user.
        """
        with transaction.atomic():
            user.groups.clear()
            for role in claims.get('roles'):
                group, _ = Group.objects.get_or_create(name=role)
                group.user_set.add(user)

    def get_userinfo(self, access_token, id_token, payload):

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": f"application/x-www-form-urlencoded"
        }
        response = requests.get("http://192.168.64.131:8080/realms/management/protocol/openid-connect/userinfo", headers=headers)
        if response.status_code == 200:
            userinfo = json.loads(response.text)
            # userinfo["roles"] = userinfo["groups"]

            print("userinfo: ", userinfo)
            print("id_token: ", id_token)
            print("access token: ", access_token)
            print("header: ", headers)
            return userinfo
            
        else: 
           raise Exception(f"Failed to get user info: {response.text}")