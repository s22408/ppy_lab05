import smtplib
from email.mime.text import MIMEText

filepath = "students.txt"
Studenci = []
flag = True

def load(path):
    lines = []

    with open(path) as file_obj:
        for line in file_obj:
            tmp = line.replace('\n', '')
            lines.append(tmp)

    for x in lines:
        linelist = x.split(',')
        if len(linelist) == 4:
            tmpstudent = {'email': linelist[0], 'name': linelist[1], 'lastName': linelist[2],
                          'points': linelist[3], 'grade': '', 'status': ''}
        else:
            tmpstudent = {'email': linelist[0], 'name': linelist[1], 'lastName': linelist[2],
                          'points': linelist[3], 'grade': linelist[4], 'status': linelist[5]}

        Studenci.append(tmpstudent)


def save(path):
    with open(path, "w") as file_object:
        for x in Studenci:
            line = x['email'] + ',' + x['name'] + ',' + x['lastName'] + ',' + x['points'] + ',' + x['grade'] + ',' + x[
                'status'] + '\n'
            file_object.write(line)


def autograde():
    for x in Studenci:

        if x['grade'] == '':
            if int(x['points']) >= 91:
                x['grade'] = '5'
            elif int(x['points']) >= 81:
                x['grade'] = '4.5'
            elif int(x['points']) >= 71:
                x['grade'] = '4'
            elif int(x['points']) >= 61:
                x['grade'] = '3.5'
            elif int(x['points']) >= 51:
                x['grade'] = '3'
            else:
                x['grade'] = '2'

            x['status'] = 'GRADED'

    save(filepath)


def emailtaken(email):
    for x in Studenci:
        if x['email'] == email:
            return True
    return False


def add():

    arg = input('dodajesz studenta! Podaj po przecinku kolejno email,imie,nazwisko,punkty\n').split(',')

    email = arg[0]
    name = arg[1]
    lastname = arg[2]
    points = arg[3]

    if emailtaken(email):
        print('email jest zajety, nie wstawiono studenta')
    else:
        tmp = {'email': email, 'name': name, 'lastName': lastname,
               'points': points, 'grade': '', 'status': ''}
        Studenci.append(tmp)
        print("dodano studenta o emialu : "+email+" !!! ")

    save(filepath)


def delete():

    arg = input("usuwasz studenta!!! podaj email/emaile studentów do usuniecia oddzielajac je przecinkiem\n").split(',')

    for x in arg:
        for y in Studenci:
            if y['email'] == x:

                Studenci.remove(y)
                print('usunieto dane studenta z emailem: '+x)
                save(filepath)
                continue
            print('??? ' + x + ' ??? nie ma studenta o takim emailu, nie mozna go usunac !!!')

    save(filepath)
    print('zapisano zaktualizowane dane w pliku')


def sendemails():

    autograde()

    for x in Studenci:
        if x['status'] != 'MAILED':

            email = x['email']
            name = x['name']
            lastname = x['lastName']
            points = x['points']
            grade = x['grade']

            body = "Uzyskano :"+points+" punktow z przedmiotu PPY, wystawiono ocenę "+grade

            msg = MIMEText(body)
            msg['Subject'] = "ocena z przedmiotu PPY "+name+" "+lastname
            msg['From'] = "ppys22408@gmail.com"
            msg['To'] = email
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.login("ppys22408@gmail.com", "hpspmwynvusifgiz")
            smtp_server.sendmail("ppys22408@gmail.com", email, msg.as_string())
            smtp_server.quit()

            x['status'] = 'MAILED'
            print("wysłano maila do: "+email)

    save(filepath)


def switch(n):
    if n == '1':
        sendemails()
    if n == '2':
        add()
    if n == '3':
        delete()
    if n == '4':
        autograde()
    if n == '0':
        return 0


print("wpisz:")
print("'1' - wysłanie maila o wystawionej ocenie studentom o statusie innym niż 'MAILED'")
print("# wystawia również automatycznie oceny studentom bez oceny")
print("'2' - dodawanie studenta")
print("'3' - usuwanie sudenta")
print("'4' - wystawienie ocen wszystkim studentom bez oceny")
print("'0' - zakonczenie programu")


while flag:
     if switch(input()) == 0:
         break

print('KONIEC')

