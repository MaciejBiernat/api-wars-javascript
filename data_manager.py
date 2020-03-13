import connection
import hashing_util



@connection.connection_handler
def check_user(cursor, form_data):
    cursor.execute("""
     SELECT username, email FROM user_reg WHERE username = '%s' OR email = '%s'
    """ % (form_data['user'], form_data['email']))

    compare_result = cursor.fetchall()
    if len(compare_result) == 0:
        return True
    else:
        return False



@connection.connection_handler
def check_login_password(cursor, login_data):
    cursor.execute("""
    SELECT password FROM user_reg WHERE username = '%s' OR email = '%s'
     """ % (login_data['user'], login_data['email']))
    db_password = cursor.fetchall()
    if len(db_password) == 0:
        return False
    else:
        compare = hashing_util.verify_password(login_data['password'],db_password[0]['password'])
        print(compare)
        return compare


@connection.connection_handler
def add_user(cursor, register_form):
    hashed_password = hashing_util.hash_password(register_form['password'])
    cursor.execute("""
                        INSERT INTO user_reg (password, username, email) VALUES ('%s', '%s', '%s')"""
                   % (hashed_password, register_form['user'],
                      register_form['email']))