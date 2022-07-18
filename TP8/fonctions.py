def mise_en_tableau(file,tete):
    f=open(file,'r')
    res='<table class="table" text=centered mx-auto w-100><tbody><tr>'
    for item in tete:
        res+= '<td><b>'+item+'</b></td>'
    res+='</tr>'
    for ligne in f:
        res+='<tr>'
        for item in ligne.split(' '):
            res+= '<td>'+item+'</td>'
        res+='</tr>'
    res+='</tbody></table>'
    f.close()
    return res

def charge_html(file):
    res=""
    f=open(file,'r')
    for ligne in f:
        res+=ligne
    return res

    