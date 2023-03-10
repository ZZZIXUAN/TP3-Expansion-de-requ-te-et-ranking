import json


def get_document():
    request = input('input your request:')  # lit une requête de l’utilisateur
    token_user = request.split()
    with open(r"index.json", 'r') as fp:
        index = json.loads(fp.read())
    with open(r"documents.json", 'r') as fp:
        documents = json.loads(fp.read())
    inter = list(set(token_user).intersection(set(index.keys())))
    print(inter)

    sort = []
    filter_token = 0
    for token in inter:  # la tokenise et la transforme
        if token in ['to', 'with', 'on']:
            filter_token = filter_token + 1
        else:
            print(token)
            document = index[token]
            print(document)
            for doc in document:
                weight = (doc, document[doc]['count'])
                print(weight)
                sort.append(weight)
            print('\n')
    sort.sort(key=lambda x: x[1], reverse=True)  # fonction de ranking

    count = 0
    with open('result.json', 'w') as fp:  # liste de retour
        for element in sort:
            document_index = int(element[0])
            title = documents[document_index]['title']
            url = documents[document_index]['url']
            print(title)
            print(url)
            print('---------------------------------------------------------')
            count = count + 1
            fp.write(str({"title": title, "url": url, }) + "\n")

    with open("metadata.json", "w") as fp:  # metadata
        fp.write(str({"Total Index": len(inter), "Filtered Index": len(inter) - filter_token, "Total Records": count}))
