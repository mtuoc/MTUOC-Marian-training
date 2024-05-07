import codecs
import sys

fentrada=sys.argv[1]
measure=sys.argv[2]
number=int(sys.argv[3])

entrada=codecs.open(fentrada,"r",encoding="utf-8")

data={}
for linia in entrada:
    linia=linia.rstrip()
    camps=linia.split(":")
    try:
        checkpoint=camps[3].replace("Up. ","").strip()
        measure2=camps[4].strip()
        value=float(camps[5].strip())
        if measure2==measure:
            data[checkpoint]=value
    except:
        pass

sorteddict=dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

cont=0
results=[]
for d in sorteddict:
    print(d, sorteddict[d])
    results.append(d)
    cont+=1
    if cont>=number:
        break
        
cadena=[]
for d in results:
    c="model.iter"+str(d)+".npz"
    cadena.append(c)
    
print(" ".join(cadena))
