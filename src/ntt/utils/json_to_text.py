
def Recursive_json(data,degre=0,texte_out=""):
    type_valide=[str,float,int,bool]
    if type(data) in type_valide or data==None:
        texte=str(data)
        texte_part='\t'*degre+texte+'\n'
        return(texte_part)
    elif(isinstance(data,dict)):
        texte_part=''
        for i in data:
            texte_part=texte_part+'\t'*degre+i+'\n'+Recursive_json(data[i],degre=degre+1)
        return(texte_part)
    
    elif(isinstance(data,list)):
        texte_part=''
        for i in range(len(data)):
            texte_part=texte_part+'\t'*degre+str(i)+'\n'+Recursive_json(data[i],degre=degre+1)
        return(texte_part)