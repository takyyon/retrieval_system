from extras import * 

class Common:
    def __init__(self):
        """
        Constructor: Used to initialize all the class variables
        """
        self.utility = Utility()
        self.file_handling = FileHandling()

    def get_document_lengths(self, folder):
        doc_length_file = 'files/' + folder + '/doc_length'
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