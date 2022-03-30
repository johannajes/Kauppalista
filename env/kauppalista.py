from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///testi.db'
db = SQLAlchemy(app)

class Lista(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(160), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Tuote %r' % self.id


@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        list_content = request.form['content']
        new_item=Lista(content=list_content)

        try:
            db.session.add(new_item)
            db.session.commit()
            return redirect ('/')
        except:
            return 'Lisäys ei onnistunut'
    else:
        tuotteet = Lista.query.order_by(Lista.date).all()
        return render_template('index.html', tuotteet=tuotteet)

@app.route('/poista/<int:id>')
def poista(id):
    poistettava=Lista.query.get_or_404(id)
    try:
        db.session.delete(poistettava)
        db.session.commit()
        return redirect ('/')
    except:
        return 'Poisto ei onnistunut'
@app.route('/paivita/<int:id>', methods=['POST','GET'])
def paivita(id):
    paivitettava=Lista.query.get_or_404(id)
    if request.method=="POST":
        paivitettava.content=request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Päivitys ei onnistunut'
    else:
        return render_template('update.html', tuote=paivitettava)
if __name__=="__main__":
    app.run(debug=True)




