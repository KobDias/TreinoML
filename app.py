from flask import Flask, render_template, request
import joblib

modelo= joblib.load('knn.pkl') # carregando o modelo pre treinado em pkl

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediz', methods=['POST'])
def prediz():
    try:
        sepal_length = float(request.form.get('sepal_length'))
        sepal_width = float(request.form.get('sepal_width'))
        petal_length = float(request.form.get('petal_length'))
        petal_width = float(request.form.get('petal_width'))

        predicao = modelo.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        especies = predicao[0] # o resultado da predição

        return render_template('index.html', especies=especies)
    
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)