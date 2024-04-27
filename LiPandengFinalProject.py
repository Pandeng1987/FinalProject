"""
LiPandengFinalProject - Personal Finance Track Manager
Name: Pandeng
Date: Apr 28, 2024
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class PersonalFinanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Track Manager")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.login_frame = ttk.Frame(self.root)
        self.dashboard_frame = ttk.Frame(self.root)
        self.income_frame = ttk.Frame(self.root)
        self.expense_frame = ttk.Frame(self.root)
        self.budget_frame = ttk.Frame(self.root)

        self.current_frame = None
        self.create_login_frame()

    def create_login_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = self.login_frame
        self.current_frame.pack(fill="both", expand=True)

        ttk.Label(self.current_frame, text="Username:").pack()
        self.username_entry = ttk.Entry(self.current_frame)
        self.username_entry.pack()

        ttk.Label(self.current_frame, text="Password:").pack()
        self.password_entry = ttk.Entry(self.current_frame, show="*")
        self.password_entry.pack()

        ttk.Button(self.current_frame, text="Login", command=self.login).pack()
        ttk.Button(self.current_frame, text="Register", command=self.register).pack()

    def create_dashboard_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = self.dashboard_frame
        self.current_frame.pack(fill="both", expand=True)

        ttk.Label(self.current_frame, text="Dashboard", font=("Helvetica", 16, "bold")).pack(pady=10)

        ttk.Button(self.current_frame, text="Income", command=self.create_income_frame).pack(pady=5)
        ttk.Button(self.current_frame, text="Expenses", command=self.create_expense_frame).pack(pady=5)
        ttk.Button(self.current_frame, text="Budget", command=self.create_budget_frame).pack(pady=5)
        ttk.Button(self.current_frame, text="Logout", command=self.create_login_frame).pack(pady=5)

    def create_income_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = self.income_frame
        self.current_frame.pack(fill="both", expand=True)

        ttk.Label(self.current_frame, text="Income Tracking", font=("Helvetica", 16, "bold")).pack(pady=10)

        ttk.Label(self.current_frame, text="Date:").pack()
        self.income_date_entry = ttk.Entry(self.current_frame)
        self.income_date_entry.pack()

        ttk.Label(self.current_frame, text="Amount:").pack()
        self.income_amount_entry = ttk.Entry(self.current_frame)
        self.income_amount_entry.pack()

        ttk.Button(self.current_frame, text="Submit", command=self.submit_income).pack(pady=10)
        ttk.Button(self.current_frame, text="Back to Dashboard", command=self.create_dashboard_frame).pack(pady=5)

    def create_expense_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = self.expense_frame
        self.current_frame.pack(fill="both", expand=True)

        ttk.Label(self.current_frame, text="Expense Tracking", font=("Helvetica", 16, "bold")).pack(pady=10)

        ttk.Label(self.current_frame, text="Category:").pack()
        self.expense_category_entry = ttk.Entry(self.current_frame)
        self.expense_category_entry.pack()

        ttk.Label(self.current_frame, text="Amount:").pack()
        self.expense_amount_entry = ttk.Entry(self.current_frame)
        self.expense_amount_entry.pack()

        ttk.Button(self.current_frame, text="Submit", command=self.submit_expense).pack(pady=10)
        ttk.Button(self.current_frame, text="Back to Dashboard", command=self.create_dashboard_frame).pack(pady=5)

    def create_budget_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = self.budget_frame
        self.current_frame.pack(fill="both", expand=True)

        ttk.Label(self.current_frame, text="Budget Management", font=("Helvetica", 16, "bold")).pack(pady=10)

        ttk.Label(self.current_frame, text="Budget Category:").pack()
        self.budget_category_entry = ttk.Entry(self.current_frame)
        self.budget_category_entry.pack()

        ttk.Label(self.current_frame, text="Amount:").pack()
        self.budget_amount_entry = ttk.Entry(self.current_frame)
        self.budget_amount_entry.pack()

        ttk.Button(self.current_frame, text="Submit", command=self.submit_budget).pack(pady=10)
        ttk.Button(self.current_frame, text="Back to Dashboard", command=self.create_dashboard_frame).pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # In a real application, you would perform authentication here.
        # For demonstration purposes, let's assume the login is successful:
        messagebox.showinfo("Login", f"Welcome, {username}!")
        self.create_dashboard_frame()

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # In a real application, you would perform registration here.
        # For demonstration purposes, let's assume the registration is successful:
        messagebox.showinfo("Registration", f"Account created for {username}!")
        self.create_dashboard_frame()

    def submit_income(self):
        date = self.income_date_entry.get()
        amount = self.income_amount_entry.get()

        # In a real application, you would process and store the income data here.
        # For demonstration purposes, let's just display the entered data:
        messagebox.showinfo("Income", f"Date: {date}\nAmount: {amount}")
        self.clear_entries()

    def submit_expense(self):
        category = self.expense_category_entry.get()
        amount = self.expense_amount_entry.get()

        # In a real application, you would process and store the expense data here.
        # For demonstration purposes, let's just display the entered data:
        messagebox.showinfo("Expense", f"Category: {category}\nAmount: {amount}")
        self.clear_entries()

    def submit_budget(self):
        category = self.budget_category_entry.get()
        amount = self.budget_amount_entry.get()

        # In a real application, you would process and store the budget data here.
        # For demonstration purposes, let's just display the entered data:
        messagebox.showinfo("Budget", f"Category: {category}\nAmount: {amount}")
        self.clear_entries()

    def clear_entries(self):
        self.income_date_entry.delete(0, tk.END)
        self.income_amount_entry.delete(0, tk.END)
        self.expense_category_entry.delete(0, tk.END)
        self.expense_amount_entry.delete(0, tk.END)
        self.budget_category_entry.delete(0, tk.END)
        self.budget_amount_entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = PersonalFinanceApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

