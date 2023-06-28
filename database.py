from sqlalchemy import create_engine, text
import os

connection_info = os.environ['connection_info']

engine = create_engine(connection_info, connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"}
})

def load_articles_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from articles"))
    articles = []
    for row in result.all():
      articles.append(dict(row._asdict()))
  return articles

with engine.connect() as conn:
  result = conn.execute(text("select * from articles ORDER BY article_id DESC"))
  articles = []
  for row in result.all():
    articles.append(dict(row._asdict()))

def load_one_article_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from articles where article_id = :val"), {"val":id})
    row=result.fetchall()
  return dict(row[0]._asdict())

def add_article_to_db(data):
  with engine.connect() as conn:
    query = text("INSERT INTO articles (title, writer, summary, content) VALUES(:title, :writer, :summary, :content)")
    variables = {"title":data['title'], "writer":data['writer'], "summary":data['summary'], "content":data['content']}
    conn.execute(query, variables)

"""test = load_one_article_from_db(1)
print(test)"""


    

