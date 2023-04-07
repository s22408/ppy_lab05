filepath = "students.txt"
Studenci = []


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


def add(email, name, lastname, points):
    if emailtaken(email):
        print('email jest zajety, nie wstawiono studenta')
    else:
        tmp = {'email': email, 'name': name, 'lastName': lastname,
               'points': points, 'grade': '', 'status': ''}
        Studenci.append(tmp)

    save(filepath)


def delete(email):

    for x in Studenci:
        if x['email'] == email:
            Studenci.remove(x)
            save(filepath)
            return 0

    print('nie ma studenta o takim emailu, nie usunieto nikogo')

