import base64
from Crypto.Cipher import AES

with open('log.txt') as f:
    lines = f.readlines()
    for line in lines:
        coise = line.split('?')[1].split('&rnd')[0][4:]
        #cryptoid = coise[:16]
        reqStr = coise[16:]
        reqStr = reqStr.replace('-', '+').replace('_', '/')



        if len(reqStr) % 16 is not 0:
            #print('Incorrectly padded message {}'.format(len(reqStr)))
            reqStr = reqStr + '='*(((len(reqStr)%16+1) * 16) - len(reqStr))

        decoded = base64.b64decode(reqStr)
        middle = AES.new('9rG0150U71T72206', AES.MODE_CBC, 'jXT#/vz]3]5X7Jl\\')
        data = middle.decrypt(decoded)

        print(data)

