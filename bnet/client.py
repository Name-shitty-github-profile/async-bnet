from .exceptions import IncorrectMethod


class BattleNetClient(object):
    def __init__(self, connection):
        self.connection = connection
        self._method = None
        self._endpoint = None

    def __getattr__(self, endpoint):
        if not "_" in endpoint: raise IncorrectMethod(endpoint)
        endpoint = endpoint.split('_')
        self._endpoint = '/'.join(endpoint[1:])
        self._method = endpoint[0].upper()
        return self

    def __call__(self, *args, **kwargs):
        return self.connection._make_request(
            method=self._method,
            endpoint=self._endpoint,
            endpoint_arguments='/'.join(args),
            parameters=kwargs
        )
