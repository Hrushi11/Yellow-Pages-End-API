from yellow_pages_api import YpApi
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/api', methods = ['POST', 'GET'])
def api():
    if request.method == 'GET':
        # return f"The URL /api is accessed directly. Try going to route to submit form"
        return render_template("error.html")    
    if request.method == 'POST':
        api = YpApi()
        form_data = request.form
        json_arr = api.scrape_extractor_multi(form_data["term"], form_data["location"], int(form_data["plier"]))
        api_dict = api.get_api(json_arr)
        return jsonify(api_dict)

@app.route("/<string:term>/<string:location>")
def getApi(term, location):
    api = YpApi()
    json_arr = api.scrape_extractor_multi(term, location, 1)
    api_dict = api.get_api(json_arr)
    return jsonify(api_dict)

@app.route("/<string:term>/<string:location>/<int:plier>")
def getApiwithPlier(term, location, plier=1):
    api = YpApi()
    json_arr = api.scrape_extractor_multi(term, location, plier)
    api_dict = api.get_api(json_arr)
    return jsonify(api_dict)


if __name__ == "__main__":
    app.run(debug=True)