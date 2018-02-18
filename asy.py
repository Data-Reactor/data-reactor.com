import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('templates/cover.html')

def make_app():
	return tornado.web.Application([
		(r"/", MainHandler),
		(r"/static/(.*)", tornado.web.StaticFileHandler, {"path": './static'}),
	])

if __name__ == "__main__":
	app = make_app()
	app.listen(80)
	tornado.ioloop.IOLoop.current().start()

