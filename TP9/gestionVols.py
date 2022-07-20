from flask import Flask,render_template
from flask import url_for


app = Flask(__name__)

@app.route ('/index.html')
@app.route ('/')
def index():
    vols=[[id,dep,arr,hdep,harr] for (id,dep,arr,hdep,harr) in 
                (ligne.split(' ') for ligne in open('data/flights.txt'))]
    
    return render_template('header_home.html')+render_template('index.html',vols=vols)+render_template('footer.html')

@app.route ('/ajouter.html')
def ajouter() :
    vols=[[id,dep,arr,hdep,harr] for (id,dep,arr,hdep,harr) in 
                (ligne.split(' ') for ligne in open('data/flights.txt'))]
    
    return render_template('header.html',page_name="GSEA - Ajouter")+render_template('ajouter.html',vols=vols)+render_template('footer.html')

@app.route ('/connecter.html')
def connecter() :
    return render_template('header.html',page_name="GSEA - Connexion")+render_template('connecter.html')+render_template('footer.html')

@app.route ('/contact.html')
def contact() :
    return render_template('header.html',page_name="GSEA - Contact")+render_template('contact.html')+render_template('footer.html')

@app.route ('/modifier.html')
def modifier() :
    vols=[[id,dep,arr,hdep,harr] for (id,dep,arr,hdep,harr) in 
                (ligne.split(' ') for ligne in open('data/flights.txt'))]
    return render_template('header.html',page_name="GSEA - Modifier")+render_template('modifier.html',vols=vols)+render_template('footer.html')

@app.route ('/supprimer.html')
def supprimer() :
    vols=[[id,dep,arr,hdep,harr] for (id,dep,arr,hdep,harr) in 
                (ligne.split(' ') for ligne in open('data/flights.txt'))]
    return render_template('header.html',page_name="GSEA - Supprimer")+render_template('supprimer.html',vols=vols)+render_template('footer.html')


if __name__ == '__main__' :
    app.run(debug = True)