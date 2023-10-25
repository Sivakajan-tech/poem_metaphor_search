from elasticsearch import Elasticsearch

# INDEX = 'metaphor_search'
INDEX = 'songs_8'
client = Elasticsearch("http://localhost:9200", verify_certs=False,
                   http_auth=['elastic', 'ImqurIpw-n7ZWFKH6Kvv'],)

def fundamental_search(query):
    qus = {
        "query": {
            "query_string": {
                "query": query
            }
        },
        "from": 0,
        "size": 10000
    }
    
    res = client.search(index=INDEX, body=qus)
    
    return res

def basic_multiple_filter_search(fields):
    """
    {
        'query': {
            'bool': {
                'must': [
                    {'match': {'Author': 'தாமரை'}},
                    {'range': {'year': {'gte': 2000, 'lte': 2020}}}
                ]
            }
        }
    }
    """
    q = {}
    q["query"] = {}
    q["query"]["bool"] = {}
    q["query"]["bool"]["must"] = []

    print(fields)
    
    for field in fields:
        if field == 'year':
            q["query"]["bool"]["must"].append({"range":{field:fields[field]}})
        else:
            q["query"]["bool"]["must"].append({"match":{field:fields[field]}})
    q.update({ "from": 0,"size": 10000})
    res = client.search(index=INDEX, body=q)
    return res


def search_advanced_query(query):
    qus = {
        "query": {
            "query_string": {
                "query": "*"+query+"*"
            }
        },
        "from": 0,
        "size": 10000
    }

    res = client.search(index=INDEX, body=qus)

    return res

def column_vise_search(query, column):
    qus = {
        "query": {
            "match": {
                column: query
            }
        },
        "from": 0,
        "size": 10000
    }
    print(qus)
    res = client.search(index=INDEX, body=qus)

    return res

# def exact_search(query):
"""
example Query
   "query": {
            "multi_match": {
                "query": "மலர்களே, வானவில்லாய்",
                "type": "best_fields",
                "operator": "or",
                "fields": ["Poem"]}
        },
        "from": 0,
        "size": 10000
"""
#     q = {
#         "query": {
#             "multi_match": {
#                 "query": query,
#                 "type": "phrase",
#                 "operator": "OR"
#             }
#         },
#         "from": 0,
#         "size": 10000
#     }
#     res = client.search(index=INDEX, body=q)
#     return res

# GET /songs_8/_search
# {
#   "aggs": {
#     "aggs_author": {
#       "terms": {
#         "field": "Author.keyword"
#       }
#     }
#   }
# }