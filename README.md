Documentație tema Python

Pentru a rezolva tema a utilizat Python 3.12.7 si Visual Studio Code
•	Prerequisites & run
Există mai multe moduri pentru a rula un fișier Python, în funcție de sistemul de operare folosit și mediul de lucru. Câteva dintre acestea ar fi:
	Din linia de comandă(Terminal sau Command Prompt)
Dacă folosim Windows, Mac sau Linux, trebuie să rulăm comenzi într-o aplicație numită Terminal (Command Prompt pe Windows).
1.	Deschidem Command Prompt(Windows)
2.	Scriem comanda: python –version
3.	Dacă primim un răspuns de tipul Python 3.x.x, atunci Python este instalat.
Dacă primim eroare, descarcăm și instalăm Python de pe python.org.
(Eu folosesc Python 3.12.7)
4.	Deschidem folder-ul în care am salvat fișierul Python:
De exemplu, unul dintre fișierele mele se numește tema1.py si este salvat în Desktop. Cu ajutorul comenzii cd Desktop, pot intra in folder-ul respectiv
( cd=change directory).
5.	Rulăm fișierul Python: python program.py
	Dintr-un editor de cod(IDE)
1.	În IDLE( editorul implicit instalat cu Python)
a)	Deschidem IDLE.
b)	Click pe File → Open și selectăm fișierul program.py.
c)	Apasăm F5 sau mergem la Run → Run Module pentru a rula fișierul.
2.	În VS Code:
a)	Descărcam VS Code
b)	Instalăm Python de pe python.org.
c)	Accesăm Extensions din VS Code și căutăm extensia Python(dezvoltată de Microsoft) și apăsăm pe INSTALL
d)	Deschidem fișierul Python pe care vrem să-l rulăm (File-Open File și selectăm fișierul)
e)	Configurăm interpretatorul Python (Ctrl+ Shift+P pt a deschide paleta de comenzi, selectăm Python: Select Interpreter și alegem versiunea Python pe care o avem instalată.)
f)	Pentru a rula fișierul
o	Din terminalul integrat, folosind comanda python nume_fisier.py
o	Folosind butonul de rulare (Run Python File)

•	Explicatie
	Exercițiul 2
o	Am instalat pandas si matplotlib, folosind in terminalul din VS Code, comenzile: pip install pandas, respectiv pip install matplotlib
o	Am inclus bibliotecile necesare(import pandas as pd; import matplotlib.pyplot as plt)
o	Am încărcat fișierul Excel file= r'C:\Users\pc\Desktop\pyth\data.xlsx' (file-variabilă care stochează valoarea atribuită; r-raw string  asigură că \ nu provoacă erori în interpretare.
o	Linia de cod data = pd.read_excel(file) este folosită pentru a citi date dintr-un fișier Excel în Python folosind biblioteca pandas.
o	Linia de cod durata = data['Durata'] este utilizată pentru a selecta o coloană dintr-un DataFrame pandas și a o atribui unei variabile. Similar si pentru celelalte coloane.
o	Linia de cod primele_5_valori_durata = durata[:5] este folosită pentru a selecta primele 5 valori din variabila durata. Similar și pentru celelalte variabile
o	Linia de cod ultimele_12_valori_durata = durata[-12:] este folosita pentru selectarea ultimelor 12 valori din variabila durata. Similar si pentru puls.
o	Linia de cod plt.figure(figsize=(10, 5)) este folosită în biblioteca Matplotlib pentru a crea o figură și a specifica dimensiunea acesteia.(“ 10” reprezintă latimea in inch, iar “5” reprezintă înălțimea figurii.
o	Linia de cod plt.plot(durata, label='Durata', marker='o', ms=10, color='green', mec='blue', mfc='blue') este utilizată pentru a desena un grafic în Matplotlib, adăugând diverse personalizări(functia plt.plot-trasează un graphic pe baza datelor furnizate; label-eticheta pentur grafic; marker-forma marker-ului; ms-marker size; color-culoarea liniei; mec-marker edge color-stabile;te culoarea conturului marker-ului; mfc-marker face color-stabileste culoarea interiorului marker-ului). Similar si pentru celelalte variabile.
o	Linia de cod plt.title()-nume graphic
o	Linia de cod plt.legend()-afiseaza legenda graficului
o	Linia de cod plt.grid() este utilizată pentru a afișa grila pe graficul desenat cu biblioteca Matplotlib.
o	Similar si pentru graficele pentru primele 5 valori, respective ultimele 12 valori
o	Linia de cod plt.show() pentru a afisa graficele

	Exercitiul 1
X=5
Y=12
o	Am creat o variabila mgr_count si am initializat-o cu 0 pentru a pastra numarul de obiecte create in clasa Manager
o	Am creat constructorul clasei Manager def __init__(self, name,salary, department) ( self-obiectul curent; name,salary,department-argumentele care vor fi transmise la crearea unui obiect al clasei Manager); 
department = f"F05 "Această linie suprascrie valoarea parametrului department cu  "F05".
 Manager.mgr_count += 1 La fiecare creare a unui obiect nou al clasei Manager, această variabilă este incrementată (+1), astfel numărând câte obiecte de tip Manager au fost create.
o	Am adaugat metoda ‘display_employee’ a.î. să afișeze doar departamentul angajatului. 
o	Metoda display_employee afișează valorile atributelor name, salary și department pentru un obiect creat dintr-o clasă.
o	Am creat 4 obiecte al clasei Manager 
o	Am apelat metoda display_employee pentru toate obiectele din clasa Manager
o	Am creat 4 obiecte ale clasei Employee
o	Am apelat metoda display_employee pentru toate obiectele din clasa Manager
o	Am afisat valorile inregistrate in variabilele mgr_count si empCount

•	Referinte bibliografice:
	https://www.w3schools.com/python/pandas/pandas_getting_started.asp
	https://www.w3schools.com/python/matplotlib_intro.asp
	https://www.w3schools.com/python/python_classes.asp
	https://www.geeksforgeeks.org/python-programming-language-tutorial/
	https://www.w3schools.com/git/default.asp
	https://chatgpt.com/share/6758a5de-7bcc-8002-a480-f983b2ff61fd



