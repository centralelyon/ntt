import numpy as np

def Texte_to_json(texte):
    data=texte.split('\n')
    texte=Recursive_liste_json(data)
    return(texte)

def Recursive_liste_json(liste,degre=0):
    if len(liste)==1:
        retour=liste[0].split('\t')[-1]
        try:
            retour=int(retour)
        except ValueError:
            try:
                retour=float(retour)
                if np.isnan(retour):
                    retour=None
            except ValueError:
                if retour =='True':
                    retour=True
                elif retour=='False':
                    retour=False
        return(retour)
    elif len(liste)>1:
        
        res=[[],[]]
        for indexe in range(len(liste)):
            t=liste[indexe].split('\t')
            if (len(t)<degre+2):
                res[0].append(indexe)
                res[1].append(t[-1])
        if res[1][0]=='0':
            donne=[]
            
            for i in range(len(res[0])-1):
                donne.append(Recursive_liste_json(liste[res[0][i]+1:res[0][i+1]],degre=degre+1))
            donne.append(Recursive_liste_json(liste[res[0][-1]+1:],degre=degre+1))
        else:
            donne={}
            for i in range(len(res[0])-1):
                donne[res[1][i]]=Recursive_liste_json(liste[res[0][i]+1:res[0][i+1]],degre=degre+1)
            
            donne[res[1][-1]]=Recursive_liste_json(liste[res[0][-1]+1:],degre=degre+1)
        return(donne)