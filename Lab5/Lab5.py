import random
import sqlite3
from sqlite3 import Error
from concurrent.futures import ThreadPoolExecutor, as_completed, wait

people_db_file = "sqlite.db"  # The name of the database file to use 
max_people = 500  # Number  of records to create 

#################### PART I ######################## 

def generate_people(count: int) -> list[tuple]:
    last_names , first_names = [], []
    last_names = readNames('LastNames.txt')
    first_names = readNames('FirstNames.txt')
    len_last_names = len(last_names)
    len_first_names = len(first_names)
    names: list[tuple] = [(i, \
                           first_names[random.randint(0, len_first_names - 1)], \
                           last_names[random.randint(0, len_last_names - 1)]) \
                            for i in range(count)]
    return names

def readNames(fname: str) -> list[str]:
    with open(fname, 'r') as filehandle:
        names = [line.strip() for line in filehandle.readlines()]
    return names

def threadGenPeople(count) -> list[str]:
    with ThreadPoolExecutor(max_workers=2) as executor:
        future_first_names = [executor.submit(readNames, 'FirstNames.txt')]
        future_last_names = [executor.submit(readNames, 'LastNames.txt')]
        # Create nested list of results
        first_names_nest = [future.result() for future in future_first_names]
        last_names_nest = [future.result() for future in future_last_names]
        # Flatten list
        first_names = [name for sublist in first_names_nest for name in sublist]
        last_names = [name for sublist in last_names_nest for name in sublist]
        # Get len of each list
        first_name_len = len(first_names)
        last_name_len = len(last_names)
        # Put into tuple with (id, firstName, lastName)
        names: list[tuple] = [(i, \
                first_names[random.randint(0, first_name_len - 1)], \
                last_names[random.randint(0, last_name_len - 1)]) \
                for i in range(count)]
    return names

################ PART II ######################

def create_people_database(db_file, count):
    conn = sqlite3.connect(db_file)
    with conn:
        sql_create_people_table = """ CREATE TABLE IF NOT EXISTS people ( 
            id integer PRIMARY KEY, 
            first_name text NOT NULL, 
            last_name text NOT NULL); """ 
        cursor = conn.cursor() 
        cursor.execute(sql_create_people_table) 

        sql_truncate_people = "DELETE FROM people;" 
        cursor.execute(sql_truncate_people) 

        # people = generate_people(count) 
        people = threadGenPeople(count)
        
        sql_insert_person = "INSERT INTO people(id,first_name,last_name) VALUES(?,?,?);" 
        for person in people: 
            # print(person) # uncomment if you want to see the person object 
            cursor.execute(sql_insert_person, person) 
            # print(cursor.lastrowid) # uncomment if you want to see the row id  \
        cursor.close() 

#################### Part III ######################################

class PersonDB():
    def __init__(self, db_file=''):
        self.db_file = db_file

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.close()

    def load_person(self, id): 
        sql = "SELECT * FROM people WHERE id=?"
        cursor = self.conn.cursor()
        cursor.execute(sql, (id,))
        records = cursor.fetchall()
        result = (-1, '', '') # id = -1, first_name = '', last_name = ''
        if records is not None and len(records) > 0:
            result = records[0]
        cursor.close()
        return result
    
def test_PersonDB():
    with PersonDB(people_db_file) as db:
        print(db.load_person(10000))
        print(db.load_person(122))
        print(db.load_person(300))

###################### PART IV ##############################
def load_person(id, db_file):
    '''Helper method for threading db access (pt 4 of lab5)'''
    with PersonDB(db_file) as db:
        return db.load_person(id)
    
def tpe_load_list():
    worker_count = 10
    people = []
    with ThreadPoolExecutor(max_workers = worker_count) as executor:
        futures = [executor.submit(load_person, x, people_db_file) for x in range(max_people)]
        for future in as_completed(futures):
            people.append(future.result())
        # print(people)
    return people

# ---------------------------------------------------------------

if __name__ == '__main__':
    # PART I
    # peeps = generate_people(5)
    print("PART I \n")
    peeps = threadGenPeople(5)
    print(peeps)

    # PART II
    print("\n PART II\n")
    create_people_database(people_db_file, max_people) 

    # PART III
    print("\n PART III\n")
    test_PersonDB()
    
    # PART IV
    print("\n PART IV\n")
    names = tpe_load_list()
    sort_names = sorted(names, key=lambda x: (x[2], x[1] ))
    print(sort_names)