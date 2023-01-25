import json
from index.utils import load_page,tokenize,clean_text,flatten_list
import pandas as pd
from numpyencoder import NumpyEncoder
import numpy as np
from nltk.stem.snowball import SnowballStemmer
import socket

socket.setdefaulttimeout(1)

class Index():
    def __init__(self,type='title') -> None:
        self.liste_urls=[]
        self.title_list=[]
        self.liste_not_valid_url=[]
        self.title_tokenize=[]
        self.index_no_pos=[]
        self.type=type

    def load_json(self,path="data/crawled_urls.json"):
        self.liste_urls = json.load(open(path))

    def get_title_list(self):
        i=0
        for elem in self.liste_urls:
            print((i/500)*100," %   Scraping -> ",elem)
            i+=1
            soup = load_page(elem)
            if soup : 
                try: #when the tag self.type not in the page 
                    self.title_list.append(soup.find(self.type).string)
                except:
                    self.liste_not_valid_url.append(elem)
            else:
                print("pas ok :",elem)
                self.liste_not_valid_url.append(elem)

    def tokenisation(self):
        for link in self.title_list:
            link_clean = clean_text(link)
            self.title_tokenize.append(tokenize(link_clean))
        self.title_tokenize_flatten = flatten_list(self.title_tokenize)



    def create_index_no_pos(self):
        self.get_title_list()
        self.tokenisation()
        df = pd.DataFrame(self.title_tokenize_flatten,columns=["token"])
        df2=df.groupby('token')['token'].count()
        self.index_no_pos=dict(df2)


    def create_index_pos(self):
        self.get_title_list()
        self.tokenisation()
        self.index_pos={}
        for doc_id,title in enumerate(self.title_tokenize):
            for pos,word in enumerate(title):
                if word in self.index_pos and doc_id in self.index_pos[word]:
                    self.index_pos[word][doc_id].append(pos)
                else:
                    self.index_pos.setdefault(word,{}).setdefault(doc_id,[pos])


    def create_stemmer_index_no_pos(self):
        self.get_title_list()
        self.tokenisation()
        stem_word = SnowballStemmer(language="french")
        token_stem= [stem_word.stem(word) for word in self.title_tokenize_flatten]
        df = pd.DataFrame(token_stem,columns=["token"])
        df2=df.groupby('token')['token'].count()
        self.stemmer_index_no_pos=dict(df2)
        



    def statistique(self):
        number_of_doc = len(self.title_list)
        number_of_tokens = len(self.title_tokenize_flatten)
        number_of_token_unique = len(set(self.title_tokenize_flatten))
        average_of_token = number_of_tokens/number_of_doc

        number_of_token_per_doc = [len(elem) for elem in self.title_tokenize]
        variance_of_token = np.var(number_of_token_per_doc)
        self.dict_statistique = {"Number of document":number_of_doc,
                            "Number of total tokens":number_of_tokens,
                            "Number of unique tokens":number_of_token_unique,
                            "Average of token pre document":average_of_token,
                            "Variance of the number of token":variance_of_token}








    def save_index_no_pos(self,name="title.non_pos_index.json"):
        with open(name, 'w') as outfile:
            json.dump(self.index_no_pos, outfile,cls=NumpyEncoder, ensure_ascii=False,indent=4)

    def save_index_pos(self,name="title.pos_index.json"):
        with open(name, 'w') as outfile:
            json.dump(self.index_pos, outfile,cls=NumpyEncoder, ensure_ascii=False,indent=4)

    def save_stemmer_index_no_pos(self,name="mon_stemmer.title.non_pos_index.json"):
        with open(name, 'w') as outfile:
            json.dump(self.stemmer_index_no_pos, outfile,cls=NumpyEncoder, ensure_ascii=False,indent=4)

    def save_statistique(self,name='metadata.json'):
        with open(name, 'w') as outfile:
            json.dump(self.dict_statistique, outfile,cls=NumpyEncoder, ensure_ascii=False,indent=4)










