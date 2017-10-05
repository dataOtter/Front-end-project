import constants as c
import mysql.connector


def add_key_value_to_db(key_value: list):
    execute_query_insert_one_row(key_value)


def get_all_data_from_db():
    statement = "SELECT * FROM " + c.TBL_NAME
    result_list_of_strs = execute_query_return_list(statement)
    return result_list_of_strs


def execute_query(statement: str):
    cnx = mysql.connector.connect(user=c.USER_NAME, password=c.PASSWORD, host=c.HOST_IP, database=c.DB_NAME)
    cursor = cnx.cursor()
    cursor.execute(statement)
    cnx.commit()
    cursor.close()
    cnx.close()


def get_insert_row_statement(table_name=c.TBL_NAME, col_labels=c.COL_LABELS):
    labels, values = '(', '('
    for label in col_labels:
        labels += "`" + label + "`" + ","
        values += "%s,"
    labels = labels[:-1] + ")"
    values = values[:-1] + ")"
    return "INSERT INTO " + table_name + " " + labels + " VALUES " + values


def execute_query_insert_one_row(row: list):
    insert_row_statement = get_insert_row_statement()
    cnx = mysql.connector.connect(user=c.USER_NAME, password=c.PASSWORD, host=c.HOST_IP, database=c.DB_NAME)
    cursor = cnx.cursor()
    cursor.execute(insert_row_statement, row)
    cnx.commit()
    cursor.close()
    cnx.close()


def execute_query_return_list(statement: str):
    cnx = mysql.connector.connect(user=c.USER_NAME, password=c.PASSWORD, host=c.HOST_IP, database=c.DB_NAME)
    cursor = cnx.cursor()
    cursor.execute(statement)
    results_list_of_tuples = cursor.fetchall()
    cnx.commit()
    cursor.close()
    cnx.close()
    return results_list_of_tuples
