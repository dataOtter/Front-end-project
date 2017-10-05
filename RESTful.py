import flask as f
import DataAccessObject as dao

app = f.Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'
pair_added = ''

@app.route("/")
def main():
    return f.render_template('index.html')


@app.route("/add", methods=["POST"])
def add():
    key_value = f.request.json

    for k, v in key_value.items():
        dao.add_key_value_to_db([k, v])
        print(k, v)
        #pair_added = k + v

    return f.render_template('index.html')


@app.route("/add_success", methods=["GET"])
def add_success():
    added = "Added to the database"
    #show_list()
    return f.jsonify({'value': added})


@app.route("/show_list", methods=["GET"])
def show_list():
    temp_list = []
    all_data = dao.get_all_data_from_db()
    #print(type(all_data), type(all_data[0]), type(all_data[0][0]), all_data)
    for tup in all_data:
        temp_list.append(list(tup))
    json_dict = {'one': temp_list}
    #print("the data " + str(json_dict))

    return f.jsonify(json_dict)

if __name__ == "__main__":
    app.run()
