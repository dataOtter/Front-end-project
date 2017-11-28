import flask as f
import DataAccessObject as dao

app = f.Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'


@app.route("/")
def main():
    return f.render_template('index.html')


@app.route("/add", methods=["POST", "GET"])
def add():
    key_value = f.request.json

    for k, v in key_value.items():
        dao.add_key_value_to_db([k, v])
        print(k, v)
        #pair_added = k + v

    return "Pair added to the database"


@app.route("/show_table", methods=["GET"])
def show_table():
    temp_list = []
    all_data = dao.get_all_data_from_db()
    #print(type(all_data), type(all_data[0]), type(all_data[0][0]), all_data)
    for tup in all_data:
        temp_list.append(list(tup))

    return f.jsonify({'one': temp_list})


@app.route("/download_csv", methods=["GET"])
def download_csv():
    return f.send_file('outputs/test.csv',
                       mimetype='text/csv',
                       attachment_filename='test.csv',
                       as_attachment=True)


if __name__ == "__main__":
    app.run()
