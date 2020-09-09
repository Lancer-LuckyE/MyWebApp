from psycopg2 import errors


def create_user(db, email, password, first_name, last_name):
    if not db.is_connected():
        db.connect_db()
    sql = 'INSERT INTO "Users" VALUES (' \
          ' \'{email}\',' \
          ' \'{password}\',' \
          ' \'{last}\',' \
          ' \'{first}\',' \
          ' {deactivate},' \
          ' {created},' \
          ' {modified});'\
        .format(email=email, password=password, first=first_name, last=last_name, deactivate=False, created='now()',
                modified='null')
    try:
        db.update_table(sql)
        return 'Account is created.', True
    except Exception as e:
        # TODO: It is better to include time info in a log
        print('create user error')
        print(e)
        return 'Sorry, internal server error. Please try again later', False


def find_user(db, email):
    if not db.is_connected():
        db.connect_db()
    sql = 'SELECT * FROM "Users" WHERE "Email" = \'{email}\';'.format(email=email)
    try:
        user = db.find_one(sql)
        return user, True
    except Exception as e:
        print("find user error")
        print('e')
        return 'Sorry, internal server error. Please try again later', False


def find_users_by(db, criteria):
    return


def update_password(db, email, password):
    if not db.is_connected():
        db.connect_db()
    sql = 'UPDATE "Users" SET "Password" = \'{password}\', "Modified" = now() WHERE "Email" = \'{email}\';'\
        .format(password=password, email=email)
    try:
        db.update_table(sql)
        return 'Account password is updated.', True
    except Exception as e:
        print('update password error')
        print(e)
        return 'Sorry, internal server error. Please try again later', False


def update_name(db, first, last, email):
    if not db.is_connected():
        db.connect_db()
    sql = 'UPDATE "Users" SET "First_Name"=\'{first}\', "Last_Name" = \'{last}\', "Modified" = now() ' \
          'WHERE "Email" = \'{email}\';'.format(last=last, first=first, email=email)
    try:
        db.update_table(sql)
        return 'User name is updated.', True
    except Exception as e:
        print('update user name error')
        print(e)
        return 'Sorry, internal server error. Please try again later', False


def deactivate(db, email):
    if not db.is_connected():
        db.connect_db()
    sql = 'UPDATE "Users" SET "Deactivated" = True, "Modified" = now() WHERE "Email" = \'{email}\';'\
        .format(email=email)
    try:
        db.update_table(sql)
        return 'Account is deactivated.', True
    except Exception as e:
        print('Account deactivate error')
        print(e)
        return 'Sorry, internal server error. Please try again later', False



# class User:
#     def __init__(self, email, password, first_name='', last_name=''):
#         self._email = email
#         self.first_name = first_name
#         self.last_name = last_name
#         self._password = password

