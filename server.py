import base64
from Crypto.Cipher import AES
from db_handler import StartDb, CloseDb
from bottle import Bottle, request
from sf_requests import dispatcher
from keys import configFile, englishLanguage

app = Bottle()

''' cursor.execute('CREATE TABLE players(id PRIMARY_KEY INT, username TEXT,
password TEXT, email TEXT, sex INT, race INT, class INT, face TEXT, unk5 INT)')
'''


# /sfgame_cfg.php?rnd=0.4670932721346617&client=windows%202.81.31&version=885116b401e56d21a6e99c7a2838cbf7
@app.route('/sfgame_cfg.php')
def getConfigFile():
    return configFile


@app.route('/lang/sfgame_en.js')
def getLanguage():
    return englishLanguage


@app.route('/req.php')
def handleRequest():

    cryptoId = request.query.req[:16]
    reqStr = request.query.req[16:]
    reqStr = reqStr.replace('-', '+').replace('_', '/')

    if cryptoId != '0-00000000000000':
        return 'Error:cryptoid_not_found'

# Pads the message so we can decode it
    if len(reqStr) % 16 is not 0:
        reqStr = reqStr + '='*(((len(reqStr) % 16+1) * 16) - len(reqStr))

    decoded = base64.b64decode(reqStr)
    middle = AES.new('[_/$VV&*Qg&)r?~g', AES.MODE_CBC, 'jXT#/vz]3]5X7Jl\\')
    data = middle.decrypt(decoded).split('|')
    try:
        sessionid, message = data[0], data[1].split(':')
    except IndexError:
        print('Non default encryption detected ' + sessionid)
        return 'Error:cryptoid_not_found'

    return dispatcher(message[0], message[1])


@app.error(404)
def qqutro(error):
    return "Olha para tras.."


if __name__ == '__main__':
    StartDb()
    app.run(host='localhost', port=80, reloader=True, quiet=False)
    CloseDb()
