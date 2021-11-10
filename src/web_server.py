from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from news import Nnews
from dbpy import Data, Base

scrap = Nnews()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qwerty123@localhost/py4'
datab = SQLAlchemy(app)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    sh = []
    text = request.form['text']
    for x in range(10):
        sh.append(scrap.newspull(text, x))
    for x in range(10):
        upd = datab.session.query(Data).filter_by(news_id = (x+1)).first()
        upd.news_text = sh[x]
        datab.session.commit()
    return '''
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
    '''.format(sh[0], sh[1], sh[2], sh[3], sh[4], sh[5], sh[6], sh[7], sh[8], sh[9])

if __name__ == '__main__':
    app.run(debug=True)