from extras import * 
from tasks import * 
from preprocess import * 

class Program:

    def __init__(self):
        self.crawler = Crawler()
        self.gram = Gram()
        self.indexer = Indexer()

    def run(self):
        # self.crawler.run()
        # self.gram.run()
        # self.indexer.run()
        self.crawler.save_doc_length()

program = Program()
program.run()