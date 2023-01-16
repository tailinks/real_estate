from cash_flows import *
import tkinter as tk
from cash_flows import *
from tkinter import ttk
from tkinter import messagebox

class App:
    def __init__(self, master):
        self.master = master
        master.title("Real Estate Present Value Calculator")

        self.property_price = tk.StringVar()
        self.down_payment = tk.StringVar()
        self.discount_rate = tk.StringVar()
        self.mortgage_rate = tk.StringVar()
        self.mortgage_length = tk.StringVar()
        self.rent_amount = tk.StringVar()
        self.rent_growth = tk.StringVar()
        self.maintenance_cost = tk.StringVar()
        self.costs_growth = tk.StringVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        # create notebook
        self.notebook = ttk.Notebook(self.master)
        self.notebook.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # create first tab for present value calculation
        self.present_value_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.present_value_tab, text="Present Value")
        tk.Label(self.present_value_tab, text="Property Price").grid(row=0, column=0)
        tk.Label(self.present_value_tab, text="Down Payment").grid(row=1, column=0)
        tk.Label(self.present_value_tab, text="Discount Rate (Decimal)").grid(row=2, column=0)
        tk.Label(self.present_value_tab, text="Mortgage Rate (Decimal)").grid(row=3, column=0)
        tk.Label(self.present_value_tab, text="Mortgage Length (Years)").grid(row=4, column=0)
        tk.Label(self.present_value_tab, text="Rent Amount Monthly").grid(row=5, column=0)
        tk.Label(self.present_value_tab, text="Rent Growth Yearly (Decimal)").grid(row=6, column=0)
        tk.Label(self.present_value_tab, text="Maintenance Yearly Cost").grid(row=7, column=0)
        tk.Label(self.present_value_tab, text="Costs Growth Yearly (Decimal)").grid(row=8, column=0)
        tk.Entry(self.present_value_tab, textvariable=self.property_price).grid(row=0, column=1)
        tk.Entry(self.present_value_tab, textvariable=self.down_payment).grid(row=1, column=1)
        tk.Entry(self.present_value_tab, textvariable=self.discount_rate).grid(row=2, column=1)
        tk.Entry(self.present_value_tab, textvariable=self.mortgage_rate).grid(row=3, column=1)
        tk.Entry(self.present_value_tab, textvariable=self.mortgage_length).grid(row=4, column=1)
        tk.Entry(self.present_value_tab, textvariable=self.rent_amount).grid(row=5, column=1)
        tk.Entry(self.present_value_tab, textvariable=self.rent_growth).grid(row=6, column=1)
        tk.Entry(self.present_value_tab, textvariable=self.maintenance_cost).grid(row=7, column=1)
        tk.Entry(self.present_value_tab, textvariable=self.costs_growth).grid(row=8, column=1)
        
        #create a button to calculate the present value
        self.calculate_button = tk.Button(self.present_value_tab, text="Calculate", command=self.calculate_present_value)
        self.calculate_button.grid(row=9, column=0, columnspan=2, pady=10)
        
        #create the second tab for price of property calculation 
        self.price_of_property_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.price_of_property_tab, text="Price of Property")
        tk.Label(self.price_of_property_tab, text="Down Payment").grid(row=0, column=0)
        tk.Label(self.price_of_property_tab, text="Discount Rate (Decimal)").grid(row=1, column=0)
        tk.Label(self.price_of_property_tab, text="Mortgage Rate (Decimal)").grid(row=2, column=0)
        tk.Label(self.price_of_property_tab, text="Mortgage Length (Years)").grid(row=3, column=0)
        tk.Label(self.price_of_property_tab, text="Rent Amount Monthly").grid(row=4, column=0)
        tk.Label(self.price_of_property_tab, text="Rent Growth Yearly (Decimal)").grid(row=5, column=0)
        tk.Label(self.price_of_property_tab, text="Maintenance Yearly Cost").grid(row=6, column=0)
        tk.Label(self.price_of_property_tab, text="Costs Growth Yearly (Decimal)").grid(row=7, column=0)
        tk.Entry(self.price_of_property_tab, textvariable=self.down_payment).grid(row=0, column=1)
        tk.Entry(self.price_of_property_tab, textvariable=self.discount_rate).grid(row=1, column=1)
        tk.Entry(self.price_of_property_tab, textvariable=self.mortgage_rate).grid(row=2, column=1)
        tk.Entry(self.price_of_property_tab, textvariable=self.mortgage_length).grid(row=3, column=1)
        tk.Entry(self.price_of_property_tab, textvariable=self.rent_amount).grid(row=4, column=1)
        tk.Entry(self.price_of_property_tab, textvariable=self.rent_growth).grid(row=5, column=1)
        tk.Entry(self.price_of_property_tab, textvariable=self.maintenance_cost).grid(row=6, column=1)
        tk.Entry(self.price_of_property_tab, textvariable=self.costs_growth).grid(row=7, column=1)

        #create a label to display the result
        self.result_label = tk.Label(self.price_of_property_tab, text="")
        self.result_label.grid(row=9, column=0, columnspan=2)
        
        #create a button to calculate the price of property
        self.calculate_button = tk.Button(self.price_of_property_tab, text="Calculate", command=self.calculate_price_of_property)
        self.calculate_button.grid(row=8, column=0, columnspan=2, pady=10)

    def calculate_present_value(self):
        property_price = float(self.property_price.get())
        down_payment = float(self.down_payment.get())
        discount_rate = InterestRate(float(self.discount_rate.get()))
        mortgage_rate = InterestRate(float(self.mortgage_rate.get()))
        mortgage_length = int(self.mortgage_length.get())
        rent_amount = float(self.rent_amount.get())
        rent_growth = InterestRate(float(self.rent_growth.get()))
        maintenance_costs = float(self.maintenance_cost.get())
        costs_growth = InterestRate(float(self.costs_growth.get()))
        
         #Do the calculations and store the result
        
        number_periods_mortgage = mortgage_length*12
        
        mortgage_payment = payment_annuity(property_price-down_payment, mortgage_rate, number_periods_mortgage)
        mortgage = Annuity(-mortgage_payment, number_periods_mortgage,time_frame="M", )
        
        maintenance = Perpetuity(-maintenance_costs, cash_flow_growth=costs_growth)
        
        rent = Perpetuity(rent_amount, time_frame="M", cash_flow_growth=rent_growth)
        
        present_value = -down_payment + mortgage.get_present_value(discount_rate) + maintenance.get_present_value(discount_rate) + rent.get_present_value(discount_rate)
        
        #display result in a message box
        messagebox.showinfo("Present Value", "The present value of the real estate project is ${:.2f}".format(present_value))

        
    def calculate_price_of_property(self):
        down_payment = float(self.down_payment.get())
        discount_rate = InterestRate(float(self.discount_rate.get()))
        mortgage_rate = InterestRate(float(self.mortgage_rate.get()))
        mortgage_length = int(self.mortgage_length.get())
        rent_amount = float(self.rent_amount.get())
        rent_growth = InterestRate(float(self.rent_growth.get()))
        maintenance_costs = float(self.maintenance_cost.get())
        costs_growth = InterestRate(float(self.costs_growth.get()))
        
        
        number_mortgage_payments = mortgage_length*12
        
        maintenance = Perpetuity(-maintenance_costs, cash_flow_growth=costs_growth)
        
        rent = Perpetuity(rent_amount, time_frame="M", cash_flow_growth=rent_growth)
        
        null_pv = maintenance.get_present_value(discount_rate) + rent.get_present_value(discount_rate) - down_payment
        maximum_payment = payment_annuity(null_pv, mortgage_rate, number_mortgage_payments)
        price_of_property = round(Annuity(maximum_payment, number_mortgage_payments, time_frame="M").get_present_value(discount_rate)+ down_payment)
        
        self.result_label.configure(text=f'The Maximum Price of Property is: {price_of_property}')

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()