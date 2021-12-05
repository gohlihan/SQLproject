import DbFunction as dbf
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3

#----------Main functions--------------------

    #dbf.show_warehouse_inv(1)

    #dbf.show_all_warehouse_inv()

    #dbf.change_warehouse_inv(99,1)

    #dbf.change_invoice_city(5,3)

    #dbf.create_invoice(invoice_id,invoice_date,customer_id,shopping_list_id,total_price,city_id,driver_id,shipping_status)

    #dbf.show_customer_totalbuy()

    #dbf.show_newphone_customer()

    #dbf.show_the_best_agent()

    #dbf.show_the_best_worker()

    #dbf.show_worker_sales()

    #dbf.show_agent_sales()

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
    for row in item:
        #print(row) # it print all records in the database
        my_tree.insert("", tk.END, values=row)
    conn.commit()
    conn.close()

# view all warehouse's stock
def View_warehouse():
    remove_all()
    # Unpack other element
    data_frame_inv.pack_forget()
    inv_modify_button_frame.pack_forget()
    agent_button_frame.pack_forget()

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

#show the best agents
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
    
#show the best agents
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

############################# Invoice Input Data Frame #############################

# Add Record Entry Boxes
data_frame_inv = LabelFrame(root, text="Record")
#data_frame_inv.pack(fill="x", expand="yes", padx=20)

inv_date_label = Label(data_frame_inv, text="Invoice Date")
inv_date_label.grid(row=0, column=0, padx=10, pady=10)
inv_date_entry = Entry(data_frame_inv)
inv_date_entry.grid(row=0, column=1, padx=10, pady=10)

inv_workerid_label = Label(data_frame_inv, text="Worker Id")
inv_workerid_label.grid(row=0, column=2, padx=10, pady=10)
inv_workerid_entry = Entry(data_frame_inv)
inv_workerid_entry.grid(row=0, column=3, padx=10, pady=10)

inv_customerid_label = Label(data_frame_inv, text="Customer Id")
inv_customerid_label.grid(row=0, column=4, padx=10, pady=10)
inv_customerid_entry = Entry(data_frame_inv)
inv_customerid_entry.grid(row=0, column=5, padx=10, pady=10)

inv_shoplistid_label = Label(data_frame_inv, text="Shopping list Id")
inv_shoplistid_label.grid(row=0, column=6, padx=10, pady=10)
inv_shoplistid_entry = Entry(data_frame_inv)
inv_shoplistid_entry.grid(row=0, column=7, padx=10, pady=10)

inv_totalp_label = Label(data_frame_inv, text="Total Price")
inv_totalp_label.grid(row=1, column=0, padx=10, pady=10)
inv_totalp_entry = Entry(data_frame_inv)
inv_totalp_entry.grid(row=1, column=1, padx=10, pady=10)

inv_cityid_label = Label(data_frame_inv, text="City Id")
inv_cityid_label.grid(row=1, column=2, padx=10, pady=10)
inv_cityid_entry = Entry(data_frame_inv)
inv_cityid_entry.grid(row=1, column=3, padx=10, pady=10)

inv_deliverid_label = Label(data_frame_inv, text="Deliver Id")
inv_deliverid_label.grid(row=1, column=4, padx=10, pady=10)
inv_deliverid_entry = Entry(data_frame_inv)
inv_deliverid_entry.grid(row=1, column=5, padx=10, pady=10)

inv_shipment_label = Label(data_frame_inv, text="Shipping Status")
inv_shipment_label.grid(row=1, column=6, padx=10, pady=10)
inv_shipment_entry = Entry(data_frame_inv)
inv_shipment_entry.grid(row=1, column=7, padx=10, pady=10)


############################ Invoice Modify Buttons ####################################

# Buttons Frame
inv_modify_button_frame = LabelFrame(root, text="Invoice Modify")
#inv_modify_button_frame.pack(fill="x", expand="yes", padx=20)

# Add Buttons
select_record_button = Button(inv_modify_button_frame, text="Select Record")
select_record_button.grid(row=0, column=0, padx=10, pady=10)

update_button = Button(inv_modify_button_frame, text="Update Record")
update_button.grid(row=0, column=1, padx=10, pady=10)

add_button = Button(inv_modify_button_frame, text="Add Record")
add_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(inv_modify_button_frame, text="Remove Selected")
remove_one_button.grid(row=0, column=3, padx=10, pady=10)



############################ Warehouse Input data frame #########################
# Add Record Entry Boxes
data_frame_warehouse = LabelFrame(root, text="Record")
#data_frame_warehouse.pack(fill="x", expand="yes", padx=20)

warehouse_item_id_label = Label(data_frame_warehouse, text="Item Id")
warehouse_item_id_label.grid(row=0, column=0, padx=10, pady=10)
warehouse_item_id_entry = Entry(data_frame_warehouse)
warehouse_item_id_entry.grid(row=0, column=1, padx=10, pady=10)

warehouse_item_name_label = Label(data_frame_warehouse, text="Item Name")
warehouse_item_name_label.grid(row=0, column=2, padx=10, pady=10)
warehouse_item_name_entry = Entry(data_frame_warehouse)
warehouse_item_name_entry.grid(row=0, column=3, padx=10, pady=10)

warehouse_item_quant_label = Label(data_frame_warehouse, text="Item Quantity")
warehouse_item_quant_label.grid(row=0, column=4, padx=10, pady=10)
warehouse_item_quant_entry = Entry(data_frame_warehouse)
warehouse_item_quant_entry.grid(row=0, column=5, padx=10, pady=10)

############################ Warehouse Modify Buttons ####################################

# Buttons Frame
warehouse_modify_button_frame = LabelFrame(root, text="Warehouse Stock Modify")
#warehouse_modify_button_frame.pack(fill="x", expand="yes", padx=20)

# Add Buttons
select_record_button = Button(warehouse_modify_button_frame, text="Select Record")
select_record_button.grid(row=0, column=0, padx=10, pady=10)

update_button = Button(warehouse_modify_button_frame, text="Update Record")
update_button.grid(row=0, column=1, padx=10, pady=10)

############################ Agent Advanced Filter Buttons ####################################

# Buttons Frame
agent_button_frame = LabelFrame(root, text="Agent Advanced Filter")
#agent_button_frame.pack(fill="x", expand="yes", padx=20)

# Add Buttons and Labels
#Entry(agent_button_frame, text=()).grid(row=0, column=0, padx=10, pady=10)

select_record_button = Button(agent_button_frame, text="Show the Best Agent",command=show_the_best_agent)
select_record_button.grid(row=1, column=0, padx=10, pady=10)

update_button = Button(agent_button_frame, text="Show the Worst Agent",command=show_the_worst_agent)
update_button.grid(row=1, column=1, padx=10, pady=10)


View_invoice()

root.mainloop()
