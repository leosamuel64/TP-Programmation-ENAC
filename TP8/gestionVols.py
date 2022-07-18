from flask import Flask
from flask import url_for
from fonctions import *

menu="""

<nav class="navbar navbar-light navbar-expand-lg">
    <a class="navbar-text btn fs-5" href="/">Home</a>
    <a class="navbar-text btn fs-5" href="afficher">Afficher</a>
    <a class="navbar-text btn fs-5" href="supprimer">Supprimer</a>
    <a class="navbar-text btn fs-5" href="presentation">Présentation</a>
</nav>
"""
        
head="""
<!DOCTYPE html>
<html lang="fr">

<head>
  <meta charset="UTF-8" />
  <title>Mon nouveau site</title>
  <link rel="shortcut icon" type="image/png" href="images/favicon.png" />
  <!-- <link rel="stylesheet" href="css/style.css" /> -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
    integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g=="
    crossorigin="anonymous" referrerpolicy="no-referrer" />
  <!-- CSS only -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
</head>

<script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/js/all.min.js"
  integrity="sha512-6PM0qYu5KExuNcKt5bURAoT6KCThUmHRewN3zUFNaoI6Di7XJPTMoT6K0nsagZKk2OB4L7E3q1uQKHNHd4stIQ=="
  crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js"
  integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>

"""

app = Flask(__name__)
@app.route ('/')
def index() :
    content=head+menu+    """
    <b>Index</b><br>
    <img src='/static/images/slide-6.jpg' width="200" height="200"/>
    """
    return content

@app.route ('/afficher')
def afficher() :
    content= head+menu+   """
    <div><b>Afficher</b></div>
    
                """ + mise_en_tableau('TP8/flights.txt',['Date','Immat','Départ','Destination','Appareil'])
    return content


@app.route ('/supprimer')
def suppression_vols() :
    content=  head+menu+  """
    <b>supprimer</b><br>
    
                """
    return content

@app.route ('/presentation')
def presentation() :
    content=   head+menu+ """
    
                """
    return content

if __name__ == '__main__' :
    app.run(debug = True)
