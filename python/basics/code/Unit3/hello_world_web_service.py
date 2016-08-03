"""
Module used to create a simple webservice that you are able to make a GET
request and return "Hello World" from.
"""

from tornado.web import Application, RequestHandler


class ExampleRequestHandler(RequestHandler):
    """

    """

    def get(self):
        self.write("Hello, world")

    @staticmethod
    def make_app():
        return Application([
            (r"/", ExampleRequestHandler),
        ])
