import flask as f

app = f.Flask(__name__)

@app.route("/")
def main():
    return f.render_template('index.html')

if __name__ == "__main__":
    app.run()
