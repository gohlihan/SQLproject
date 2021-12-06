import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

from DbFunction import show_the_best_worker

#-----------Tkinter Setup---------------------------
root = tk.Tk()
root.title("AAA Company")

window_width = 1000
window_height = 600

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# add some style
style = ttk.Style()

# pick a Theme
style.theme_use('default')

# configure the treeview color
style.configure('Treeview',
    background='#D3D3D3',
    foreground='black',
    rowheight=25,
    fieldbackground='#D3D3D3')

# change selected color
style.map('Treeview',
    background=[('selected',"#347083")])

# create a treeview frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# create a treeview scroolbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# create the treeview
my_tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set, selectmode='extended')
my_tree.pack()

# configure the scroolbar
tree_scroll.config(command=my_tree.yview)

########################## Functions ###################################

# Remove all records
def remove_all():
	for record in my_tree.get_children():
		my_tree.delete(record)

# View all invoices
def View_invoice():
    remove_all()
    # Unpack 
    data_frame_warehouse.pack_forget()
    warehouse_modify_button_frame.pack_forget()
    agent_button_frame.pack_forget()
    worker_button_frame.pack_forget()
    customer_button_frame.pack_forget()
    driver_button_frame.pack_forget()
    # Pack
    data_frame_inv.pack(fill="x", expand="yes", padx=20)
    inv_modify_button_frame.pack(fill="x", expand="yes", padx=20)



    # Define Columns
    my_tree['columns'] = ("Invoice Id", "Invoice Date","Worker Id","Customer Id","Shopping List Id","Total Price","City Id","Deliver Id","Shipping Status")

    # Format Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Invoice Id", anchor=W, width=100)
    my_tree.column("Invoice Date", anchor=W, width=100)
    my_tree.column("Worker Id", anchor=W, width=100)
    my_tree.column("Customer Id", anchor=W, width=100)
    my_tree.column("Shopping List Id", anchor=W, width=100)
    my_tree.column("Total Price", anchor=W, width=100)
    my_tree.column("City Id", anchor=W, width=100)
    my_tree.column("Deliver Id", anchor=W, width=100)
    my_tree.column("Shipping Status", anchor=W, width=100)

    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Invoice Id", text="Invoice Id",anchor=W)
    my_tree.heading("Invoice Date",text="Invoice Date", anchor=W)
    my_tree.heading("Worker Id", text="Worker Id",anchor=W)
    my_tree.heading("Customer Id",text="Customer Id", anchor=W)
    my_tree.heading("Shopping List Id", text="Shopping List Id",anchor=W)
    my_tree.heading("Total Price", text="Total Price",anchor=W)
    my_tree.heading("City Id", text="City Id",anchor=W)
    my_tree.heading("Deliver Id",text="Deliver Id", anchor=W)
    my_tree.heading("Shipping Status", text="Shipping Status",anchor=W)


    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT *
    FROM Invoices
    '''
    c.execute(sql)
    item = c.fetchall()
    for invoice_row in item:
        #print(row) # it print all records in the database
        my_tree.insert("", tk.END, values=(invoice_row[0],invoice_row[1],invoice_row[2],invoice_row[3],invoice_row[4],invoice_row[5],invoice_row[6],invoice_row[7],invoice_row[8]))
    conn.commit()
    conn.close()

# view all warehouse's stock
def View_warehouse():
    remove_all()
    # Unpack other element
    data_frame_inv.pack_forget()
    inv_modify_button_frame.pack_forget()
    agent_button_frame.pack_forget()
    worker_button_frame.pack_forget()
    customer_button_frame.pack_forget()
    driver_button_frame.pack_forget()

    # Pack Self element
    data_frame_warehouse.pack(fill="x", expand="yes", padx=20)
    warehouse_modify_button_frame.pack(fill="x", expand="yes", padx=20)



    # Define Columns
    my_tree['columns'] = ("Stock List Id","Warehouse Id", "City Id","Agent Id","Item Id","Item Name","Quantity")

    # Format Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Stock List Id", anchor=W, width=100)
    my_tree.column("Warehouse Id", anchor=W, width=100)
    my_tree.column("City Id", anchor=W, width=100)
    my_tree.column("Agent Id", anchor=W, width=100)
    my_tree.column("Item Id", anchor=W, width=100)
    my_tree.column("Item Name", anchor=W, width=100)
    my_tree.column("Quantity", anchor=W, width=100)


    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Stock List Id", text="Stock List Id",anchor=W)
    my_tree.heading("Warehouse Id", text="Warehouse Id",anchor=W)
    my_tree.heading("City Id",text="City Id", anchor=W)
    my_tree.heading("Agent Id", text="Agent Id",anchor=W)
    my_tree.heading("Item Id",text="Item Id", anchor=W)
    my_tree.heading("Item Name", text="Item Name",anchor=W)
    my_tree.heading("Quantity", text="Quantity",anchor=W)


    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT *
    FROM Warehouses
    ORDER BY warehouse_id
    '''
    c.execute(sql)
    item = c.fetchall()
    for row in item:
        #print(row) # it print all records in the database
        my_tree.insert("", tk.END, values=row)
    conn.commit()
    conn.close()

# view all agents
def View_agent():
    remove_all()
    # Unpack other element
    data_frame_inv.pack_forget()
    inv_modify_button_frame.pack_forget()
    data_frame_warehouse.pack_forget()
    warehouse_modify_button_frame.pack_forget()
    worker_button_frame.pack_forget()
    customer_button_frame.pack_forget()
    driver_button_frame.pack_forget()

    # Pack Self element
    agent_button_frame.pack(fill="x", expand="yes", padx=20)



    # Define Columns
    my_tree['columns'] = ("Agent Id","Agent Name", "City Id")

    # Format Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Agent Id", anchor=W, width=200)
    my_tree.column("Agent Name", anchor=W, width=200)
    my_tree.column("City Id", anchor=W, width=200)



    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Agent Id", text="Agent Id",anchor=W)
    my_tree.heading("Agent Name",text="Agent Name", anchor=W)
    my_tree.heading("City Id",text="City Id", anchor=W)



    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT *
    FROM Agents
    '''
    c.execute(sql)
    item = c.fetchall()
    for row in item:
        #print(row) # it print all records in the database
        my_tree.insert("", tk.END, values=row)
    conn.commit()
    conn.close()
def show_the_best_agent():
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT agent_id,agent_name,MAX(totalsale)
    FROM (SELECT a.agent_id, a.agent_name, SUM(i.total_price) AS totalsale
    FROM Workers w, Invoices i, Agents a, Managers m
    WHERE i.worker_id = w.worker_id AND w.manager_id = m.manager_id AND m.agent_id = a.agent_id
    GROUP BY a.agent_id, a.agent_name)
    '''
    c.execute(sql)
    the_best_agent = c.fetchall()
    b_label = Label(agent_button_frame, text="The Best Agent Is: \n\n"+str(the_best_agent))
    b_label.grid(row=0, column=0, padx=10, pady=10)
    conn.commit()
    conn.close()
def show_the_worst_agent():
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT agent_id,agent_name,MIN(totalsale)
    FROM (SELECT a.agent_id, a.agent_name, SUM(i.total_price) AS totalsale
    FROM Workers w, Invoices i, Agents a, Managers m
    WHERE i.worker_id = w.worker_id AND w.manager_id = m.manager_id AND m.agent_id = a.agent_id
    GROUP BY a.agent_id, a.agent_name)
    '''
    c.execute(sql)
    the_worst_agent = c.fetchall()
    w_label = Label(agent_button_frame, text="The Worst Agent Is: \n\n"+str(the_worst_agent))
    w_label.grid(row=0, column=1, padx=10, pady=10)
    conn.commit()
    conn.close()

# view all workers
def View_worker():
    remove_all()
    # Unpack other element
    data_frame_inv.pack_forget()
    inv_modify_button_frame.pack_forget()
    data_frame_warehouse.pack_forget()
    warehouse_modify_button_frame.pack_forget()
    agent_button_frame.pack_forget()
    customer_button_frame.pack_forget()
    driver_button_frame.pack_forget()

    # Pack Self element
    worker_button_frame.pack(fill="x", expand="yes", padx=20)

    # Define Columns
    my_tree['columns'] = ("Worker Id","Worker Name", "Manager Id")

    # Format Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Worker Id", anchor=W, width=200)
    my_tree.column("Worker Name", anchor=W, width=200)
    my_tree.column("Manager Id", anchor=W, width=200)

    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Worker Id", text="Worker Id",anchor=W)
    my_tree.heading("Worker Name",text="Worker Name", anchor=W)
    my_tree.heading("Manager Id",text="Manager Id", anchor=W)

    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT *
    FROM Workers
    '''
    c.execute(sql)
    item = c.fetchall()
    for row in item:
        #print(row) # it print all records in the database
        my_tree.insert("", tk.END, values=row)
    conn.commit()
    conn.close()
def show_the_best_worker():
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT worker_id,worker_name,MAX(totalsale)
    FROM (SELECT w.worker_id, w.worker_name, SUM(i.total_price) AS totalsale
    FROM Workers w, Invoices i
    WHERE i.worker_id = w.worker_id
    GROUP BY w.worker_id, w.worker_name)
    '''
    c.execute(sql)
    the_best_worker = c.fetchall()
    bw_label = Label(worker_button_frame, text="The Best Worker Is: \n\n"+str(the_best_worker))
    bw_label.grid(row=0, column=0, padx=10, pady=10)
    conn.commit()
    conn.close()
def show_the_worst_worker():
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT worker_id,worker_name,MIN(totalsale)
    FROM (SELECT w.worker_id, w.worker_name, SUM(i.total_price) AS totalsale
    FROM Workers w, Invoices i
    WHERE i.worker_id = w.worker_id
    GROUP BY w.worker_id, w.worker_name)
    '''
    c.execute(sql)
    the_worst_worker = c.fetchall()
    w_label = Label(worker_button_frame, text="The Worst Worker Is: \n\n"+str(the_worst_worker))
    w_label.grid(row=0, column=1, padx=10, pady=10)
    conn.commit()
    conn.close()

# view all customers
def View_customer():
    remove_all()
    # Unpack other element
    data_frame_inv.pack_forget()
    inv_modify_button_frame.pack_forget()
    data_frame_warehouse.pack_forget()
    warehouse_modify_button_frame.pack_forget()
    agent_button_frame.pack_forget()
    worker_button_frame.pack_forget()
    driver_button_frame.pack_forget()

    # Pack Self element
    customer_button_frame.pack(fill="x", expand="yes", padx=20)

    # Define Columns
    my_tree['columns'] = ("Customer Id","Customer Name", "City Id", "Invoice Id")

    # Format Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Customer Id", anchor=W, width=200)
    my_tree.column("Customer Name", anchor=W, width=200)
    my_tree.column("City Id", anchor=W, width=200)
    my_tree.column("Invoice Id", anchor=W, width=200)

    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Customer Id", text="Customer Id",anchor=W)
    my_tree.heading("Customer Name",text="Customer Name", anchor=W)
    my_tree.heading("City Id",text="City Id", anchor=W)
    my_tree.heading("Invoice Id",text="Invoice Id", anchor=W)

    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT *
    FROM Customers
    '''
    c.execute(sql)
    item = c.fetchall()
    for row in item:
        #print(row) # it print all records in the database
        my_tree.insert("", tk.END, values=row)
    conn.commit()
    conn.close()
def show_newphone_customer(): 
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT id, name, MAX(Sum)
    FROM 
    (SELECT Customers.customer_id AS id, Customers.customer_name AS name, SUM(item_quantity) AS Sum
    FROM Customers, Invoices, Shopping_lists
    WHERE Customers.customer_id = Invoices.customer_id 
    AND Invoices.shopping_list_id = Shopping_lists.shopping_list_id 
    AND Shopping_lists.item_id = 1
    GROUP BY Customers.customer_id)
    '''
    c.execute(sql)
    top_newphone_buyer= c.fetchall()
    top_label = Label(customer_button_frame, text="Top New Phone Buyer Is: \n\n"+str(top_newphone_buyer))
    top_label.grid(row=0, column=0, padx=10, pady=10)
    conn.commit()
    conn.close()
def show_oldphone_customer(): 
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT id, name, MAX(Sum)
    FROM 
    (SELECT Customers.customer_id AS id, Customers.customer_name AS name, SUM(item_quantity) AS Sum
    FROM Customers, Invoices, Shopping_lists
    WHERE Customers.customer_id = Invoices.customer_id 
    AND Invoices.shopping_list_id = Shopping_lists.shopping_list_id 
    AND Shopping_lists.item_id = 2
    GROUP BY Customers.customer_id)
    '''
    c.execute(sql)
    top_oldphone_buyer= c.fetchall()
    top_label = Label(customer_button_frame, text="Top Old Phone Buyer Is: \n\n"+str(top_oldphone_buyer))
    top_label.grid(row=0, column=1, padx=10, pady=10)
    conn.commit()
    conn.close()


# view all drivers
def View_driver():
    remove_all()
    # Unpack other element
    data_frame_inv.pack_forget()
    inv_modify_button_frame.pack_forget()
    data_frame_warehouse.pack_forget()
    warehouse_modify_button_frame.pack_forget()
    agent_button_frame.pack_forget()
    worker_button_frame.pack_forget()
    customer_button_frame.pack_forget()

    # Pack Self element
    driver_button_frame.pack(fill="x", expand="yes", padx=20)

    # Define Columns
    my_tree['columns'] = ("Driver Id","Driver Name", "City Id")

    # Format Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Driver Id", anchor=W, width=200)
    my_tree.column("Driver Name", anchor=W, width=200)
    my_tree.column("City Id", anchor=W, width=200)

    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Driver Id", text="Driver Id",anchor=W)
    my_tree.heading("Driver Name",text="Driver Name", anchor=W)
    my_tree.heading("City Id",text="City Id", anchor=W)


    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT *
    FROM Drivers
    '''
    c.execute(sql)
    item = c.fetchall()
    for row in item:
        #print(row) # it print all records in the database
        my_tree.insert("", tk.END, values=row)
    conn.commit()
    conn.close()
def show_active_driver():
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT driver_id, driver_name, MAX(count)
    FROM (SELECT d.driver_id, d.driver_name, COUNT(i.city_id) AS count
    FROM Drivers d, Invoices i
    WHERE d.driver_id = i.driver_id
    GROUP BY d.driver_id, d.driver_name)
    '''
    c.execute(sql)
    top_driver = c.fetchall()
    top_label = Label(driver_button_frame, text="The Most Active Driver Is: \n\n"+str(top_driver))
    top_label.grid(row=0, column=0, padx=10, pady=10)
    conn.commit()
    conn.close()
def show_nonactive_driver():
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT driver_id, driver_name, MIN(count)
    FROM (SELECT d.driver_id, d.driver_name, COUNT(i.city_id) AS count
    FROM Drivers d, Invoices i
    WHERE d.driver_id = i.driver_id
    GROUP BY d.driver_id, d.driver_name)
    '''
    c.execute(sql)
    nontop_driver = c.fetchall()
    top_label = Label(driver_button_frame, text="The Non Active Driver Is: \n\n"+str(nontop_driver))
    top_label.grid(row=0, column=1, padx=10, pady=10)
    conn.commit()
    conn.close()


############################ Commands Buttons ####################################

# Buttons Frame
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

# Add Buttons
show_invoice_button = Button(button_frame, text="View Invoices", command=View_invoice)
show_invoice_button.grid(row=0, column=0, padx=10, pady=10)

show_warehouse_button = Button(button_frame, text="View Warehouse Stocks", command=View_warehouse)
show_warehouse_button.grid(row=0, column=1, padx=10, pady=10)

show_agent_button = Button(button_frame, text="View Agents", command=View_agent)
show_agent_button.grid(row=0, column=2, padx=10, pady=10)

show_worker_button = Button(button_frame, text="View Workers", command=View_worker)
show_worker_button.grid(row=0, column=3, padx=10, pady=10)

show_customer_button = Button(button_frame, text="View Customers", command=View_customer)
show_customer_button.grid(row=0, column=4, padx=10, pady=10)

show_driver_button = Button(button_frame, text="View Drivers", command=View_driver)
show_driver_button.grid(row=0, column=5, padx=10, pady=10)

############################# Invoice Input Data Frame #############################

# Add Record Entry Boxes
data_frame_inv = LabelFrame(root, text="Record")
#data_frame_inv.pack(fill="x", expand="yes", padx=20)

inv_id_label = Label(data_frame_inv, text="Invoice Id")
inv_id_label.grid(row=0, column=0, padx=10, pady=10)
inv_id_entry = Entry(data_frame_inv)
inv_id_entry.grid(row=0, column=1, padx=10, pady=10)

inv_date_label = Label(data_frame_inv, text="Invoice Date")
inv_date_label.grid(row=0, column=2, padx=10, pady=10)
inv_date_entry = Entry(data_frame_inv)
inv_date_entry.grid(row=0, column=3, padx=10, pady=10)

inv_workerid_label = Label(data_frame_inv, text="Worker Id")
inv_workerid_label.grid(row=0, column=4, padx=10, pady=10)
inv_workerid_entry = Entry(data_frame_inv)
inv_workerid_entry.grid(row=0, column=5, padx=10, pady=10)

inv_customerid_label = Label(data_frame_inv, text="Customer Id")
inv_customerid_label.grid(row=0, column=6, padx=10, pady=10)
inv_customerid_entry = Entry(data_frame_inv)
inv_customerid_entry.grid(row=0, column=7, padx=10, pady=10)

inv_shoplistid_label = Label(data_frame_inv, text="Shopping list Id")
inv_shoplistid_label.grid(row=1, column=0, padx=10, pady=10)
inv_shoplistid_entry = Entry(data_frame_inv)
inv_shoplistid_entry.grid(row=1, column=1, padx=10, pady=10)

inv_totalp_label = Label(data_frame_inv, text="Total Price")
inv_totalp_label.grid(row=1, column=2, padx=10, pady=10)
inv_totalp_entry = Entry(data_frame_inv)
inv_totalp_entry.grid(row=1, column=3, padx=10, pady=10)

inv_cityid_label = Label(data_frame_inv, text="City Id")
inv_cityid_label.grid(row=1, column=4, padx=10, pady=10)
inv_cityid_entry = Entry(data_frame_inv)
inv_cityid_entry.grid(row=1, column=5, padx=10, pady=10)

inv_deliverid_label = Label(data_frame_inv, text="Deliver Id")
inv_deliverid_label.grid(row=1, column=6, padx=10, pady=10)
inv_deliverid_entry = Entry(data_frame_inv)
inv_deliverid_entry.grid(row=1, column=7, padx=10, pady=10)

inv_shipment_label = Label(data_frame_inv, text="Shipping Status")
inv_shipment_label.grid(row=2, column=0, padx=10, pady=10)
inv_shipment_entry = Entry(data_frame_inv)
inv_shipment_entry.grid(row=2, column=1, padx=10, pady=10)


############################ Invoice Modify Buttons ####################################

def select_inv_record():
    # Clear textbox
    inv_id_entry.delete(0, END)
    inv_date_entry.delete(0, END)
    inv_workerid_entry.delete(0, END)
    inv_customerid_entry.delete(0, END)
    inv_shoplistid_entry.delete(0, END)
    inv_totalp_entry.delete(0, END)
    inv_cityid_entry.delete(0, END)
    inv_deliverid_entry.delete(0, END)
    inv_shipment_entry.delete(0, END)
    # focus the selection
    selected = my_tree.focus()

    # Grab record values
    values = my_tree.item(selected,'values')

    # outpus to textbox
    inv_id_entry.insert(0, values[0])
    inv_date_entry.insert(0, values[1])
    inv_workerid_entry.insert(0, values[2])
    inv_customerid_entry.insert(0, values[3])
    inv_shoplistid_entry.insert(0, values[4])
    inv_totalp_entry.insert(0, values[5])
    inv_cityid_entry.insert(0, values[6])
    inv_deliverid_entry.insert(0, values[7])
    inv_shipment_entry.insert(0, values[8])

def update_inv_record():
    selected = my_tree.focus()
    my_tree.item(selected, text="",values=(inv_id_entry.get(), inv_date_entry.get(), inv_workerid_entry.get(), inv_customerid_entry.get(), inv_shoplistid_entry.get(), inv_totalp_entry.get(), inv_cityid_entry.get(), inv_deliverid_entry.get(), inv_shipment_entry.get()))

    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    
    c.execute('''
    UPDATE Invoices SET
    invoice_date = :invoice_date,
    worker_id = :worker_id,
    customer_id = :customer_id,
    shopping_list_id = :shopping_list_id,
    total_price = :total_price,
    city_id = :city_id,
    driver_id = :driver_id,
    shipping_status = :shipping_status
    WHERE invoice_id = :invoice_id
    ''',
    {
        'invoice_date': inv_date_entry.get(),
        'worker_id': inv_workerid_entry.get(),
        'customer_id': inv_customerid_entry.get(),
        'shopping_list_id': inv_shoplistid_entry.get(),
        'total_price': inv_totalp_entry.get(),
        'city_id': inv_cityid_entry.get(),
        'driver_id': inv_deliverid_entry.get(),
        'shipping_status': inv_shipment_entry.get(),
        'invoice_id': inv_id_entry.get(),
    })
    conn.commit()
    conn.close()
    messagebox.showinfo("Info", "Invoice Update Successful")

def add_inv_record():
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    
    c.execute('INSERT INTO Invoices VALUES (:invoice_id,:invoice_date,:worker_id,:customer_id,:shopping_list_id,:total_price,:city_id,:driver_id,:shipping_status)',
    {
        'invoice_id': inv_id_entry.get(),
        'invoice_date': inv_date_entry.get(),
        'worker_id': inv_workerid_entry.get(),
        'customer_id': inv_customerid_entry.get(),
        'shopping_list_id': inv_shoplistid_entry.get(),
        'total_price': inv_totalp_entry.get(),
        'city_id': inv_cityid_entry.get(),
        'driver_id': inv_deliverid_entry.get(),
        'shipping_status': inv_shipment_entry.get(),
    })
    conn.commit()
    conn.close()
    remove_all()
    View_invoice()
    messagebox.showinfo("Info", "New Invoice Added")

def remove_inv_record():
    x = my_tree.selection()[0]
    my_tree.delete(x)

    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    
    c.execute('DELETE FROM Invoices WHERE invoice_id=' + inv_id_entry.get())
    conn.commit()
    conn.close()
    remove_all()
    View_invoice()
    messagebox.showinfo("Info", "Invoice Deleted")


# Buttons Frame
inv_modify_button_frame = LabelFrame(root, text="Invoice Modify")
#inv_modify_button_frame.pack(fill="x", expand="yes", padx=20)

# Add Buttons
select_record_button = Button(inv_modify_button_frame, text="Select Record",command=select_inv_record)
select_record_button.grid(row=0, column=0, padx=10, pady=10)

update_button = Button(inv_modify_button_frame, text="Update Record", command=update_inv_record)
update_button.grid(row=0, column=1, padx=10, pady=10)

add_button = Button(inv_modify_button_frame, text="Add Record", command=add_inv_record)
add_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(inv_modify_button_frame, text="Remove Selected Record", command=remove_inv_record)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)


############################ Warehouse Input data frame #########################
# Add Record Entry Boxes
data_frame_warehouse = LabelFrame(root, text="Record")
#data_frame_warehouse.pack(fill="x", expand="yes", padx=20)

warehouse_stocklist_id_label = Label(data_frame_warehouse, text="Stock List Id")
warehouse_stocklist_id_label.grid(row=0, column=0, padx=10, pady=10)
warehouse_stocklist_id_entry = Entry(data_frame_warehouse)
warehouse_stocklist_id_entry.grid(row=0, column=1, padx=10, pady=10)

warehouse_id_label = Label(data_frame_warehouse, text="Warehouse Id")
warehouse_id_label.grid(row=0, column=2, padx=10, pady=10)
warehouse_id_entry = Entry(data_frame_warehouse)
warehouse_id_entry.grid(row=0, column=3, padx=10, pady=10)

warehouse_city_id_label = Label(data_frame_warehouse, text="City Id")
warehouse_city_id_label.grid(row=0, column=4, padx=10, pady=10)
warehouse_city_id_entry = Entry(data_frame_warehouse)
warehouse_city_id_entry.grid(row=0, column=5, padx=10, pady=10)

warehouse_agent_id_label = Label(data_frame_warehouse, text="Agent Id")
warehouse_agent_id_label.grid(row=0, column=6, padx=10, pady=10)
warehouse_agent_id_entry = Entry(data_frame_warehouse)
warehouse_agent_id_entry.grid(row=0, column=7, padx=10, pady=10)

warehouse_item_id_label = Label(data_frame_warehouse, text="Item Id")
warehouse_item_id_label.grid(row=1, column=0, padx=10, pady=10)
warehouse_item_id_entry = Entry(data_frame_warehouse)
warehouse_item_id_entry.grid(row=1, column=1, padx=10, pady=10)

warehouse_item_name_label = Label(data_frame_warehouse, text="Item Name")
warehouse_item_name_label.grid(row=1, column=2, padx=10, pady=10)
warehouse_item_name_entry = Entry(data_frame_warehouse)
warehouse_item_name_entry.grid(row=1, column=3, padx=10, pady=10)

warehouse_item_quant_label = Label(data_frame_warehouse, text="Item Quantity")
warehouse_item_quant_label.grid(row=1, column=4, padx=10, pady=10)
warehouse_item_quant_entry = Entry(data_frame_warehouse)
warehouse_item_quant_entry.grid(row=1, column=5, padx=10, pady=10)

############################ Warehouse Modify Buttons ####################################

def select_warehouse_record():
    # Clear textbox
    warehouse_stocklist_id_entry.delete(0, END)
    warehouse_id_entry.delete(0, END)
    warehouse_city_id_entry.delete(0, END)
    warehouse_agent_id_entry.delete(0, END)
    warehouse_item_id_entry.delete(0, END)
    warehouse_item_name_entry.delete(0, END)
    warehouse_item_quant_entry.delete(0, END)

    # focus the selection
    selected = my_tree.focus()

    # Grab record values
    values = my_tree.item(selected,'values')

    # outpus to textbox
    warehouse_stocklist_id_entry.insert(0, values[0])
    warehouse_id_entry.insert(0, values[1])
    warehouse_city_id_entry.insert(0, values[2])
    warehouse_agent_id_entry.insert(0, values[3])
    warehouse_item_id_entry.insert(0, values[4])
    warehouse_item_name_entry.insert(0, values[5])
    warehouse_item_quant_entry.insert(0, values[6])

def update_warehouse_record():
    selected = my_tree.focus()
    my_tree.item(selected, text="",values=(warehouse_stocklist_id_entry.get(), warehouse_id_entry.get(), warehouse_city_id_entry.get(), warehouse_agent_id_entry.get(), warehouse_item_id_entry.get(), warehouse_item_name_entry.get(), warehouse_item_quant_entry.get()))

    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    
    c.execute('''
    UPDATE Warehouses SET
    warehouse_id = :warehouse_id,
    city_id = :city_id,
    agent_id = :agent_id,
    item_id = :item_id,
    item_name = :item_name,
    stock_item_quantity = :stock_item_quantity
    WHERE stock_list_id = :stock_list_id
    ''',
    {
        'warehouse_id': warehouse_id_entry.get(),
        'city_id': warehouse_city_id_entry.get(),
        'agent_id': warehouse_agent_id_entry.get(),
        'item_id': warehouse_item_id_entry.get(),
        'item_name': warehouse_item_name_entry.get(),
        'stock_item_quantity': warehouse_item_quant_entry.get(),
        'stock_list_id': warehouse_stocklist_id_entry.get(),
    })
    conn.commit()
    conn.close()
    messagebox.showinfo("Info", "Warehouse Record Update Successful")

def add_warehouse_record():
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    
    c.execute('INSERT INTO Warehouses VALUES (:stock_list_id,:warehouse_id,:city_id,:agent_id,:item_id,:item_name,:stock_item_quantity)',
    {
        'stock_list_id': warehouse_stocklist_id_entry.get(),
        'warehouse_id': warehouse_id_entry.get(),
        'city_id': warehouse_city_id_entry.get(),
        'agent_id': warehouse_agent_id_entry.get(),
        'item_id': warehouse_item_id_entry.get(),
        'item_name': warehouse_item_name_entry.get(),
        'stock_item_quantity': warehouse_item_quant_entry.get(),
    })
    conn.commit()
    conn.close()
    remove_all()
    View_warehouse()
    messagebox.showinfo("Info", "New Warehouse Record Added")

def remove_warehouse_record():
    x = my_tree.selection()[0]
    my_tree.delete(x)

    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    
    c.execute('DELETE FROM Warehouses WHERE stock_list_id=' + warehouse_stocklist_id_entry.get())
    conn.commit()
    conn.close()
    remove_all()
    View_warehouse()
    messagebox.showinfo("Info", "Warehouse Record Deleted")

# Buttons Frame
warehouse_modify_button_frame = LabelFrame(root, text="Warehouse Stock Modify")
#warehouse_modify_button_frame.pack(fill="x", expand="yes", padx=20)

# Add Buttons
select_record_button = Button(warehouse_modify_button_frame, text="Select Record",command=select_warehouse_record)
select_record_button.grid(row=0, column=0, padx=10, pady=10)

update_button = Button(warehouse_modify_button_frame, text="Update Record",command=update_warehouse_record)
update_button.grid(row=0, column=1, padx=10, pady=10)

add_button = Button(warehouse_modify_button_frame, text="Add Record",command=add_warehouse_record)
add_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(warehouse_modify_button_frame, text="Remove Selected Record",command=remove_warehouse_record)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)


############################ Agent Advanced Filter Buttons ####################################

# Buttons Frame
agent_button_frame = LabelFrame(root, text="Agent Advanced Filter")
#agent_button_frame.pack(fill="x", expand="yes", padx=20)

# Add Buttons and Labels
show_best_button = Button(agent_button_frame, text="Show the Best Agent",command=show_the_best_agent)
show_best_button.grid(row=1, column=0, padx=10, pady=10)

show_worst_button = Button(agent_button_frame, text="Show the Worst Agent",command=show_the_worst_agent)
show_worst_button.grid(row=1, column=1, padx=10, pady=10)


############################ Worker Advanced Filter Buttons ####################################

# Buttons Frame
worker_button_frame = LabelFrame(root, text="Worker Advanced Filter")
#worker_button_frame.pack(fill="x", expand="yes", padx=20)

# Add Buttons and Labels
show_best_button = Button(worker_button_frame, text="Show the Best Worker",command=show_the_best_worker)
show_best_button.grid(row=1, column=0, padx=10, pady=10)

show_worst_button = Button(worker_button_frame, text="Show the Worst Worker",command=show_the_worst_worker)
show_worst_button.grid(row=1, column=1, padx=10, pady=10)

############################ Customer Advanced Filter Buttons ####################################

# Buttons Frame
customer_button_frame = LabelFrame(root, text="Customer Advanced Filter")
#customer_button_frame.pack(fill="x", expand="yes", padx=20)

# Add Buttons and Labels
show_best_button = Button(customer_button_frame, text="Show Top New Phone Buyer",command=show_newphone_customer)
show_best_button.grid(row=1, column=0, padx=10, pady=10)

show_worst_button = Button(customer_button_frame, text="Show Top Old Phone Buyer",command=show_oldphone_customer)
show_worst_button.grid(row=1, column=1, padx=10, pady=10)

############################ Driver Advanced Filter Buttons ####################################

# Buttons Frame
driver_button_frame = LabelFrame(root, text="Driver Advanced Filter")
#driver_button_frame.pack(fill="x", expand="yes", padx=20)

# Add Buttons and Labels
show_best_button = Button(driver_button_frame, text="Show Most Active Driver",command=show_active_driver)
show_best_button.grid(row=1, column=0, padx=10, pady=10)

show_best_button = Button(driver_button_frame, text="Show Non Active Driver",command=show_nonactive_driver)
show_best_button.grid(row=1, column=1, padx=10, pady=10)

View_invoice()

root.mainloop()
