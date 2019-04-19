from extras import * 

class Common:
    def __init__(self):
        """
        Constructor: Used to initialize all the class variables
        """
        self.utility = Utility()
        self.file_handling = FileHandling()

    def get_doc_length_path(self, stem_folder, folder):
        return 'files/' + folder + '/' + ('stem_' if len(stem_folder) > 0 else '') + 'doc_length'

    def get_score_path(self, stem_folder, score, folder):
        return 'files/' + folder + '/' + stem_folder + score

    def get_ngram_path(self, stem_folder, gram, folder):
        return 'files/' + folder + '/' + stem_folder + 'gram-' + str(gram)

    def get_indexer_path(self, stem_folder, type, gram, folder):
        indexer = 'positional' if type else 'simple'
        return 'files/' + folder + '/' + stem_folder  + indexer + '-index/' + 'gram_' + str(gram)

    def get_queries(self, stem, folder='test-collection'):
        query_file_path = 'files/' + folder + '/' + ('stem_' if stem else '') + 'query.txt'
        print('\n' + self.utility.line_break + '\n' +\
            'Reading Queries from ' +\
                query_file_path)
        queries = self.file_handling.read_file_lines(query_file_path)
        return queries

    def get_document_lengths(self, stem_folder, folder):
        doc_length_file = self.get_doc_length_path(stem_folder, folder)
        lines = self.file_handling.read_file_lines(doc_length_file)
        doc_length = {}
        for l in lines:
            data = l.split()
            doc_length[data[0]] = int(data[1])
        return doc_length

    def get_total_document_length(self, doc_length):
        total = 0.0
        for d in doc_length:
            total += doc_length[d]
        return total