import sqlite3

def CreateDatabase(name):
    """
    Creates a new database if it does not excist. Returns a connection.
    """
    if '.db' in name:
        return sqlite3.connect(name)
    else:
        return sqlite3.connect(name+'.db')
def CreateTable(connection,tableName,dict):
    """
    Creates a new table in the database provided. Everything can be NULL. Requires a dictionary. Returns table name.
    """
    command = f"CREATE TABLE IF NOT EXISTS {tableName} (id INTEGER PRIMARY KEY, "
    p1 = ""
    for key,value in dict.items():
        if " " not in value:
            value = list(value)
            value.insert(0," ")
            value = "".join(value)
        if " " not in key:
            key = list(key)
            key.insert(0," ")
            key = "".join(key)

        p1 += key + value +','

    p1 = p1[:-1]
    command += p1
    command += ");"
    print ("Executing command -> ",command)
    cursor = connection.cursor()
    try:
        cursor.execute(command)
        connection.commit()
        return tableName
    except Exception as e:
        print(e)
def InsertIntoTable(connection,tableName,dict):
    """
    Inserts a single row into a table. Requires a dictionary. Returns True if successfull.
    """
    command = f"INSERT INTO {tableName}(id, "
    p1 = ""
    p2 = "(NULL,"
    variables = []
    for key,value in dict.items():
        p1 += key + ','
        p2 += '?' + ','
        variables.append(value)
    p1 = p1[:-1]
    p2 = p2[:-1]
    p1 += ') VALUES '
    p2 += ')'
    command += p1 + p2 +';'
    cursor = connection.cursor()

    print("Executing command -> ",command)

    try:
        cursor.execute(command,variables)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
def UpdateWhereId(connection,tableName,id,dict):
    """
    Updates variables where id.
    """    
    command = f"UPDATE {tableName} SET "
    p1 = ""
    variables = []
    for key, value in dict.items():
        p1 += key + '=' + '? ' + ','
        variables.append(value)
    p1=p1[:-1]
    command += p1  + "WHERE id = " + str(id)

    print("Executing command -> ",command)

    cursor = connection.cursor()
    try:
        cursor.execute(command,variables)
        connection.commit()
    except Exception as e:
        print(e)


def SearchById(connection,tableName,id):
    """
    Returns * from that id. If nothing found returns an empty list.
    """
    command = f"SELECT * FROM {tableName} WHERE id={id}"
    cursor = connection.cursor()
    print("Executing command -> ",command)
    try:
        cursor.execute(command)
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return []


# SEARCH FOR VALUE WHERE KEY = VALUE {key:value}



if __name__ == "__main__":
    print("Luka Igrutinovic is cool!")

#         ^Just an easter egg^
