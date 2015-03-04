#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import aleat
import suma


class hola(webapp.app):
    def process(self, parsedRequest):
        return ("200 OK", "<html><body>Hola</body></html>\r\n")


class adios(webapp.app):
    def process(self, parsedRequest):
        return ("200 OK", "<html><body>Adios</body></html>\r\n")

if __name__ == "__main__":
    hola = hola()
    adios = adios()
    aleat = aleat.Aleat()
    suma = suma.suma()
    app = {"/hola": hola, "/adios": adios, "/aleat": aleat, "/suma": suma}
    try:
        testWebApp = webapp.webApp("localhost", 1234, app)
    except KeyboardInterrupt:
        print "Key board interrupt detected."
