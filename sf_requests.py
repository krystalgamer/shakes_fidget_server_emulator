import hashlib
from db_handler import QueryDb

def dispatcher(name, arg):

    if name in globals():
        return globals()[name](arg)

    return 'penis'

def accountcheck(name):
    res = QueryDb('SELECT * FROM players WHERE username=?', (name,))
    return 'success:'

def versioncheck(arg):
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

    print('{} {} {} {}'.format(sexL[sex-1], raceL[race-1], classeL[classe-1], face))
    
#mouth, hair, eyebrows, eyes, beard, nose, ears, extra, zero
#print('{} wants to register'.format(name))
    return 'success:'

def accountlogin(details):

    details = details.split('/')
    password, loginCount = details[1], details[2]

    print(password)
    
    return 'skipallow:0&timestamp:1530644858&playerid:81713&tracking.s:signup&success:'
