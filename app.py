from flask import Flask, render_template, request
from database import load_articles_from_db, load_one_article_from_db,  add_article_to_db
import nltk
nltk.download('punkt')

app = Flask(__name__)


@app.route("/")
def show_homepage():
  return render_template('home.html')


@app.route("/read")
def show_articles():
  articles = load_articles_from_db()
  return render_template('articles.html', articles=articles)


@app.route("/read/<article_id>")
def read_article(article_id):
  article = load_one_article_from_db(article_id)
  content = article['content']
  content_with_linebreaks = content.replace('\n', '<br>')
  return render_template('indi_article.html',
                         art=article,
                         content=content_with_linebreaks)

@app.route("/write")
def write():
  return render_template('write.html')

@app.route("/write/submit", methods=['POST'])
def write_submit():
  data = request.form
  add_article_to_db(data)
  return render_template('article_accepted.html')

@app.route("/test")
def test():
  return render_template('article_accepted.html')
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
