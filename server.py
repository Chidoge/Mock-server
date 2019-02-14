# The address we listen for connections on
listen_ip = "0.0.0.0"
listen_port = 3001

import cherrypy
import json
import os
import urllib3
import socket
import sys

from thread import MyThread

class MainApp(object):

    #CherryPy Configuration
    _cp_config = {'tools.encode.on': True, 
                  'tools.encode.encoding': 'utf-8',
                  'tools.sessions.on' : 'True',
                 }             

    #Catch 404 error
    @cherrypy.expose
    def default(self, *args, **kwargs):
        """The default page, given when we don't recognise where the request is for."""
        page = "404 Error : Website not found"
        cherrypy.response.status = 404
        return page


    #Index page
    @cherrypy.expose
    def index(self):

        return "server up"


@cherrypy.expose
def runMainApp():


    global textPath

    conf = {

        '/static' : {
            'tools.staticdir.on'  : True,
            'tools.staticdir.dir' : os.path.dirname(__file__) + "/serve"
            
        }
    }

    # Create an instance of MainApp and tell Cherrypy to send all requests under / to it. (ie all of them)
    cherrypy.tree.mount(MainApp(), '/',conf)

    # Tell Cherrypy to listen for connections on the configured address and port.
    cherrypy.config.update({'server.socket_host': listen_ip,'server.socket_port': listen_port,'engine.autoreload.on': True,})

    # Start the web server
    cherrypy.engine.start()
    global thread
    thread = MyThread()
    thread.daemon = True
    thread.start()
    # And stop doing anything else. Let the web server take over.
    cherrypy.engine.block()


#-------------------------------------------END---------------------------------------------------#

#Run the function to start everything
runMainApp()

