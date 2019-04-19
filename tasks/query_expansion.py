from extras import * 
from common import Common
from indexer import Indexer
import math
import nltk
import operator
from collections import defaultdict
from nltk.stem import SnowballStemmer
from nltk.corpus import wordnet

class Query_Expansion:

    def __init__(self):
        """
        Constructor: Used to initialize all the class variables
        """
        self.utility = Utility()
        self.frequency_map = defaultdict()
        self.file_handling = FileHandling()
        self.common = Common()
        self.indexer = Indexer()
        self.positional_index  = self.indexer.read_index(index_type=True)

    def generate_expected_words_for_expansion(self, queries):
        stopWords = self.utility.get_stop_list()
        stemmer = SnowballStemmer("english")
        for i in range (0,len(queries)):
            query = queries[i]
            listofwords = []
            words = query.split()
            for word in words:
                word = word.lower()
                stem = stemmer.stem(word)
                expected = self.fetch_expected_words(word,stem)
                if expected not in stopWords:
                    frequency = self.generate_frequency_map(word,expected)
                    if frequency > 0:
                        listofwords.append(expected)

            self.frequency_map[i+1] = listofwords

        return self.frequency_map


    def generate_frequency_map(self,word,stem):
        occurrences = 0
        if stem in self.positional_index and word in self.positional_index:
            dict_stem = self.positional_index[stem]
            dict_word = self.positional_index[word]

            for doc in dict_word:
                if doc in dict_stem:
                    list1 = dict_word[doc]
                    list2 = dict_stem[doc]
                    pos1 = 0
                    for i in range(0, len(list1)):
                        pos1 = pos1 + list1[i]
                        pos2 = 0
                        for j in range(0, len(list2)):
                            pos2 = pos2 + list2[j]
                            if abs(pos1 - pos2) <= 12:
                                occurrences = occurrences + 1
                                break

        return occurrences

    def fetch_expected_words(self,word,stem):
        if self.utility.check_word_exist(stem):
            return stem
        else:
            return nltk.stem.WordNetLemmatizer().lemmatize(word)

    def expand_queries_using_stemming(self, queries):
        stem_map = self.generate_expected_words_for_expansion(queries)
        updated_query_map = defaultdict(set)
        for i in range(len(queries)):
            stop_words = self.utility.get_stop_list()
            listofwords = stem_map[i+1]
            for word in listofwords:
                for syn in wordnet.synsets(word):
                    for l in syn.lemmas():
                        if str(l.name) not in  queries[i] and '_' not in str(l.name) and str(l.name) not in stop_words:
                            updated_query_map[i+1].add(l.name())
                            if (len(updated_query_map[i+1])) > 4:
                                break
                    if len(updated_query_map[i+1]) > 4:
                        break

        new_queries = []

        for i in range (len(queries)):
            old_query = queries[i]
            new_query = old_query
            for word in updated_query_map[i+1]:
                new_query = new_query + " "+ str(word)
            new_queries.append(new_query)
        return new_queries
    