from extras import * 
from tasks import * 
from preprocess import * 

class Program:

    def __init__(self):
        self.crawler = Crawler()
        self.gram = Gram()
        self.indexer = Indexer()
        self.baseline_runs = Baseline_Runs()
        self.common = Common()
        self.query_highlight = Query_Highlight()

    def run(self):
        # self.crawler.process_stem_documents()
        # self.crawler.run()
        # self.gram.run(True)
        # self.crawler.save_doc_length()
        # self.crawler.save_doc_length(True)
        # self.indexer.run()
        # self.indexer.read_index()
        # self.indexer.read_index('test-collection', True)
        # self.baseline_runs.run()
        # stopwords = self.common.get_stopwords()
        self.query_highlight.highlight_queries() 
        # queries = self.common.process_test_queries()     

program = Program()
program.run()