# Inizializzazione delle variabili
t_max:float = float('-inf')
day_max:int = 0
t_min:float = float('inf')
day_min:int = 0
cont_norma:int = 0
t_media:float = 0

# Ciclo per 7 giorni
for i in range(1,8):
  temp:float = float(input(f"Inserisci la temperatura per il giorno {i}: "))
  t_media += temp
  
  # Verifica temperatura massima
  if temp > t_max:
    t_max = temp
    day_max = i
  # Verifica temperatura minima
  elif temp < t_min:
    t_min = temp
    day_min = i
    
  
  # Controllo temperatura nella norma
  if 10 <= temp <= 30:
    cont_norma += 1
    if cont_norma == 7:
      print("Temperature nella norma")
  # Controllo allerta temperatura
  elif temp < 5 or temp > 35:
    print("Allerta temperatura")

# Calcolo media settimanale
t_media = t_media / 7

# Output dei risultati
print(f"Temperatura media: {t_media}")
print(f"Temperatura massima: {t_max} registrata il giorno {day_max}")
print(f"Temperatura minima: {t_min} registrata il giorno {day_min}")