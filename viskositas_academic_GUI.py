# packages imports
from tkinter import font
from tkinter.ttk import *
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil
import time
import csv
import webbrowser
import pickle
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# GUI base
nome, versao = 'Viskositas', 'Academic'
master = Tk()
fonte_padrao = font.nametofont('TkDefaultFont')
fonte_padrao.configure(family='Verdana')
fonte_menor = ('Verdana', 7)
master.title(f'{nome} {versao} ')
master.resizable(False, False)


# open file "viskositas_academic_pipeline.s" to standardize data
# and predict the viscosity of CaO-SiO₂-MgO-Al₂O₃-MnO-FeO-CaF₂-Na₂O systems
with open('viskositas_academic_pipeline.s', 'rb') as arquivo:
    va_model = pickle.load(arquivo)  # "viskositas_academic_model" == va_model


# class error about temperature
class TError(Exception):
    pass


# class error about the chemical composition
class CError(Exception):
    pass


# function to generate the "options" below
def menuu(titulo, altura, texto):
    master2 = Toplevel()
    master2.title(titulo)
    master2.resizable(0, 0)
    t = Text(master2, width=100, height=altura)
    t.pack()
    t.insert(END, texto)
    master2.mainloop()
    master2.quit()


# "References" option
references_texto = ('All references used in mathematical and computational modeling, database, data analysis,\n'
'computational model construction can be seen in:\n'
'\n'
'Duchesne, M., Bronsch, A., Hughes, R., Masset, P.\n'
'Fuel. p. 38-43, v. 114, 2013.\n'
'http://dx.doi.org/10.1016/j.fuel.2012.03.010\n'
'\n'
'Ziwei Chen, Minghao Wang, Zhao Meng, Hao Wang, Lili Liu, Xidong Wang.\n'
'Ceramics International. p. 30691-30701, v. 47, 2021.\n'
'https://doi.org/10.1016/j.ceramint.2021.07.248\n'
'\n'
'Anjos, Patrick Queiroz dos\n'
'Undergratuate Thesis. Ifes, Vitória, p. 51-52, 2021.\n'
'https://repositorio.ifes.edu.br/handle/123456789/1195')


def references():
    titulo=f'{nome} {versao} — References'
    menuu(titulo=titulo, altura=15, texto=references_texto)


# "How to use?" option
how_to_use_texto = ('The chemical composition must be entered in the respective fields together with the temperature,\n'
'with the unit of mass (SEE "Units" in the main menu). After entering the data, click on the\n'
'"<Calculate Viscosity>" button to predict the viscosity value of the introduced chemical system\n'
'at the chosen temperature.\n'
'\n'
'The execution time for predicting viscosity in the chosen system can be seen in "Time execution(s):"\n'
'at the top of the application where it denotes the execution time, in seconds, of the computational\n'
f'model in {nome}.\n'
'\n'
'All errors being related to the database used to build the neural network. The limits\n'
f'of {nome} is the chemical composition (by database), the temperature, which varies\n'
'between 682.95 and 2481.85°C and the viscosity, which varies between approximately -6.2146 and\n'
'18.420 (log η) (log = logₑ).\n'
'\n'
'To exit the application, click on the "Exit" menu and on the "Do you want to exit\n'
f'{nome} {versao}?" click "Yes". This way all windows will be closed automatically.\n'
'If not click "No" and keep enjoying!')


def how_to_use():
    titulo=f'{nome} {versao} — How to use? '
    menuu(titulo=titulo, altura=18, texto=how_to_use_texto)


# "About" option
about_texto = (f'{nome} {versao} is a neural network and has better efficiency when compared to\n'
'classic equations, neural networks in literature and other commercial software and uses the values\n'
'of chemical composition and temperature to predict the viscosity value of the chemical system at\n'
'the given temperature.')


def about():
    titulo=f'{nome} {versao} — About'
    menuu(titulo=titulo, altura=5, texto=about_texto)


# "Errors and Exceptions" option
erro_texto = ('Some errors have been programmed to be described in the viscosity (log η) field, to demonstrate\n'
'what kind of error and its probable cause. There are 4 errors:\n'
'- #COMP!, indicates an error in the introduction of the chemical composition of the slag to be\n'
'simulated, at a given temperature. Usually, the error is established when the sum of all components\n'
'equals ZERO or there are considerable variations between the contents within the chemical system to\n'
'be simulated, normally related to the insertion of contents deltas within the composition or\n'
'negative contents;\n'
f'- #TEMP!, dependent on the temperature values entered in {nome} {versao}. The error occurs when the\n'
'temperature entered is less than or equal to ZERO;\n'
'- #VALU!, results from the wrong placement of characters in the chemical composition and/or\n'
'temperature input fields. Common errors are correlated with the comma (,) introduced in the\n'
'contents of the chemical composition and the letter O (eng: ou) introduced instead of the number 0\n'
'(eng: zero);\n'
'- #TIME!, subject to the calculation of the viscosity prediction execution time. Occurs when there\n'
'is one error in the viscosity simulation or when the last viscosity value is an error.\n'
'\n'
'In addition to indicating common errors in the simulation in the viscosity field (log η), the\n'
'option File > Open denotes the description of the error in a message box, a Warning Message,\n'
f'resulting from the wrong choice of files to be placed in {nome} {versao}. The error is described as\n'
'"ERROR/EXCEPTION: X..." where X stands for the description of the error itself. Usually the error\n'
'or exception is attributed to:\n'
'- incorrect choice of files;\n'
'- use of special characters within the file or delimiters between data;\n'
'- absence of header or excess or missing limit of chemical elements in the file.\n'
'\n'
f'Some Exceptions were placed on {nome} {versao} to develop a high level and user-friendly experience.\n'
'Exceptions such as generating reports via File > Save in .xlsx, .docx, .ods formats or writing\n'
'erroneous characters and/or errors in .csv format, and indexing using Copy + Paste of\n'
f'external files for {nome} {versao} were introduced in the application.')


def erro():
    titulo=f'{nome} {versao} — Errors and Exceptions '
    menuu(titulo=titulo, altura=30, texto=erro_texto)


# "Contact" option
contact_texto = ('More information about the mathematical and computational modeling, construction of the\n'
'computational model, CUSTOMIZATION of the GUI and FULL VERSION access of Viskositas,\n'
'or any errors:\n'
'\n'
'Site: https://www.patrickdosanjos.com/\n'
'E-mail: patrick.dosanjos@outlook.com\n'
'Linkedin: https://www.linkedin.com/in/patrick-queiroz-dos-anjos/\n'
'GitHub: https://github.com/patrick21081995')


def contact():
    titulo=f'{nome} {versao} — Contact'
    menuu(titulo=titulo, altura=9, texto=contact_texto)


# main table generator
def tabela(parente, linha, coluna, w):
    tabela = []
    for r in range(linha):
        row = []
        for c in range(coluna):
            var = StringVar()
            entry = Entry(parente, textvar=var, width=w, justify='center', font=fonte_menor)
            entry.grid(row=r+1, column=c)
            row.append(var)
        tabela.append(row)
    return tabela


# Frame to introduce the main table
l1 = LabelFrame(master)
l1.grid(row=1, column=0, columnspan=2, padx=5, pady=(0,5), ipadx=2, ipady=2)
linhas, colunas = 10, 10
table = tabela(l1, linhas, colunas, 8)


# generator event for secundary menu "Edit" 
def paste(event):
    try:
        rows = master.clipboard_get().split('\n')
        for r, row in enumerate(rows):
            values = row.split('\t')
            for c, value in enumerate(values):
                table[r][c].set(value)
    except IndexError:
        pass


# event "Paste"
def colar():
    paste(True)


# event "Delete"
def deletar():
    for i in range(0, linhas):
        for j in range(0, colunas):
            table[i][j].set('')
    entry.delete(0, END)


# function to get numerical value of table
def get(alface):
    return alface.get()


# event "Copy"
def copiar():
    for i in range(0, linhas):
        for j in range(0, colunas):
            if table[i][j].get() == '':
                table[i][j].set(0.0)

    master.clipboard_clear()
    for i in range(0, linhas):
        try:
            if i == 0:
                pass
            else:
                master.clipboard_append('\n')
            if sum(list(map(float, (map(get, table[i][0:len(table[i])-1]))))) == 0:
                continue
            else:
                for j in range(0, colunas):
                    master.clipboard_append(table[i][j].get() + '\t')
        except ValueError:
            for j in range(0, colunas):
                master.clipboard_append(table[i][j].get() + '\t')
    master.clipboard_append('\n')

    for i in range(0, linhas):
        for j in range(0, colunas):
            if table[i][j].get() == '0.0':
                table[i][j].set('')


# event "Cut"
def cortar():
    copiar(); deletar()


# bind the function 
master.bind('<<Paste>>', paste)


# open .csv file to the application 
def abrir():
    try:
        arquivo = filedialog.askopenfilename(title=f'{nome} {versao} — Open .csv file ',
        filetypes=[('CSV file', '*.csv'),
        ('All files', '*')])

        lista_a = []
        with open(arquivo, 'r', newline='') as csv_arquivo:
            csv_arquivo.readline()
            arquivo = csv.reader(csv_arquivo, delimiter=',')
            for linha in arquivo:
                lista_a += [[linha[0], linha[1], linha[2], linha[3], linha[4], linha[5],
                linha[6], linha[7], linha[8]]]

        for m in range(len(lista_a)):
            for o in range(len(lista_a[0])):
                table[m][o].set(lista_a[m][o])

    except FileNotFoundError:
        pass

    except (IndexError, UnicodeDecodeError) as erro:
        titulo = f'{nome} {versao} — Open .csv file '
        mensagem2 = f'ERROR/EXCEPTION (TYPE): {erro} ({type(erro)}).'
        messagebox.showerror(titulo, mensagem2)


# save and generate a report (.csv file) of Viskositas Academic predictions
def salvar():
    try:
        lista_s = []

        for i in range(0, linhas):
            for j in range(0, colunas):
                if table[i][j].get() == '':
                    table[i][j].set(0.0)

        lista_l = []
        i = 1
        for linha in table:
            try:
                lista_l = [i, linha[0].get(), linha[1].get(), linha[2].get(), linha[3].get(), linha[4].get(), linha[5].get(),
                linha[6].get(), linha[7].get(), linha[8].get(), linha[9].get()]
                if sum(map(float, lista_l[1: 10])) == 0.0:
                    pass
                else:
                    lista_s += [lista_l]
                i += 1
            except ValueError:
                lista_s += [lista_l]
                i += 1

        for i in range(0, linhas):
            for j in range(0, colunas):
                if table[i][j].get() == '0.0':
                    table[i][j].set('')

        arquivo = filedialog.asksaveasfilename(title=f'{nome} {versao} — Save .csv file ',
        filetypes=[('CSV file', '*.csv'),
        ('All files', '*')], defaultextension='.csv')

        with open(arquivo, 'w', newline='') as csv_arquivo:
            arquivo = csv.writer(csv_arquivo, delimiter=',')
            arquivo.writerow(['ID', 'CaO(%mass)', 'SiO2', 'MgO', 'Al2O3', 'MnO',
            'FeO', 'CaF2', 'Na2O', 'T(degrees Celsius)', 'log n(n - Pa.s)'])

            for i in range(0, len(lista_s)):
                arquivo.writerow(lista_s[i])

    except FileNotFoundError:
        pass

    except IndexError:
        pass

    except UnicodeDecodeError:
        pass


# neural network to predict the viscosity
def rede():
    for i in range(0, linhas):
        for j in range(0, colunas):
            if table[i][j].get() == '':
                table[i][j].set(0.0)

    antes = time.time()

    for ii in range(0, linhas):
        try:
            lista = [table[ii][0].get(), table[ii][1].get(), table[ii][2].get(), table[ii][3].get(),
            table[ii][4].get(), table[ii][5].get(), table[ii][6].get(), table[ii][7].get(),
            table[ii][8].get()]
            lista[4:4] = [0.0]
            lista[9:9] = [0.0]*10

            lista = list(map(float, lista[0:len(lista)]))

            if sum(lista)==0.0 and table[ii][9].get()=='0.0':
                continue

            if sum(lista[0:len(lista)-1])==0.0 and int(lista[-1])!=0.0:
                raise CError

            lista[-1] += 273.15
            viscosidad = va_model.predict([lista])

            if float(table[ii][8].get()) <= 0.0:
                raise TError
            else:
                table[ii][9].set(viscosidad[0].round(decimals=4))

            entry.delete(0, END)
            entry.insert(0, round(time.time()-antes, 6))

        except TError:
            table[ii][9].set('#TEMP!')
            entry.delete(0, END)
            entry.insert(0, '#TIME!')

        except CError:
            table[ii][9].set('#COMP!')
            entry.delete(0, END)
            entry.insert(0, '#TIME!')

        except ValueError:
            table[ii][9].set('#VALU!')
            entry.delete(0, END)
            entry.insert(0, '#TIME!')

    for i in range(0, linhas):
        for j in range(0, colunas):
            if table[i][j].get() == '0.0':
                table[i][j].set('')


# Multi-Viskositas message
def rede_multi():
    titulo = f'{nome} {versao} — Multi-Viskositas '
    mensagem = ('Multi-Viskositas (predict the viscosity of thousands/millions '
    'chemical compositions at specified temperatures) is not available in Academic version. '
    'Please, see Viskositas Project and notify the administrator (see "Contact").')
    messagebox.showwarning(titulo, mensagem)


# labels
parente = l1
Label(parente, text='CaO').grid(row=0, column=0)
Label(parente, text='SiO₂').grid(row=0, column=1)
Label(parente, text='MgO').grid(row=0, column=2)
Label(parente, text='Al₂O₃').grid(row=0, column=3)
Label(parente, text='MnO').grid(row=0, column=4)
Label(parente, text='FeO').grid(row=0, column=5)
Label(parente, text='CaF₂').grid(row=0, column=6)
Label(parente, text='Na₂O').grid(row=0, column=7)
Label(parente, text='T').grid(row=0, column=8)
Label(parente, text='log η').grid(row=0, column=9)

# "Time window"
l2 = LabelFrame(master)
l2.grid(row=0, column=1, sticky='e', padx=5, pady=5)
entry = Entry(l2, justify='center', width=20)
entry.grid(row=1, column=1, pady=5, padx=(0,10))
text_l2 = Label(l2, text='Time execution (s): ')
text_l2.grid(row=1, column=0)

# button to predict the viscosity
botao = Button(master, text=' <Calculate Viscosity> ', width=20, height=1,
background='azure', border=2, command=rede)
botao.grid(row=0, column=0, sticky='w', padx=5, pady=5)

# main menu 
menubar = Menu(master)

# secundary menu "File"
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Open ', command=abrir)
filemenu.add_command(label='Save ', command=salvar)
menubar.add_cascade(label='File ', menu=filemenu)

# secundary menu "Edit"
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label='Cut ', command=cortar)
editmenu.add_command(label='Copy ', command=copiar)
editmenu.add_command(label='Paste ', command=colar)
editmenu.add_command(label='Delete ', command=deletar)
menubar.add_cascade(label='Edit ', menu=editmenu)

# secundary menu "Units"
optionsmenu = Menu(menubar, tearoff=0)
optionsmenu_3 = Menu(optionsmenu, tearoff=0)
optionsmenu_3.add_command(label='%mass ')
optionsmenu_4 = Menu(optionsmenu, tearoff=0)
optionsmenu_4.add_command(label='°C ')
optionsmenu_5 = Menu(optionsmenu, tearoff=0)
optionsmenu_5.add_command(label='Pa.s ')
optionsmenu.add_cascade(label='Composition ', menu=optionsmenu_3)
optionsmenu.add_cascade(label='Temperature (T) ', menu=optionsmenu_4)
optionsmenu.add_cascade(label='Viscosity (η) ', menu=optionsmenu_5)
menubar.add_cascade(label='Units ', menu=optionsmenu)


# function to download the base_file_viskositas_academic.csv
# IF the file is in the same directory of viskositas_academic_GUI.py
def base():
    try:
        target = filedialog.asksaveasfilename(title=f'{nome} {versao} — Base file (.csv) ',
        filetypes=[('CSV file', '*.csv'),
        ('All files', '*')], defaultextension='.csv')
        shutil.copy2(os.path.dirname(os.path.realpath(__file__)) + "\\base_file_viskositas_academic.csv", target)
    except FileNotFoundError:
        pass


# function to visualize the project (web)
def projeto():
    webbrowser.open('https://github.com/patrick21081995/Viskositas_Academic')


# function to visualize the project license (web)
def licenca():
    webbrowser.open('https://github.com/patrick21081995/Viskositas_Academic/blob/main/LICENSE')


# function to visualize the Viskositas project (web)
def v_project():
    webbrowser.open('https://github.com/patrick21081995/VISKOSITAS')


# secundary menu "Help"
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label=f'How to use {nome} {versao}? ', command=how_to_use)
helpmenu.add_command(label='About ', command=about)
helpmenu.add_command(label='Contact ', command=contact)
helpmenu.add_command(label='Base file (.csv) ', command=base)
helpmenu.add_command(label='Erros and Exceptions ', command=erro)
helpmenu.add_separator()
helpmenu.add_command(label='References ', command=references)
helpmenu.add_separator()
helpmenu.add_command(label='Project ', command=projeto)
helpmenu.add_command(label='License ', command=licenca)
helpmenu.add_command(label='Viskositas Project ', command=v_project)
menubar.add_cascade(label='Help ', menu=helpmenu)

# secundary menu "Multi-Viskositas"
menubar.add_separator()
menubar.add_cascade(label='Multi-Viskositas ', command=rede_multi) 
menubar.add_separator()

# secundary menu "Exit"
exitmenu = Menu(menubar, tearoff=0)
exitmenu_2 = Menu(exitmenu, tearoff=0)
exitmenu_2.add_command(label='Yes ', command=master.quit)
exitmenu_2.add_command(label='No ')
exitmenu.add_cascade(label=f'Do you want to exit {nome} {versao}? ', menu=exitmenu_2)
menubar.add_cascade(label='Exit ', menu=exitmenu)

# configure the main menu 
master.config(menu=menubar)

# app inicialization 
master.mainloop()
