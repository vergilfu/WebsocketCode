from flask import Flask,request
from flask_cors import CORS
from sqlalchemy.orm import sessionmaker
import json
from sqlalchemy import create_engine
from method import notebookmethod

app = Flask("lovestory")
CORS(app)

@app.route('/notebooks/<ac>',methods=['POST'])
def notebooksfunc(ac):
    with open('./configjson.json', encoding='utf-8') as f:
        configs = json.load(f)
    engine = create_engine(configs['dburl'])
    Session = sessionmaker(bind=engine)
    session = Session()
    if ac == 'loaddata':
        return notebookmethod.loadData(db=session,req=request.get_json())
    if ac == 'new':
        return notebookmethod.new(db=session,req=request.get_json())


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8085)