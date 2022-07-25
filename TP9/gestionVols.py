from flask import Flask,render_template,request,redirect,session
from flask import url_for
from fonctions import *
from flask_session import Session


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

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
    
    return render_template('header.html',page_name="GSEA - Ajouter")+render_template('ajouter.html',vols=vols,aeroport=liste_aeroport())+render_template('footer.html')

@app.route ('/connecter.html')
def connecter() :
    return render_template('header.html',page_name="GSEA - Connexion")+render_template('connecter.html')+render_template('footer.html')

@app.route ('/contact.html')
def contact() :
    return render_template('header.html',page_name="GSEA - Contact")+render_template('contact.html')+render_template('footer.html')

@app.route ('/modifier.html')
def modifier(modif=False,num=0) :
    vols=[[id,dep,arr,hdep,harr] for (id,dep,arr,hdep,harr) in 
                (ligne.split(' ') for ligne in open('data/flights.txt'))]
    return render_template('header.html',page_name="GSEA - Modifier")+render_template('modifier.html',vols=vols,modif=modif,num=num)+render_template('footer.html')
        
@app.route ('/supprimer.html')
def supprimer() :
    vols=[[id,dep,arr,hdep,harr] for (id,dep,arr,hdep,harr) in 
                (ligne.split(' ') for ligne in open('data/flights.txt'))]
    return render_template('header.html',page_name="GSEA - Supprimer")+render_template('supprimer.html',vols=vols)+render_template('footer.html')


@app.route('/supprimer.html/<message>')
def numVolSuppr(message) :
    vols=[[id,dep,arr,hdep,harr] for (id,dep,arr,hdep,harr) in 
                (ligne.split(' ') for ligne in open('data/flights.txt'))]
    vols.pop(convert_int(message)-1)
    file=open('data/flights.txt','w')
    for (id,dep,arr,hdep,harr) in vols:
        file.write(id+' '+dep+' '+arr+' '+hdep+' '+harr)
    file.close()
    
    page="""
            <html>
                <head>
                    <meta http-equiv="Refresh" content="0; url=/supprimer.html" />
                </head>
            </html>
    """
    return page
    
@app.route('/resultat',methods = ['GET'])
def ajouteVol():
    
    result=request.args
    immat = result['immat']
    dep = result['dep']
    arr = result['arr']
    hdep = result['hdep']
    harr = result['harr']
    
    vols=[[id,dep,arr,hdep,harr] for (id,dep,arr,hdep,harr) in 
                (ligne.split(' ') for ligne in open('data/flights.txt'))]
    
    vols.append((immat,dep,arr,hdep,harr))
    
    file=open('data/flights.txt','w')
    for (id,dep,arr,hdep,harr) in vols:
        file.write(id+' '+dep+' '+arr+' '+hdep+' '+harr.strip()+'\r')
    file.close()
    
    page=   """
            <html>
                <head>
                    <meta http-equiv="Refresh" content="0; url=/ajouter.html" />
                </head>
            </html>
            """
    return page

@app.route('/modifier_page.html')
def modif_page():
    return render_template('header.html',page_name="GSEA - Supprimer")+render_template('modif_page.html',aeroport=liste_aeroport(),num=session['num'],vol=session['vol'],)+render_template('footer.html')
    

@app.route('/modifier.html/<message>')
def modifVol(message) :
    num=convert_int(message)
    vols=[[id,dep,arr,hdep,harr] for (id,dep,arr,hdep,harr) in 
                (ligne.split(' ') for ligne in open('data/flights.txt'))]
    session['num']=num-1
    res=[]
    
    for i in vols[num-1]:
        res.append(i.strip())
    session['vol']=res
    return redirect('/modifier_page.html') 

@app.route('/resultat_modif',methods = ['GET'])
def modif():
    
    result=request.args
    immat = result['immat']
    dep = result['dep']
    arr = result['arr']
    hdep = result['hdep']
    harr = result['harr']
    
    vols=[[id,dep,arr,hdep,harr] for (id,dep,arr,hdep,harr) in 
                (ligne.split(' ') for ligne in open('data/flights.txt'))]
    
    vols[session['num']]=((immat,dep,arr,hdep,harr))
    
    file=open('data/flights.txt','w')
    for (id,dep,arr,hdep,harr) in vols:
        file.write(id+' '+dep+' '+arr+' '+hdep+' '+harr.strip()+'\r')
    file.close()
    
    page=   """
            <html>
                <head>
                    <meta http-equiv="Refresh" content="0; url=/modifier.html" />
                </head>
            </html>
            """
    return page


if __name__ == '__main__' :
    app.run(debug = True)