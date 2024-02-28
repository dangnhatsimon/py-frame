from tkinter import *
from PIL import Image, ImageTk
import sqlite3

root = Tk()
root.title("Simple Search")
root.iconbitmap('D:/Python/TKinter/search_book_open_search_locate_6178.ico')
root.geometry("400x400")

conn = sqlite3.connect('address_book.db')

cursor = conn.cursor()

# create_query = """ CREATE TABLE addresses (
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
# )

# """
# cursor.execute(create_query)

# conn.commit()

# conn.close()


def submit():
    conn = sqlite3.connect('address_book.db')

    cursor = conn.cursor()

    insert_query = """ INSERT INTO addresses 
    VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)
    """
    cursor.execute(
        insert_query,
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        }
    )

    conn.commit()

    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    conn = sqlite3.connect('address_book.db')

    cursor = conn.cursor()

    retrieve_query = """SELECT *
    FROM addresses
    """
    records = cursor.fetchall()

    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)
    conn.commit()

    conn.close()


def delete():
    conn = sqlite3.connect('address_book.db')

    cursor = conn.cursor()

    delete_query = """DELETE FROM addresses
    WHERE oid = 
    """ + select_box.get()

    cursor.execute(delete_query)

    select_box.delete(0, END)

    conn.commit()

    conn.close()


def update():
    conn = sqlite3.connect('address_book.db')

    cursor = conn.cursor()

    record_id = select_box.get()
    
    update_query = """UPDATE addresses
    SET
    first_name = :first,
    last_name = :last,
    address = :address,
    city = :city,
    state = :state,
    zipcode = :zipcode
    WHERE oid = :oid
    """
    cursor.execute(
        update_query,
        {
            'first': f_name_editor.get(),
            'last': l_name_editor.get(),
            'address': address_editor.get(),
            'city': city_editor.get(),
            'state': state_editor.get(),
            'zipcode': zipcode_editor.get(),
            'oid': record_id
        }
    )

    conn.commit()

    conn.close()
    
    editor.destroy()


def edit():
    global editor
    editor = Tk()
    editor.title("Update a record")
    editor.iconbitmap(
        'D:/Python/TKinter/search_book_open_search_locate_6178.ico')
    editor.geometry("400x600")

    conn = sqlite3.connect('address_book.db')

    cursor = conn.cursor()

    record_id = select_box.get()
    edit_query = """ SELECT *
    FROM addresses
    WHERE oid = 
    """ + record_id
    cursor.execute(edit_query)
    records = cursor.fetchall()

    conn.commit()

    conn.close()

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=0, padx=20)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))

    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)

    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)

    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)

    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)

    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    save_button = Button(
        editor, text="Save record from Database", command=update)
    save_button.grid(row=6, column=0, columnspan=2,
                     padx=10, pady=10, ipadx=145)


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=0, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

select_box = Entry(root, width=30)
select_box.grid(row=9, column=1, pady=5)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

select_box_label = Label(root, text="Select ID")
select_box_label.grid(row=10, column=1, pady=5)


query_button = Button(root, text="Show", command=query)
query_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

submit_button = Button(root, text="Add", command=submit)
submit_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

delete_button = Button(root, text="Delete", command=delete)
delete_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=135)

edit_button = Button(root, text="Edit", command=edit)
edit_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=145)

conn.commit()

conn.close()

root.mainloop()
