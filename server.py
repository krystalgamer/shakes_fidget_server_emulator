from bottle import Bottle, request
from keys import *
from Crypto.Cipher import AES
import base64
from sf_requests import *
import sqlite3

app = Bottle()

conn = sqlite3.connect('db.sql')
cursor = conn.cursor()

#cursor.execute('CREATE TABLE players(id PRIMARY_KEY INT, username TEXT, password TEXT, email TEXT, sex INT, race INT, class INT, face TEXT, unk5 INT)')
#conn.commit()

#/sfgame_cfg.php?rnd=0.4670932721346617&client=windows%202.81.31&version=885116b401e56d21a6e99c7a2838cbf7
@app.route('/sfgame_cfg.php')
def getConfigFile():
    #(rnd, client, version) = request.params.get('rnd'),request.params.get('client'),request.params.get('version')
    return configFile

@app.route('/lang/sfgame_en.js')
def getLanguage():
    return englishLanguage

requestDict = {'accountcheck' : accountcheck, 'getserverversion' : versioncheck, 'accountcreate' : accountcreate, 'accountlogin' : accountlogin}

@app.route('/req.php')
def handleRequest():

    cryptoId = request.query.req[:16]
    reqStr = request.query.req[16:]
    reqStr = reqStr.replace('-', '+').replace('_', '/')


    #Pads the message so we can decode it
    if len(reqStr) % 16 is not 0:
        #print('Incorrectly padded message {}'.format(len(reqStr)))
        reqStr = reqStr + '='*(((len(reqStr)%16+1) * 16) - len(reqStr))

    
    decoded = base64.b64decode(reqStr)
    middle = AES.new('[_/$VV&*Qg&)r?~g', AES.MODE_CBC, 'jXT#/vz]3]5X7Jl\\')
    data = middle.decrypt(decoded).split('|')
    sessionid, message = data[0], data[1].split(':')

    #print(message)

    return requestDict[message[0]](message[1])

@app.error(404)
def qqutro(error):
    return "Olha para tras.."

app.run(host='localhost', port=80, reloader=True, quiet=True)
