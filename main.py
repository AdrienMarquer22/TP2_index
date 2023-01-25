from index.index import Index

if __name__=="__main__":

    test=Index()

    test.load_json()


    test.get_title_list()


    test.tokenisation()
    test.title_tokenize.append(['karine', 'lacombe', 'karine'])

    test.create_index_pos()

    test.save_index_pos()

    test.create_index_no_pos()

    test.save_index_no_pos()

    test.create_stemmer_index_no_pos()

    test.save_stemmer_index_no_pos()