from server.auth import OIDCAuthenticationBackend

class KeycloakAuthenticated(OIDCAuthenticationBackend):
    def has_permission(self, request, view):
       return not (request.user and request.user.is_authenticated)