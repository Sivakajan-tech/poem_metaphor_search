from flask import Flask, render_template, request
from searchquery import *
from elasticsearch_dsl import Index

app = Flask(__name__, template_folder='templates')


@app.route('/advanced_search', methods=['GET', 'POST'])
def advanced_search():
    if request.method == 'POST':

        query = request.form['searchTerm2']
        res = search_advanced_query(query)
        fields = query
        hits = res['hits']['hits']
        time = res['took']

        num_results = res['hits']['total']['value']

        return render_template('output.html', query=fields, hits=hits, num_results=num_results, time=time)

    if request.method == 'GET':
        # pdb.set_trace()
        return render_template('output.html', init='True')


@app.route('/filter_search', methods=['GET', 'POST'])
def filter_search():
    import pdb
    if request.method == 'POST':
        fields = {}
        print(request)
        Author = {
            "vairamuthu": "வைரமுத்து",
            "damarai": "தாமரை",
            "visj": "வ. ஐ. ச. ஜெயபாலன்",
            "tshankar": "தபு ஷங்கர்",
            "vali": "கவிஞர் வாலி",
            "leena": "லீனா மணிமேகலை"
        }

        if request.form['Author'] != 'none':
            fields["Author"] = Author[request.form['Author']]

        fields["year"] = {
            "gte": int(request.form['start_year']),
            "lte": int(request.form['end_year'])
        }

        # check request.form dict have basic or advanced key
        res = basic_multiple_filter_search(fields)

        hits = res['hits']['hits']
        time = res['took']

        num_results = res['hits']['total']['value']

        return render_template('output.html', query=fields, hits=hits, num_results=num_results, time=time)

    if request.method == 'GET':
        # pdb.set_trace()
        return render_template('output.html', init='True')





@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':

        query = request.form['searchTerm']
        res = fundamental_search(query)
        fields = query
        hits = res['hits']['hits']
        time = res['took']

        num_results = res['hits']['total']['value']

        return render_template('output.html', query=fields, hits=hits, num_results=num_results, time=time)

    if request.method == 'GET':
        # pdb.set_trace()
        return render_template('output.html', init='True')


@app.route('/column_search', methods=['GET', 'POST'])
def column_search():
    if request.method == 'POST':

        query = request.form['searchTerm3']
        column = request.form['poem_column']
        res = column_vise_search(query,column)
        fields = query
        hits = res['hits']['hits']
        time = res['took']

        num_results = res['hits']['total']['value']

        return render_template('output.html', query=fields, hits=hits, num_results=num_results, time=time)

    if request.method == 'GET':
        # pdb.set_trace()
        return render_template('output.html', init='True')


if __name__ == '__main__':
    app.debug = True
    app.run(port=6997)
