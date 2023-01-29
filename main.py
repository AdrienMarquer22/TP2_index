from index.index import Index
import argparse




if __name__=="__main__":
    # pour name ajouter le .json

    parser = argparse.ArgumentParser()
    parser.add_argument('--type')
    parser.add_argument('--name',default="index")

    parser.add_argument('--pos', action='store_true',default=False)

    parser.add_argument('--nopos', action='store_true',default=False)

    parser.add_argument('--stem', action='store_true',default=False)



    args = parser.parse_args()

    index=Index(args.type,args.stem)
    index.load_json()

    if args.pos:
        index.create_index_pos()
        index.save_index_pos(args.name + ".pos_index.json")
        index.statistique()
        index.save_statistique("metadata.json")
    if args.nopos:
        index.create_index_no_pos()
        index.save_index_no_pos(args.name + ".non_pos_index.json")
        index.statistique()
        index.save_statistique("metadata.json")
    if not args.nopos and not args.pos:
        print("Select at least one option --pos or --nopos")

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

