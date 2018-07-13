# -*- coding: utf-8 -*-
import random
import hashlib
from db_handler import QueryDb, IntegrityError

def dispatcher(name, arg):

    if name in globals():
        return globals()[name](arg)

    print('Unimplemented ' + name)
    return 'penis'

def accountcheck(name):
    res = QueryDb('SELECT * FROM players WHERE username=?', (name,))

    res = res.fetchone()
    if res is None:
        return 'success:'
    
    return 'Error:character_exists'


def getserverversion(arg):
    return 'serverversion:1509&Success:'


sexL = ['Male', 'Female']
raceL = ['Human', 'Elf', 'Dwarf', 'Gnome', 'Orc', 'Dark Elf', 'Goblin', 'Demon']
classeL = ['Warrior', 'Wizard', 'Archer', 'Assassin']

def accountcreate(details):

#print(details)
    details = details.split('/')
    if len(details) is not 10:
        print('Not enough details creating character')
        return 0

#sex 1-male 2-female
    name, password, email, sex, race, classe,face,unk5, version, lan = details
    
    sex = int(sex)
    race = int(race)
    classe = int(classe)
    logincount = random.randrange(4761)

    hashMethod = hashlib.sha1()
    hashMethod.update(password + 'ahHoj2woo1eeChiech6ohphoB7Aithoh')
    password = hashMethod.hexdigest()

    hashMethod = hashlib.sha1()
    hashMethod.update(password + str(logincount))
    password = hashMethod.hexdigest()


    try:
        res = QueryDb('''INSERT INTO players(username, password, email, sex, race, class,
        face, unk5, logincount) VALUES(?,?,?,?,?,?,?,?, ?)''',
         (name, password, email, sex, race, classe, face, unk5, logincount), True)
    except IntegrityError as e:
        reason = str(e).split('players.')[1] 
        if reason == 'username':
            return 'Error:character_exists'
        elif reason == 'email':
            return 'Error:email not available'

    
#mouth, hair, eyebrows, eyes, beard, nose, ears, extra, zero
#print('{} wants to register'.format(name))
    return 'success:'


def poll(unk):
    return 'success:'


def wheeloffortune(unk):
    return 'wheelresult(2):2/118218&Success:'


def accountlogin(details):

    details = details.split('/')
    password, logincount = details[1], int(details[2])

    res = QueryDb(''' SELECT password,logincount FROM players WHERE username=? ''', (details[0],), True)
    if len(res) == 0:
        return 'Error:player not found'

    print(res)
    db_password, db_logincount = res[0]

    if db_logincount != logincount:
        return 'login count:{}&Error:login count too low'.format(db_logincount)

    if db_password != password:
        return 'Error:wrong pass'

    return u'playerid:1&sessionid:109K48144737im271521l12G5215865m&ownplayersave.playerSave:1107215839/11496/1531343200/1288441703/-691055940/40/0/157/696969/19869780/37964/2557/6619135/41006534/194/446/318/7/1/4/7/201/6/4/10/202/0/12582920/257/11796481/1057/767/748/1057/839/2472/282/282/761/761/1007/725/708/1011/802/1643118592/35913728/0/1023410182/655418/1421/0/6/0/0/124/0/0/1908844/0/520093699/3276808/1788/0/1/5/3/355/0/0/767255/0/855638021/65594/846/0/1/4/5/202/202/202/18544420/0/687865860/1966131/916/0/1/4/5/127/127/127/1069498/0/8/5/0/0/1/3/4/356/0/0/1238596/0/7/51/806/0/1/4/5/150/150/150/2667136/0/1526726665/655415/0/0/6/0/0/158/0/0/12349880/0/10/15/0/0/1/5/4/344/0/0/970688/0/184549377/327703/242/418/1/4/5/325/0/0/978924/0/2/9/25/0/1/5/3/331/0/0/1041951/0/12/16/0/0/11/12/0/168/25/0/245053/0/12/16/0/0/11/12/0/168/25/0/75057/0/1358954504/655415/0/0/6/0/0/155/0/0/11185490/0/0/0/0/0/0/0/0/0/0/0/0/0/5/9/2488/0/5/4/1/207/151/0/402408/0/1531343182/157/157/157/5/2/4/-74/-14/-95/5/16/8/900/1200/600/0/0/0/0/0/0/0/0/0/0/0/0/10/28/0/0/2/3/4/363/0/0/2964003/0/0/0/0/0/0/0/0/0/0/0/0/0/181418/140931/50786/512900/1530000/772900/0/1531343182/65541/8/1771/0/5/2/1/212/146/0/3750248/10/4/9/1756/0/2/3/4/371/0/0/6440589/0/3/8/1265/0/1/5/3/365/0/0/3036410/1/3/8/1865/0/4/1/3/198/156/0/2974664/10/65543/9/1413/0/3/5/4/210/142/0/3552912/10/6/10/1178/0/4/5/3/352/0/0/5781023/0/1531343182/65546/6/0/0/4/2/5/186/180/0/1484190/10/65546/3/0/0/2/3/5/186/166/0/742095/1/65545/12/0/0/3/5/2/348/0/0/4469010/0/65545/2/0/0/5/3/4/356/0/0/4954385/0/8/18/0/0/2/1/3/360/0/0/5264760/0/9/6/0/0/1/3/2/371/0/0/2967952/1/6/-2/0/3/3/10871/0/0/0/0/1395906386/0/0/1/5777/242/418/0/0/0/0/0/1531343182/6000/0/91/1530277851/1530639622/0/0/1/1288524893/157/0/0/0/0/0/0/0/2/-111/0/0/4/1530274251/4/12/12/12/12/12/12/12/12/12/3/120/9/425/0/0/0/0/0/0/0/0/0/0/751516766/751516766/751516766/1/1392935581/0/1452/0/0/42/0/1397602706/550/0/0/0/4947300/5/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/1/1530273753/0/0/0/0/0/0/0/0/0/0/0/0/0/4/2/1/1523037580/0/0/0/0/0/0/0/900/300/0/0/0/0/0/0/0/0/0/0/1530316804/0/0/173519/900/300/0/0/0/0/0/0/0/0/0/0/0/-2147482433/0/185218/2104/37092/1530639922/0/0/0/0/0/0/0/&skipallow:0&success:' 
