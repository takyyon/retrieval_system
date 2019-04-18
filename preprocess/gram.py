from extras import * 

class Gram:

    def __init__(self):
        """
        Constructor: Used to initialize all the class variables
        """
        self.utility = Utility()
        self.file_handling = FileHandling()

    def get_ngrams_formatted(self, ngrams):
        data = ''
        for n in ngrams:
            data += ('$'.join(n)) + '\n'
        return data

    def generate_n_grams(self, folder, gram = 1):
        content_path = 'files/' + folder + '/document-content/'
        gram_path = 'files/' + folder + '/gram_' + str(gram) +'/'
        docs = self.file_handling.get_all_files(content_path)
        print('\n' + self.utility.line_break + '\n' +\
            'Processing the document content to create ' + str(gram) + '-grams.' +\
                'Processed data is available under ' + gram_path)
        for d in docs:
            print('\nReading ' + d + '...')
            content = self.file_handling.read_file(content_path + d)
            ngrams = self.utility.get_and_process_ngrams(content, gram)
            data = self.get_ngrams_formatted(ngrams)
            print('Saving ' + str(gram) + '-grams...')
            self.file_handling.save_file(data, gram_path + d)

    def run(self, folder = 'test-collection', grams = [1]):
        for g in grams:
            self.generate_n_grams(folder, g)

