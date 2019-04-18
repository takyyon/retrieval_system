from extras import * 
from time import sleep

class Crawler:

    def __init__(self):
        """
        Constructor: Used to initialize all the class variables
        """
        self.utility = Utility()
        self.file_handling = FileHandling()

    def save_document_content(self, folder, tag = 'pre'):
        content_path = 'files/' + folder + '/document-content/'
        raw_html_path = 'files/' + folder + '/raw-documents/'
        docs = self.file_handling.get_all_files(raw_html_path)
        print('\n' + self.utility.line_break + '\n' +\
            'Processing the Raw HTML. Parsing and tokenizing the article.' +\
                'Processed data is available under ' + content_path)
        for d in docs:
            print('\nReading ' + d + '...')
            html_content = self.file_handling.read_file(raw_html_path + d)
            content = self.utility.getAllHTMLTags(html_content, tag)
            data = ''
            for c in content:
                data += self.utility.parse(c.get_text()) + ' '
            tokenized_data = self.utility.tokenize(data).strip()
            print('Saving Document content...')
            self.file_handling.save_file(tokenized_data, content_path + d)
    
    def get_header(self, html):
        headers = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        for header in headers:
            content = self.utility.getAllHTMLTags(html_content, header)
            if len(content) > 0:
                return content[0]
        return self.utility.get_random_string()

    def crawl_urls(self, folder, urls):
        raw_html_path = 'files/' + folder + '/raw-documents/'
        print('\n' + self.utility.line_break + '\n' +\
            'Processing Url and saving the raw html content.' +\
                'Processed data is available under ' + raw_html_path)
        for url in urls:
            html = self.utility.getHtml(url)
            header = self.get_header(html)
            self.file_handling.save_file(html, raw_html_path + header)
            sleep(1)

    def run(self, folder='test-collection', urls=[]):
        self.file_handling.create_folder('files/' + folder)
        self.crawl_urls(folder, urls)
        self.save_document_content(folder, 'p')