from jivago.wsgi.annotations import Resource
from jivago.wsgi.methods import GET


@Resource("/")
class RootResource(object):

    @GET
    def root_message(self) -> str:
        return "Hello-World-as-a-Service, built using Jivago Framework v0.0.5."

