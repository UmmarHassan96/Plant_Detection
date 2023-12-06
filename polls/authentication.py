from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class ApiKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.query_params.get('api_key') or request.data.get('api_key')
        if api_key != 'apikey1234':
            raise AuthenticationFailed('Invalid API key')

        # Returning (None, None) indicates a successful authentication without associating a user.
        return (None, None)
