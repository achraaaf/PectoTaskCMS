import json
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///words.db'
db = SQLAlchemy(app)

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    translation = db.Column(db.String(100), nullable=False)
    example_sentence = db.Column(db.String(200), nullable=True)

def load_data():
    with open('sm1_new_kap1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        word_first_lang = item.get('wordFirstLang')
        sentence_first_lang = item.get('sentenceFirstLang')
        word_second_lang = item.get('wordSecondLang')
        sentence_second_lang = item.get('sentenceSecondLang')

        if word_first_lang:  
            new_word = Word(
                word=word_first_lang,
                translation=word_second_lang,
                example_sentence=sentence_first_lang
            )

            db.session.add(new_word)
    
    db.session.commit()

with app.app_context():
    db.create_all() 
    load_data() 

@app.route("/", methods=["GET"])
def index():
    search_query = request.args.get("search", "") 
    page = request.args.get("page", 1, type=int) 

    if search_query:
        words = Word.query.filter(Word.word.like(f"%{search_query}%")).paginate(page=page, per_page=5)
    else:
        words = Word.query.paginate(page=page, per_page=5)

    return render_template("index.html", words=words, search=search_query)


@app.route("/edit/<int:id>", methods=["GET"])
def edit_word(id):
    word = Word.query.get_or_404(id)  
    return render_template("edit.html", word=word)

@app.route("/update/<int:id>", methods=["POST"])
def update_word(id):
    word = Word.query.get_or_404(id)
    word.word = request.form["word"]
    word.translation = request.form["translation"]
    word.example_sentence = request.form["example_sentence"]
    
    
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
