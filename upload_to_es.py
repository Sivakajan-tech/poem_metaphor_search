from elasticsearch import Elasticsearch, helpers
import pandas as pd

es = Elasticsearch("http://localhost:9200", verify_certs=False, basic_auth=['elastic', 'ImqurIpw-n7ZWFKH6Kvv'])
INDEX = 'songs_8'
corpus = pd.read_json('data/corpus.json',encoding='utf-8',typ='series')
mapping = pd.read_json('mapping.json', typ='series')

res = helpers.bulk(es, corpus, index=INDEX)
