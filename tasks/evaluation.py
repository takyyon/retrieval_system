from extras import * 
from common import Common
from indexer import Indexer
import math
from .baseline_runs import Baseline_Runs
from .query_highlight import Query_Highlight
import operator

class Evaluation:

    def __init__(self):
        """
        Constructor: Used to initialize all the class variables
        """
        self.utility = Utility()
        self.file_handling = FileHandling()
        self.common = Common()
        self.query_highlight = Query_Highlight()
        self.baseline_runs = Baseline_Runs()

    def evaluate_model(self, score, queries, folder):
        

    def run(self, stem=False, folder='test-collection'):
        self.stem_folder = 'stem-' if stem else ''
        queries = self.common.get_queries(stem, folder)
        scores = ['bm25', 'binary-independence', 'tf-idf']
        for score in scores:
            self.evaluate_model(score, queries, folder)