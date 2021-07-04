import csv
from random_word import RandomWords
import random
from datetime import date
import time

def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

def clear_csv(fname):
    csv_file = open('pwds.csv','w',newline = "" )
    csv_file.close()

def add_entry(new_entry):
    hx = read_csv('pwds.csv')

    csv_file = open('pwds.csv','w',newline = "" )
    csv_writer = csv.writer(csv_file)

    for entry in hx:
        csv_writer.writerow(entry)
        
    csv_writer.writerow([date_gen(),new_entry])

    csv_file.close()

def generate():
    r = RandomWords()
    time.sleep(1)
    f1 = r.get_random_word(minLength = 3)
    f2 = r.get_random_word(minLength = 3)
    num = random.randint(100,999)

    return f1+f2+str(num)

def date_gen():
    today = date.today()
    return today.strftime("%d/%m/%Y")

def get_new_pass():
    new_pass = generate()
    add_entry('pwds.csv',new_pass)
    print("New password added")

def print_hx():
    hx = read_csv('pwds.csv')
    for row in hx:
        print(row)

def return_latest_pass():
    hx = read_csv('pwds.csv')
    return hx[-1]

def set_password(password):
    add_entry('pwds.csv',password)
    print('Password added')
    


