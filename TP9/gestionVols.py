from flask import Flask,render_template
from flask import url_for


app = Flask(__name__)

@app.route ('/index.html')
@app.route ('/')
def index():
    vols=[[id,dep,arr,hdep,harr] for (id,dep,arr,hdep,harr) in 
                (ligne.split(' ') for ligne in open('data/flights.txt'))]
    
    return render_template('index.html',vols=vols)

@app.route ('/ajouter.html')
def ajouter() :
    return render_template('ajouter.html')

@app.route ('/connecter.html')
def connecter() :
    return render_template('connecter.html')

@app.route ('/contact.html')
def contact() :
    return render_template('contact.html')

@app.route ('/modifier.html')
def modifier() :
    return render_template('modifier.html')

@app.route ('/supprimer.html')
def supprimer() :
    return render_template('supprimer.html')


if __name__ == '__main__' :
    app.run(debug = True)