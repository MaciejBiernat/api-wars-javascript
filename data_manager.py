import connection
import hashing_util



@connection.connection_handler
def check_user(cursor, register_form):
    cursor.execute("""
     SELECT username, email FROM user_reg WHERE username = '%s' OR email = '%s'
    """ % (register_form['user'], register_form['email']))

    compare_result = cursor.fetchall()
    if len(compare_result) == 0:
        add_user(register_form)
        return 'Registration successful. Please sign in to continue.'
    else:
        return False

# @connection.connection_handler
# def check_login_user_name(cursor, login_data):
#     cursor.execute("""
#      SELECT user_name FROM users WHERE user_name = '%s'
#     """ % (login_data['user_name']))
#
#     compare_result = cursor.fetchall()
#     if len(compare_result) == 0:
#         return False
#     else:
#         return True

# @connection.connection_handler
# def check_login_password(cursor, login_data):
#     cursor.execute("""
#     SELECT password FROM users WHERE user_name = '%s'
#      """ % (login_data['user_name']))
#     db_password = cursor.fetchall()
#     if len(db_password) == 0:
#         return False
#     else:
#         compare = hashing_utility.verify_password(login_data['password'],db_password[0]['password'])
#         print(compare)
#         return compare


@connection.connection_handler
def add_user(cursor, register_form):
    hashed_password = hashing_util.hash_password(register_form['password'])
    cursor.execute("""
                        INSERT INTO user_reg (password, username, email) VALUES ('%s', '%s', '%s')"""
                   % (hashed_password, register_form['user'],
                      register_form['email']))