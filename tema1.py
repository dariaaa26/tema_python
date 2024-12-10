import pandas as pd
import matplotlib.pyplot as plt

file=r'C:\Users\pc\Desktop\pyth\data.xlsx' 
data = pd.read_excel(file)

durata = data['Durata']
puls = data['Puls']
max_puls=data['MaxPuls']
calorii=data['Calorii']

primele_5_valori_durata = durata[:5]
primele_5_valori_puls = puls[:5]
primele_5_valori_max_puls=max_puls[:5]
primele_5_valori_calorii=calorii[:5]

ultimele_12_valori_durata = durata[-12:]
ultimele_12_valori_puls = puls[-12:]

plt.figure(figsize=(10, 5))
plt.plot(durata, label='Durata', marker='o', ms=10, color='green', mec='blue', mfc='blue')
plt.plot(puls, label='Puls', marker='x', ms=10, color='yellow', mec='orange', mfc='orange')
plt.plot(max_puls, label='Max_puls', marker='*', ms=10, color='pink', mec='purple', mfc='purple')
plt.plot(calorii, label='Calorii', marker='+', ms=10,color='red', mec='black', mfc='black')
 
plt.title('Toate valorile')
plt.legend()
plt.grid()

plt.figure(figsize=(10, 5))
plt.plot(primele_5_valori_durata, label='Durata', marker='o', color='green', mec='blue', mfc='blue')
plt.plot(primele_5_valori_puls, label='Puls', marker='x', color='yellow', mec='orange', mfc='orange')
plt.plot(primele_5_valori_max_puls, label='Max_Puls', marker='*', color='pink', mec='purple', mfc='purple')
plt.plot(primele_5_valori_calorii, label='Calorii', marker='+', color='red', mec='black', mfc='black')
plt.title(f'Primele {5} valori')
plt.legend()
plt.grid()

plt.figure(figsize=(10, 5))
plt.plot(ultimele_12_valori_durata, label='Durata', marker='o', color='purple', mec='black', mfc='black')
plt.plot(ultimele_12_valori_puls, label='Puls', marker='x', color='pink', mec='red', mfc='red')
plt.title(f'Ultimele {12} valori')
plt.legend()
plt.grid()

plt.show()
