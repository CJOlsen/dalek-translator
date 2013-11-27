import os
from flask import Flask, jsonify, render_template, request, redirect, url_for
import words


app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/_aj', methods=['GET'])
def dalekify():
    new_word = request.args.get('word', "error", type=str)
    return jsonify(result=words.dalekify(new_word))

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about')
def about():
    return redirect(url_for('static', filename='about.html'))

if __name__ == '__main__':
    app.run()

