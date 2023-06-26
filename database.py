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
  result = conn.execute(text("select * from articles"))
  articles = []
  for row in result.all():
    articles.append(dict(row._asdict()))

def load_one_article_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from articles where article_id = :val"), {"val":id})
    row=result.fetchall()
  return dict(row[0]._asdict())

"""test = load_one_article_from_db(1)
print(test)"""


    

