from INDEX.index import Index

if __name__=="__main__":

    test=Index()

    test.load_json()


    test.get_title_list()


    test.tokenisation()
    test.title_tokenize.append(['karine', 'lacombe', 'karine'])

    print( test.title_tokenize)

    test.create_index_pos()

    print(test.index_pos)

    test.save_index_pos('test.json')