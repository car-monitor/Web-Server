class RenderHandler(BaseHandler):

    def get(self, input):
        self.render(input + '.html')
