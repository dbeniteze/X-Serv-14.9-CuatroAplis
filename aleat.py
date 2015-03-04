#!/usr/bin/python

import webapp
import random


class Aleat(webapp.app):

    def process(self, parsedRequest):
        """Process the relevant elements of the request.
        Returns the HTTP code for the reply, and an HTML page.
        """
        direccion_aleat = random.randint(0, 10000000)
        html = ("<html><body><h1>Hello World!" +
                "</h1></body></html>" +
                '<a href=' "/aleat/"+ str(direccion_aleat) +
                '>Dame otra </a>' +
                "\r\n")
        return ("200 OK", html)

