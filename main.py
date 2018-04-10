
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

def process_set(terms, query, table):
    answer = table[terms[0]]
    if "and" in query:
        for t in terms[1:]:
            answer = answer & table[t]

    elif "or" in query:
        for t in terms[1:]:
            answer = answer | table[t]

    elif "not" in query:
        for t in terms[1:]:
            answer = answer - table[t]

    
    answer = sorted(answer)
    # print(answer)
    
    return answer


if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--source',
                       default='source.csv',
                       help='input source data file name')
    parser.add_argument('--query',
                        default='query.txt',
                        help='query file name')
    parser.add_argument('--output',
                        default='output.txt',
                        help='output file name')
    args = parser.parse_args()
    
    # Please implement your algorithm below
    
    # TODO load source data, build search engine
    id_title = {}
    file = args.source
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace(u'\ufeff', '')
            line = line.strip().split(',', 1)
            id_title[int(line[0])] = line[1]

    # read query.txt find words
    inverted_index = {}
    with open(args.query, 'r') as f:
        queries = f.readlines()
        rep = {" and ": " ", " or ": " ", " not ": " "}
        for query in queries:
            query = query.strip()
            query = replace_all(query, rep).split(" ")
            for term in query:
                if term not in inverted_index:
                    inverted_index[term] = set()


    # build inverted index:
    print("build inverted index")
    for i in range(1, len(id_title)+1):
        for term in inverted_index:
            if term in id_title[i]:
                inverted_index[term].add(i)



    # print(inverted_index)


    # TODO compute query result
    result = []
    print("process query:")
    with open(args.query, 'r') as f:
        queries = f.readlines()
        rep = {" and ": " ", " or ": " ", " not ": " "}
        for query in queries:
            query = query.strip()
            terms = replace_all(query, rep).split(" ")
            answer = process_set(terms, query, inverted_index)

            if answer == []:
                answer = [0]
            result.append(answer)
    print("result")

    # TODO output result
    with open(args.output, 'w') as wf:
        for r in result[:-1]:
            wf.write(','.join(str(e) for e in r))
            wf.write('\n')
        wf.write(','.join(str(e) for e in result[-1]))
