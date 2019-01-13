from jivago.templating.rendered_view import RenderedView
from jivago.wsgi.annotations import Resource, Path
from jivago.wsgi.invocation.parameters import PathParam
from jivago.wsgi.methods import GET


@Resource("/hello")
class HelloWorldResource(object):

    @GET
    def unnamed_hello(self) -> str:
        return "Hello World!"

    @GET
    @Path("/{name}")
    def path_named_hello(self, name: PathParam[str]) -> str:
        return "Hello {}!".format(name)

    @GET
    @Path("/{name}/template")
    def named_hello_with_a_template(self, name: PathParam[str]) -> RenderedView:
        return RenderedView("named_hello.html", {"name": name})
