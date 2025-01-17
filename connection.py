
import os
import psycopg2
import psycopg2.extras
import urllib


# def get_connection():
#     urllib.parse.uses_netloc.append('postgres')
#     url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
#     connection = psycopg2.connect(
#         database=url.path[1:],
#         user=url.username,
#         password=url.password,
#         host=url.hostname,
#         port=url.port
#     )
#     if connection:
#         return connection
#
#     else:
#         raise KeyError('Some necessary environment variable(s) are not defined')


# def open_database():
#     try:
#         connection = get_connection()
#         connection.autocommit = True
#     except psycopg2.DatabaseError as exception:
#         print('Database connection problem')
#         raise exception
#     return connection
#
#
# def connection_handler(function):
#     def wrapper(*args, **kwargs):
#         connection = open_database()
#         dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
#         ret_value = function(dict_cur, *args, **kwargs)
#         dict_cur.close()
#         connection.close()
#         return ret_value
#
#     return wrapper

# def get_connection_string():
#     urllib.parse.uses_netloc.append('postgres')
#     url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
#     connection = psycopg2.connect(
#         database=url.path[1:],
#         user=url.username,
#         password=url.password,
#         host=url.hostname,
#         port=url.port
#     )
#     if connection:
#         return connection
#     else:
#         raise KeyError('Some necessary environment variable(s) are not defined')
#
def get_connection_string():
    # setup connection string
    # to do this, please define these environment variables first
    user_name = os.environ.get('PSQL_USER_NAME')
    password = os.environ.get('PSQL_PASSWORD')
    host = os.environ.get('PSQL_HOST')
    database_name = os.environ.get('PSQL_DB_NAME')

    env_variables_defined = user_name and password and host and database_name

    if env_variables_defined:
        # this string describes all info for psycopg2 to connect to the database
        return 'postgresql://{user_name}:{password}@{host}/{database_name}'.format(
            user_name=user_name,
            password=password,
            host=host,
            database_name=database_name
        )
    else:
        raise KeyError('Some necessary environment variable(s) are not defined')


def open_database():
    try:
        connection_string = get_connection_string()
        connection = psycopg2.connect(connection_string)
        connection.autocommit = True
    except psycopg2.DatabaseError as exception:
        print('Database connection problem')
        raise exception
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        # we set the cursor_factory parameter to return with a RealDictCursor cursor (cursor which provide dictionaries)
        dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        ret_value = function(dict_cur, *args, **kwargs)
        dict_cur.close()
        connection.close()
        return ret_value

    return wrapper




