from tkinter import *
import os
os.system('cls')

EXPRESSION = " "
CONT = "clear"
TERM = ""
RESULT = ""

def change_col(item, btn, event=' '):
    if btn == bt_equal:
        btn.config(bg="#05d2e1", fg="white")
    else:
        btn.config(bg="#595959", fg="white")
    window.after(100, lambda: normal_col(val=item, btn=btn))
    
def normal_col(val, btn):
    if btn == bt_equal:
        btn.config(fg='white', bg='#04a4af')
        calculate()
    elif btn == bt_back:
        btn.config(bg="#131313", fg="white")
        delete()
    else:
        btn.config(bg="#131313", fg="white")
        set_exp(val)

def set_exp(value):
    global EXPRESSION, CONT
    if CONT == 'clear':
        if (EXPRESSION[-1] == '+' or EXPRESSION[-1] == '-' or EXPRESSION[-1] == '×' or EXPRESSION[-1] == '÷') and (value == '+' or value == '-' or value == '×' or value == '÷'):
            if EXPRESSION[-1] != value:  
                EXPRESSION = EXPRESSION[:-1]
                EXPRESSION = EXPRESSION + str(value)
                calc_text.config(text=EXPRESSION)
            else:
                calc_text.config(text=EXPRESSION)
        else:
            EXPRESSION = EXPRESSION + str(value)
            calc_text.config(text=EXPRESSION)
    elif CONT == 'calc':
        if value == '+' or value == '-' or value == '×' or value == '÷':
            EXPRESSION = EXPRESSION + str(value)
            calc_text.config(text=EXPRESSION)
            CONT = 'clear'
        else:
            clear()
            EXPRESSION = EXPRESSION + str(value)
            calc_text.config(text=EXPRESSION)
            CONT = 'clear'
    elif CONT == 'change':
        calc_text.config(text=EXPRESSION)
        CONT = 'calc'

def clear():
    global EXPRESSION
    EXPRESSION = " "
    calc_text.config(text=EXPRESSION)

def calculate():
    global EXPRESSION, CONT, RESULT
    EXPRESSION = EXPRESSION.replace('×', '*')
    EXPRESSION = EXPRESSION.replace('÷', '/')

    if len(EXPRESSION) > 2:
        if EXPRESSION[1] == '*' or EXPRESSION[1] == '/':
            EXPRESSION = "0" + EXPRESSION
    else:
        EXPRESSION = "0+0"

    RESULT = str(eval(EXPRESSION))
    EXPRESSION = RESULT

    EXPRESSION = EXPRESSION.replace('*', '×')
    EXPRESSION = EXPRESSION.replace('/', '÷')
    
    CONT = "calc"
    calc_text.config(text=RESULT)

def delete():
    global EXPRESSION 
    EXPRESSION = EXPRESSION[:-1]
    if EXPRESSION == "":
        EXPRESSION = " "
    calc_text.config(text=EXPRESSION)

def clear_term():
    global EXPRESSION
    if EXPRESSION[-1] != '+' and EXPRESSION[-1] != '-' and EXPRESSION[-1] != '×' and EXPRESSION[-1] != '÷':
        EXPRESSION = EXPRESSION[:-(get_len_last_term())]
        if EXPRESSION == "":
            EXPRESSION = " "
        calc_text.config(text=EXPRESSION)

def get_len_last_term():
    global EXPRESSION
    if EXPRESSION[-1] != '+' and EXPRESSION[-1] != '-' and EXPRESSION[-1] != '×' and EXPRESSION[-1] != '÷':
        chars = len(get_last_term())
        return chars

def get_last_term():
    global EXPRESSION
    if EXPRESSION[-1] != '+' and EXPRESSION[-1] != '-' and EXPRESSION[-1] != '×' and EXPRESSION[-1] != '÷':
        num = []
        for char in EXPRESSION[-1:-(len(EXPRESSION)+1):-1]:
            if char == '+' or char == '-' or char == '×' or char == '÷':
                break
            else:
                num.append(char)

        num.reverse()
        num = ''.join(num)

        return num

def change_sign():
    global EXPRESSION, CONT
    if CONT == 'calc':
        CONT = "change"
        if EXPRESSION[0] == '-':
            EXPRESSION = EXPRESSION.strip('-')
        elif EXPRESSION[0] != '-':
            EXPRESSION = '-' + EXPRESSION
            
        set_exp('')

window = Tk()
window.title("Calculator")
window['bg'] = '#1f1f1f'
window.attributes('-alpha', 0.97)
window.resizable(False, False)
window.geometry('317x402+800+300')
window.config(pady=5, padx=5)

calc_text = Label(text=EXPRESSION, width=11, bg='#8a8a8f', fg='#1f1f20', highlightthickness=0, borderwidth=0, justify="right", font=("Arial", 35, "normal"), pady=10, padx=5, anchor='e')
calc_text.grid(column=0, row=1, columnspan=4, sticky="EW")



bt_C = Button(text="C", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#cc191c', font=("Arial", 12, "normal"), activebackground="#ee2b2e", activeforeground="white", command=clear)
bt_C.grid(column=0, row=2, sticky="EW", padx=1, pady=2)

bt_CE = Button(text="CE", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=clear_term)
bt_CE.grid(column=1, row=2, sticky="EW", padx=1, pady=2)

bt_back = Button(text="◄", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=delete)
bt_back.grid(column=2, row=2, sticky="EW", padx=1, pady=2)
window.bind('<BackSpace>',  lambda event, item="back", btn=bt_back: change_col(item, btn))

bt_div = Button(text="÷", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=lambda: set_exp(value="÷"))
bt_div.grid(column=3, row=2, sticky="EW", padx=1, pady=2)
window.bind('/',  lambda event, item="÷", btn=bt_div: change_col(item, btn))



bt_7 = Button(text="7", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=lambda: set_exp(value=7))
bt_7.grid(column=0, row=3, sticky="EW", padx=1, pady=0)
window.bind('7',  lambda event, item=7, btn=bt_7: change_col(item, btn))

bt_8 = Button(text="8", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=lambda: set_exp(value=8))
bt_8.grid(column=1, row=3, sticky="EW", padx=1, pady=0)
window.bind('8',  lambda event, item=8, btn=bt_8: change_col(item, btn))

bt_9 = Button(text="9", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=lambda: set_exp(value=9))
bt_9.grid(column=2, row=3, sticky="EW", padx=1, pady=0)
window.bind('9',  lambda event, item=9, btn=bt_9: change_col(item, btn))

bt_mult = Button(text="×", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=lambda: set_exp(value="×"))
bt_mult.grid(column=3, row=3, sticky="EW", padx=1, pady=0)
window.bind('*',  lambda event, item="×", btn=bt_mult: change_col(item, btn))




#---------------- DONE --------------------#
bt_4 = Button(text="4", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=lambda: set_exp(value=4))
bt_4.grid(column=0, row=4, sticky="EW", padx=1, pady=1)
window.bind('4',  lambda event, item=4, btn=bt_4: change_col(item, btn))

bt_5 = Button(text="5", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=lambda: set_exp(value=5))
bt_5.grid(column=1, row=4, sticky="EW", padx=1, pady=1)
window.bind('5',  lambda event, item=5, btn=bt_5: change_col(item, btn))

bt_6 = Button(text="6", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=lambda: set_exp(value=6))
bt_6.grid(column=2, row=4, sticky="EW", padx=1, pady=1)
window.bind('6',  lambda event, item=6, btn=bt_6: change_col(item, btn))

bt_sub = Button(text="-", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=lambda: set_exp(value="-"))
bt_sub.grid(column=3, row=4, sticky="EW", padx=1, pady=1)
window.bind('-',  lambda event, item="-", btn=bt_sub: change_col(item, btn))


#---------------- DONE --------------------#
bt_1 = Button(text="1", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=lambda: set_exp(value=1))
bt_1.grid(column=0, row=5, sticky="EW", padx=1, pady=1)
window.bind('1',  lambda event, item=1, btn=bt_1: change_col(item, btn))

bt_2 = Button(text="2", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=lambda: set_exp(value=2))
bt_2.grid(column=1, row=5, sticky="EW", padx=1, pady=1)
window.bind('2',  lambda event, item=2, btn=bt_2: change_col(item, btn))

bt_3 = Button(text="3", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=lambda: set_exp(value=3))
bt_3.grid(column=2, row=5, sticky="EW", padx=1, pady=1)
window.bind('3',  lambda event, item=3, btn=bt_3: change_col(item, btn))

bt_add = Button(text="+", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=lambda: set_exp(value="+"))
bt_add.grid(column=3, row=5, sticky="EW", padx=1, pady=1)
window.bind('+',  lambda event, item="+", btn=bt_add: change_col(item, btn))



bt_change_sign = Button(text="+/-", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=change_sign)
bt_change_sign.grid(column=0, row=6, sticky="EW", padx=1, pady=1)

bt_0 = Button(text="0", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=lambda: set_exp(value=0))
bt_0.grid(column=1, row=6, sticky="EW", padx=1, pady=1)
window.bind('0',  lambda event, item=0, btn=bt_0: change_col(item, btn))

bt_dot = Button(text=".", highlightthickness=0, height=3, borderwidth=0, fg='white',bg='#131313', font=("Arial", 12, "normal"), activebackground="#595959", activeforeground="white", command=lambda: set_exp(value="."))
bt_dot.grid(column=2, row=6, sticky="EW", padx=1, pady=1)
window.bind('.',  lambda event, item=".", btn=bt_dot: change_col(item, btn))

bt_equal = Button(text="=", highlightthickness=0, height=3, borderwidth=0, fg='white', bg='#04a4af', font=("Arial", 12, "normal"), activebackground="#05d2e1", activeforeground="white", command=calculate)
bt_equal.grid(column=3, row=6, sticky="EW", padx=1, pady=1)
window.bind('=',  calculate)
window.bind('<Return>',  lambda event, item="=", btn=bt_equal: change_col(item, btn))

window.mainloop()