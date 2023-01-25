from index.index import Index
import argparse




if __name__=="__main__":
    # pour name ajouter le .json

    parser = argparse.ArgumentParser()
    parser.add_argument('--type')
    parser.add_argument('--name',default="index")

    parser.add_argument('--pos', action='store_true',default=False)

    parser.add_argument('--nopos', action='store_true',default=False)

    parser.add_argument('--stem_nopos', action='store_true',default=False)



    args = parser.parse_args()

    index=Index(args.type)
    index.load_json()

    if args.pos:
        index.create_index_pos()
        index.save_index_pos(args.name + ".json")
        index.statistique()
        index.save_statistique("metadata.json")
    elif args.nopos:
        index.create_index_no_pos()
        index.save_index_no_pos(args.name + ".json")
        index.statistique()
        index.save_statistique("metadata.json")
    elif args.stem_nopos:
        index.create_stemmer_index_no_pos()
        index.save_stemmer_index_no_pos(args.name + ".json")
        index.statistique()
        index.save_statistique("metadata.json")
    else:
        print("Select on option --pos or --nopos or --stem_nopos")

    # test=Index()

    # test.load_json()


    # test.get_title_list()


    # test.tokenisation()
    # test.title_tokenize.append(['karine', 'lacombe', 'karine'])

    # test.create_index_pos()

    # test.save_index_pos()

    # test.create_index_no_pos()

    # test.save_index_no_pos()

    # test.create_stemmer_index_no_pos()

    # test.save_stemmer_index_no_pos()

