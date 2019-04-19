from extras import * 
from common import Common
from indexer import Indexer
import math
from .baseline_runs import Baseline_Runs
import operator

class Query_Highlight:

    def __init__(self):
        """
        Constructor: Used to initialize all the class variables
        """
        self.utility = Utility()
        self.file_handling = FileHandling()
        self.common = Common()
        self.indexer = Indexer()
        self.baseline_runs = Baseline_Runs()
        self.threshold_length = 10

    def find_index(self, index, content, end=False):
        if end:
            while index < len(content) and (content[index] != ' ' or content[index] != '\n'):
                index += 1
            if index >= len(content):
                return len(content)
            return index
        
            while index >= 0 and (content[index] != ' ' or content[index] != '\n'):
                index -= 1
            if index < 0:
                return 0
            return index - 1

    def generate_query_snippets(self, query_len, len_checked, query, folder, doc):
        raw_doc_path = self.common.get_raw_doc_path(self.stem_folder, folder) + '/' + doc
        raw_html_content = self.file_handling.read_file(raw_doc_path)
        html_tags = self.utility.getAllHTMLTags(raw_html_content, 'pre')
        content = ' '.join([x.get_text() for x in html_tags])
        term_index = content.find(query)
        if term_index == -1:
            return []
        len_left = query_len - len_checked - len(query)
        beg = self.find_index(term_index - len_checked - self.threshold_length, content)
        end = self.find_index(term_index + len_left + self.threshold_length, content, True)
        return [content[beg:end]]

    def get_total_hits(self, result):
        total = 0
        for r in result:
            total += len(result[r])
        return total

    def save_snippets(self, index, query, folder, result):
        query_snippet_path = self.common.get_query_snippet_path(self.stem_folder, folder) + '/' + str(index)
        data = 'Snippets for the query:  ' + query + '\n' + self.utility.line_break + '\n'
        total_hits = self.get_total_hits(result)
        print('Saving snippets for ' + query + ' to ' + query_snippet_path + '....')
        if total_hits == 0:
            data += 'No snippets found for the query..'
        else:
            data += 'Total Hits:  ' + str(total_hits) + '\n' + self.utility.line_break + '\n\n'
            for r in result:
                data += self.utility.line_break + '\nDocument:  ' + r + '\n' + self.utility.line_break
                for s in result[r]:
                    data += s + '\n' + self.utility.line_break + '\n'
                data += '\n'
        self.file_handling.save_file(data, query_snippet_path)
        
    def highlight_query(self, stem, index, query, folder, score):
        top_docs = self.baseline_runs.read_top_documents_for_score(stem, folder, index, 100, score)
        trigrams = self.utility.get_and_process_ngrams(query, 3)
        query_len = len(query)
        result = {}
        len_checked = 0
        print('\nProcessing ' + query + '...')
        for gram in trigrams:
            temp_query = ' '.join(gram)
            for d in top_docs:
                snippets = self.generate_query_snippets(query_len, len_checked, temp_query, folder, d)
                for s in snippets:
                    if d not in result:
                        result[d] = {}
                    if s not in result[d]:
                        result[d][s] = True
            len_checked += len(gram[0])
        self.save_snippets(index, query, folder, result)

    def highlight_queries(self, folder='test-collection', stem= False, score='bm25'):
        self.stem_folder = 'stem-' if stem else ''
        queries = self.common.get_queries(stem, folder)
        print('\n' + self.utility.line_break + '\n' +\
            'Processing queries  to generate snippets.')
        for i in range(len(queries)):
            higlighted = self.highlight_query(stem, i, queries[i], folder, score)
        

    