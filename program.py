from extras import * 
from tasks import * 
from preprocess import * 

class Program:

    def __init__(self):
        self.crawler = Crawler()
        self.gram = Gram()
        self.indexer = Indexer()
        self.baseline_runs = Baseline_Runs()

    def run(self):
        # self.crawler.run()
        # self.gram.run()
        # self.indexer.run()
        # self.indexer.read_positional_index()
        # self.crawler.save_doc_length()
        self.baseline_runs.run()

program = Program()
program.run()