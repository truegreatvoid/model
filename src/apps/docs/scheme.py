from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.plumbing import build_bearer_security_scheme_object


class JWTAuthScheme(OpenApiAuthenticationExtension):
    target_class = 'model_apps.core.jtw_authentication.JWTAuthentication'
    name = 'bearerAuth'

    def get_security_definition(self, auto_schema):
        return build_bearer_security_scheme_object(
            header_name='Authorization',
            token_prefix='Bearer',
        )
