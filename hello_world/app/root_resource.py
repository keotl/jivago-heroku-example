import jivago
from jivago.templating.rendered_view import RenderedView
from jivago.wsgi.annotations import Resource
from jivago.wsgi.methods import GET


@Resource("/")
class RootResource(object):

    @GET
    def root_message(self) -> RenderedView:
        return RenderedView("home.html", {"version": jivago.__version__})
