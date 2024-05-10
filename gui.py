from accounts import Account
from tkinter import *
import csv

class GUI:

    def __init__(self, window) -> None:

        '''
        This function is the main setup for the general user interface

        :param window: primary tkinter display
        '''

        self.window = window

        custom_font1 = ('Verdana', 16)
        custom_font2 = ('Verdana', 8)

        self.frame_one = Frame(window)
        self.login_label = Label(self.frame_one, text='Please Login to Continue', font=custom_font1)
        self.name1_label = Label(self.frame_one, text='First Name:', font=custom_font2)
        self.name1_input = Entry(self.frame_one, width=30)
        self.login_label.pack(pady=6)
        self.name1_label.pack(side='left')
        self.name1_input.pack(side='left')
        self.frame_one.pack(pady=6)

        self.frame_two = Frame(window)
        self.name2_label = Label(self.frame_two, text='Last Name: ', font=custom_font2)
        self.name2_input = Entry(self.frame_two, width=30)
        self.name2_label.pack(side='left')
        self.name2_input.pack(side='left')
        self.frame_two.pack(pady=6)

        self.frame_three = Frame(window)
        self.pin_label = Label(self.frame_three, text='PIN Number:', font=custom_font2)
        self.pin_input = Entry(self.frame_three, show='*', width=30)
        self.pin_label.pack(side='left')
        self.pin_input.pack(side='left')
        self.frame_three.pack(pady=6)

        self.frame_four = Frame(window)
        self.Submit_button = Button(self.frame_four, text='SUBMIT', font=custom_font1, command=self.search)
        self.Submit_button.pack()
        self.frame_four.pack(pady=6)

        self.frame_five = Frame(window)
        self.welcome_label = Label(self.frame_five, text='', font=custom_font1)
        self.question_label = Label(self.frame_five, text='', font=custom_font2)
        self.welcome_label.pack(pady=12)
        self.question_label.pack()
        self.frame_five.pack()

        self.frame_six = Frame(window)
        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.deposit_button = Radiobutton(self.frame_six, variable=self.radio_answer, value=1,  text='Deposit', font=custom_font2)
        self.withdraw_button = Radiobutton(self.frame_six, variable=self.radio_answer, value=2, text='Withdraw', font=custom_font2)
        self.create_button = Button(self.frame_six, text='CREATE', font=custom_font2, command=self.create)
        self.cancel_button = Button(self.frame_six, text='CANCEL', font=custom_font2, command=self.cancel)
        self.frame_six.pack(pady=6)

        self.frame_seven = Frame(window)
        self.amount_error = Label(self.frame_seven, text='')
        self.amount_label = Label(self.frame_seven, text='Amount:')
        self.amount_input = Entry(self.frame_seven, width=30)
        self.frame_seven.pack()

        self.frame_eight = Frame(window)
        self.amount_submit = Button(self.frame_eight, text='ENTER', font=custom_font2, command=self.move_money)
        self.amount_exit = Button(self.frame_eight, text='EXIT', font=custom_font2, command=self.cancel)
        self.new_balance = Label(self.frame_eight, text='', font=custom_font2)
        self.new_balance.pack()
        self.frame_eight.pack(pady=6)

        self.frame_nine = Frame(window)
        self.error_label = Label(self.frame_nine, text='', font=custom_font2)
        self.error_label.pack()
        self.frame_nine.pack()

    def search(self) -> None:

        '''
        This function is used to search through the csv file in order to
        either retrieve a name, or ask the user whether they would like
        to create a new account or not.

        :return:
        '''

        self.error_label.config(text='')

        with open('accounts.csv', 'r', newline='') as account_csv:

            csv_reader = csv.reader(account_csv)

            ret_acc = Account(self.name1_input.get())
            first_name = ret_acc.get_name()
            last_name = self.name2_input.get()
            pin_num = self.pin_input.get()
            get_balance = ret_acc.get_balance()
            account_info = [first_name, last_name, pin_num, str(get_balance)]

            try:

                test_pin = int(pin_num)

                if len(first_name) < 1 or len(last_name) < 1:

                    raise AttributeError

                elif len(pin_num) != 4:

                    raise ValueError

                else:

                    for row in csv_reader:

                        if row[0:2] == account_info[0:2]:

                            self.welcome_label.config(text='Welcome to The Bank of Gotham')
                            self.question_label.config(text=f'What would you like to do {self.name1_input.get()}?')
                            self.welcome_label.pack(pady=12)
                            self.create_button.pack_forget()
                            self.cancel_button.pack_forget()
                            self.question_label.pack()
                            self.deposit_button.pack(side='left')
                            self.withdraw_button.pack(side='left')
                            self.amount_error.pack()
                            self.amount_label.pack(side='left', padx=8)
                            self.amount_input.pack(side='left')
                            self.amount_submit.pack(pady=12)
                            self.amount_exit.pack()
                            self.Submit_button.pack_forget()

                        else:

                            self.welcome_label.config(text="Account not found")
                            self.question_label.config(text=f'Create one?')
                            self.deposit_button.pack_forget()
                            self.withdraw_button.pack_forget()
                            self.create_button.pack(pady=8)
                            self.cancel_button.pack()

            except ValueError:

                self.error_label.config(text='Please make sure the PIN is a 4 digit number')

            except AttributeError:

                self.error_label.config(text='Please enter a first and last name')

    def create(self) -> None:

        '''
        If the user decides to create a new account they will be redirected
        here. This is where you will be able to make a new account, and add
        the info to the csv file where other accounts are located.

        :return:
        '''

        self.error_label.config(text='')

        new_acc = Account(self.name1_input.get())
        first_name = new_acc.get_name()
        last_name = self.name2_input.get()
        pin_num = self.pin_input.get()
        get_balance = new_acc.get_balance()
        account_info = [first_name, last_name, pin_num, str(get_balance)]

        try:

            self.Submit_button.pack_forget()

            with open('accounts.csv', 'r', newline='') as account_csv:

                reader = csv.reader(account_csv)

                for row in reader:

                    if row[0:2] == account_info[0:2]:

                        raise TypeError

            with open('accounts.csv', 'a') as account_csv:

                self.create_button.pack_forget()
                self.cancel_button.pack_forget()
                self.welcome_label.config(text='Account Created! Click Submit!')
                self.question_label.config(text='')
                writer = csv.writer(account_csv)
                writer.writerow(account_info)

            self.Submit_button.pack()

        except TypeError:

            self.error_label.config(text='This account already exists!')



    def cancel(self) -> None:

        '''
        This is a function that simply wipes any pieces of the
        GUI that the user is not using. This happens when exit
        or cancel is clicked

        :return:
        '''

        self.create_button.pack_forget()
        self.cancel_button.pack_forget()
        self.welcome_label.config(text='')
        self.question_label.config(text='')
        self.deposit_button.pack_forget()
        self.withdraw_button.pack_forget()
        self.amount_label.pack_forget()
        self.amount_input.pack_forget()
        self.amount_submit.pack_forget()
        self.amount_exit.pack_forget()
        self.new_balance.config(text='')
        self.Submit_button.pack()


    def move_money(self) -> None:

        '''
        This function's primary role is to allocate different
        money where the user wants it to go by withdrawing or
        depositing using the logic from accounts.py

        :return:
        '''

        temp_list = []

        first_name = self.name1_input.get()
        last_name = self.name2_input.get()
        pin_num = self.pin_input.get()
        account_info = [first_name, last_name, pin_num]

        W_or_D = self.radio_answer.get()

        try:

            wd_amount = float(self.amount_input.get())

            with open('accounts.csv', 'r', newline='') as account_csv:

                reader = csv.reader(account_csv)

                for row in reader:

                    if row[0:2] == account_info[0:2]:

                        wd_account = [first_name, last_name, pin_num, row[3]]
                        ret_acc = Account(first_name, float(row[3]))

                    else:

                        temp_list.append(row)

            if W_or_D == 1: #deposit

                deposit = ret_acc.deposit(wd_amount)

                if deposit:

                    pass

                else:

                    raise ValueError

            elif W_or_D == 2: #withdraw

                withdraw = ret_acc.withdraw(wd_amount)

                if withdraw:

                    pass

                else:

                    raise ZeroDivisionError

            else:

                raise AttributeError

            new_balance = round(ret_acc.get_balance(), 2)
            wd_account[3] = new_balance
            temp_list.append(wd_account)

            with open('accounts.csv', 'w') as account_csv:

                writer = csv.writer(account_csv)

                for line in temp_list:

                    writer.writerow(line)

            self.new_balance.config(text=f'New Balance: {new_balance:.2f}')
            self.error_label.config(text='')

        except AttributeError:

            self.error_label.config(text='Would you like to withdraw or deposit?')

        except ZeroDivisionError:

            self.error_label.config(text=f'Make sure your amount is > 0 and not more than your current balance')

        except ValueError:

            self.error_label.config(text='No special characters ($,@,%)')