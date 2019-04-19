from extras import * 

class Indexer:

    def __init__(self):
        """
        Constructor: Used to initialize all the class variables
        """
        self.utility = Utility()
        self.file_handling = FileHandling()


    def update_index(self, grams, doc):
        for i in range(len(grams)):
            gram = grams[i]
            if gram.strip() is '':
                continue
            if gram not in self.indexer:
                self.indexer[gram] = {}
            if doc not in self.indexer[gram]:
                self.indexer[gram][doc] = []
            ln = len(self.indexer[gram][doc])
            ind = i
            if ln > 0:
                ind += self.indexer[gram][doc][ln - 1]
            self.indexer[gram][doc].append(ind)

    def create_save_indexer(self, folder, grams):
        for gram in grams:
            self.indexer = {}
            print('\n' + self.utility.line_break + '\n' +\
            'Processing the ' + str(gram) + '-grams to create a index.')
            ngram_path = 'files/' + folder + '/gram_' + str(gram) + '/'
            docs = self.file_handling.get_all_files(ngram_path)
            for d in docs:
                print('Updating the index with ' + d + '...')
                ngram_content = self.file_handling.read_file_lines(ngram_path + d)
                self.update_index(ngram_content, d)
            self.save_index(folder, gram)
            self.save_index(folder, gram, True)


    def save_index(self, folder, gram, positional = False):
        indexer_file = 'files/' + folder +\
            ('/positional_index' if positional else '/simple_index') + '/gram_' + str(gram)
        print('\n' + self.utility.line_break + '\n' +\
            'Saving ' + ('positional' if positional else 'simple') + ' index..' + '\n' +\
            'Processed data is available under ' + indexer_file)
        data = ''
        for term in self.indexer:
            data += term + ' ' + str(len(self.indexer[term])) + '\n'
            for doc in self.indexer[term]:
                data += doc + ' ' + str(len(self.indexer[term][doc])) + '\n'
                if positional:
                    data += ','.join([str(x) for x in self.indexer[term][doc]]) + '\n'
        self.file_handling.save_file(data, indexer_file)

    def read_simple_index(self, folder='test-collection', gram=1):
        indexer_file = 'files/' + folder + '/simple_index/gram_' + str(gram)
        print('\n' + self.utility.line_break + '\n' +\
            'Reading simple index from ' + indexer_file)
        lines = self.file_handling.read_file_lines(indexer_file)
        indexer = {}
        i = 0
        while i < len(lines):
            data = lines[i].split()
            term = data[0]
            indexer[term] = {}
            doc_freq = int(data[1])
            i += 1
            for j in range(doc_freq):
                data = lines[i].split()
                indexer[term][data[0]] = int(data[1])
                i += 1 
        return indexer

    def read_positional_index(self, folder='test-collection', gram=1):
        indexer_file = 'files/' + folder + '/positional_index/gram_' + str(gram)
        print('\n' + self.utility.line_break + '\n' +\
            'Reading positional index from ' + indexer_file)
        lines = self.file_handling.read_file_lines(indexer_file)
        indexer = {}
        i = 0
        while i < len(lines):
            data = lines[i].split()
            term = data[0]
            indexer[term] = {}
            doc_freq = int(data[1])
            i += 1
            for j in range(doc_freq):
                data = lines[i].split()
                i += 1
                positions = lines[i].split(',')
                indexer[term][data[0]] = [int(x) for x in positions]
                i += 1
        return indexer

    def run(self, folder='test-collection', grams=[1]):
        self.create_save_indexer(folder, grams)