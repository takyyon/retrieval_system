from extras import * 
from tasks import * 
from preprocess import * 

class Program:

    def __init__(self):
        self.crawler = Crawler()
        self.gram = Gram()

    def run(self):
        # self.crawler.run([])
        # self.gram.run()

program = Program()
program.run()