import pandas_datareader.data as web
import webbrowser
import datetime
import matplotlib.pyplot as plt
import numpy as np
import json
from firebase import firebase
from firebase_admin import credentials, initialize_app, storage,firestore
# Init firebase with your credentials
cred = credentials.Certificate(r"serviceAccountKey.json")
initialize_app(cred, {'storageBucket': 'stock-data-fc41e.appspot.com'})
firebase = firebase.FirebaseApplication('https://stock-data-fc41e-default-rtdb.firebaseio.com/', None)
result = firebase.get('/Analysis/', '')
data = json.dumps(result)
resp = json.loads(data)
finalz=resp['ed']
finaly=resp['em']
finalx=resp['ey']
finalr=resp['sd']
finalq=resp['sm']
finalp=resp['sy']
x=int(finalx)
y=int(finaly)
z=int(finalz)
p=int(finalp)
q=int(finalq)
r=int(finalr)
start= datetime.datetime(p,q,r)
end= datetime.datetime(x,y,z)
result = firebase.get('/Stocks/', '')
data = json.dumps(result)
resp = json.loads(data)
finalb=resp['s1']
finalc=resp['s2']
finald=resp['s3']
tesla=web.DataReader(finalb,'yahoo',start,end)
ford=web.DataReader(finalc,'yahoo',start,end)
gm=web.DataReader(finald,'yahoo',start,end)
#open prices
tesla['Open'].plot(label='TSLA Open price',figsize=(15,6))
gm['Open'].plot(label='GM Open price')
ford['Open'].plot(label='F Open price')
plt.title(' Stock Prices of cars companys')
plt.ylabel('Stock Price')
plt.legend()
plt.savefig("graphopenprice.jpg")

# Put your local file path 
fileName = r"graphopenprice.jpg"
bucket = storage.bucket()
blob = bucket.blob("graphopenprice")
blob.upload_from_filename(fileName)

# Opt : if you want to make public access from the URL
blob.make_public()
print("your file url", blob.public_url)
db = firestore.client()
doc_ref = db.collection(u'stock').document(u'data')
doc_ref.set({
     u'img-link': blob.public_url,
})
#volume traded &interpretations
tesla['Volume'].plot(label="Tesla",figsize=(10,7))
ford['Volume'].plot(label="Ford")
gm['Volume'].plot(label="Tesla")
plt.legend()
plt.savefig("volume_traded.jpg")

# Put your local file path 
fileName = r"volume_traded.jpg"
bucket = storage.bucket()
blob = bucket.blob("volume_traded")
blob.upload_from_filename(fileName)

# Opt : if you want to make public access from the URL
blob.make_public()

print("your file url", blob.public_url)
def run_re():
     import webbrowser
     return(webbrowser.open('https://stock-py-fb-self.vercel.app/', new=0, autoraise=True))
run_re()