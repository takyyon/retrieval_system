from extras import * 
from tasks import * 
from preprocess import * 
import sys
from time import sleep

class Program:

    def __init__(self):
        self.crawler = Crawler()
        self.gram = Gram()
        self.indexer = Indexer()
        self.baseline_runs = Baseline_Runs()
        self.common = Common()
        self.query_highlight = Query_Highlight()
        self.evaluation = Evaluation()
        self.file_handling = FileHandling()
        self.query_expansion = Query_Expansion()
        self.spell_checker = Spell_Checker()

    def get_input(self, prompt):
        return int(input(prompt))

    def get_initial_run(self):
        return self.get_input('1. Test Collection Run\n' +\
            '2. New Run (on new set of URLs)\n3. Exit\n\nYour Option: ')

    def run_query_highlighting(self, folder):
        self.query_highlight.highlight_queries(score='bm25', folder=folder, stopwords=self.stopwords)
        self.query_highlight.highlight_queries(score='tf-idf', folder=folder, stopwords=self.stopwords)
        self.query_highlight.highlight_queries(score='binary-independence', folder=folder, stopwords=self.stopwords)

    def run_query_expansion(self, folder):
        # query expansion: stemming
        self.baseline_runs.run(folder=folder, query_expansion=True)
        # query expansion: pseudo-relevance
        self.baseline_runs.run(folder=folder, query_expansion=False)

    def run_stemmed_document_case(self, folder):

        self.crawler.save_doc_length(folder=folder, stem=True)
        sleep(2)

        self.gram.run(folder=folder, stem=True)
        sleep(2)

        self.baseline_runs.run(stem=True)

    def run_on_folder(self, folder='test-collection'):
        
        self.crawler.run(folder)
        sleep(2)
        
        self.gram.run(folder=folder)
        sleep(2)

        self.crawler.save_doc_length(folder=folder)
        sleep(2)

        self.indexer.run(folder=folder)
        sleep(2)

        self.baseline_runs.run(folder=folder)
        sleep(2)

        self.run_query_expansion(folder=folder)

        self.baseline_runs.run(folder=folder, filter_queries=True)
        sleep(2)

        self.baseline_runs.run(folder=folder, filter_queries=True, query_expansion=True)
        sleep(2)

        self.run_query_highlighting(folder=folder) 
        sleep(2)

        self.evaluation.run(folder=folder)
        sleep(2)

        self.spell_checker.run(queries=self.common.get_queries(stem=True))
        sleep(2)

        self.run_stemmed_document_case(folder=folder)


    def run_fresh_urls(self):
        url_path = input('Give the complete path for the file containing a list of URLS\n' +\
            + ' (Each URL should be in a new line): ')
        urls = self.file_handling.read_file_lines(url_path)
        folder = 'fresh-run'
        self.crawler.crawl_urls(folder, urls)
        self.run_on_folder(folder)

    def run(self):
        inp = self.get_initial_run()
        if inp == 3:
            print('Exiting...')
            exit()
        self.stopwords = self.common.get_stopwords()
        self.gram.set_stopwords(self.stopwords)
        if inp == 1:
            self.run_on_folder()
            return
        self.run_fresh_urls()
        
program = Program()
program.run()