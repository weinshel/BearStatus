# request handler for editing page (/edit) goes here
# assume admin login has already been handled

import cgi
from google.appengine.api import users
import webapp2


class Edit(webapp2.RequestHandler):


app = webapp2.WSGIApplication([
    ('/edit', Edit)
], debug=True)