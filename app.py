from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediz', methods=['POST'])
def prediz():
    request.form.get(float('sepal_length'))
    request.form.get(float('sepal_width'))
    request.form.get(float('petal_length'))
    request.form.get(float('petal_width'))



if __name__ == '__main__':
    app.run(debug=True)