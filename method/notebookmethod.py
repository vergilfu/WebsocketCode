from modules.dbmodules import Notebooks

def loadData(db, req):
    return db.query(Notebooks).all()

def new(db, req):
    new_note = Notebooks(ftitle=req['ftitle'], fcontent=req['fcontent'], fnodename=req['fnodename'],
                         fnodeid=req['fnodeid'], fparentnodename=req['fparentnodename'],
                         fparentnodeid=req['fparentnodeid'])
    db.add(new_note)
    db.commit()

