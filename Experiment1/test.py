import webapp2

class Mainpage(webapp2.RequestHandler):

def get(self):
  self.response.write("Hello word")

app=webapp2.WSGIApplication([('/',Mainpage),],debug=True)
