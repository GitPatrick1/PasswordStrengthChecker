import tkinter as tk
import re
from PIL import Image, ImageTk

# Funzione per verificare la forza della password
def check_password_strength():
    password = password_entry.get()  # Recupera la password inserita dall'utente
    if not password:
        result_label.config(text="Inserisci una password!", fg="red")
        return
    
    # Criteri
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    number_criteria = any(char.isdigit() for char in password)
    special_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Calcolo punteggio
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])

    # Determina la forza della password e il colore del messaggio
    if score == 5:
        result_label.config(text="Password Forte", fg="green")
    elif 3 <= score < 5:
        result_label.config(text="Password Moderata", fg="orange")
    else:
        result_label.config(text="Password Debole", fg="red")

# Funzione per mostrare/nascondere la password
def toggle_password_visibility():
    if password_entry.cget("show") == "*":  # Password nascosta
        password_entry.config(show="")
        eye_button.config(image=eye_open_image)
    else:  # Password visibile
        password_entry.config(show="*")
        eye_button.config(image=eye_closed_image)

# Configurazione della finestra principale
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x400")  # Dimensioni aggiornate per includere i bottoni e migliorare la visualizzazione

# Aggiungi immagine di sfondo
background_image = Image.open("sfondo_password1.jpg")  # Sostituisci con il tuo percorso per l'immagine
background_photo = ImageTk.PhotoImage(background_image)
root.bg_image = background_photo  # Conserva l'immagine per evitare che venga eliminata

# Applicazione dell'immagine di sfondo come etichetta
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Titolo in alto
title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 18, "bold"), bg="#b3e5fc")
title_label.pack(pady=20)

# Riquadro centrale
frame = tk.Frame(root, bg="white", padx=20, pady=20, relief="ridge", bd=2, highlightthickness=1, highlightbackground="black")  # Bordo nero attorno al rettangolo dell'input
frame.place(relx=0.5, rely=0.5, anchor="center")

# Etichetta istruzioni
instruction_label = tk.Label(frame, text="Inserisci la tua password:", font=("Arial", 12), bg="white")
instruction_label.pack(pady=5)

# Campo di input per la password
password_entry = tk.Entry(frame, show="*", font=("Arial", 14), width=30)
password_entry.pack(pady=10)

# Crea immagini per i bottoni di visibilità ridimensionate a 48x48 pixel
eye_closed_image = tk.PhotoImage(file="eye_closed.png")  # L'immagine ridimensionata a 48x48 pixel
eye_open_image = tk.PhotoImage(file="eye_open.png")  # L'immagine ridimensionata a 48x48 pixel

# Bottone per mostrare/nascondere la password accanto alla casella di input
button_width = 48  # Dimensioni fisse per i bottoni ridimensionati
button_height = 48  # Dimensioni fisse per i bottoni ridimensionati
eye_button = tk.Button(frame, image=eye_closed_image, command=toggle_password_visibility, width=button_width, height=button_height)
eye_button.pack(side="right", padx=5)

# Bottone di verifica
check_button = tk.Button(frame, text="Verifica", font=("Arial", 12), command=check_password_strength)
check_button.pack(pady=10)

# Etichetta per mostrare il risultato
result_label = tk.Label(frame, text="", font=("Arial", 14), bg="white")
result_label.pack(pady=10)

# Pulsante per uscire dal programma
exit_button = tk.Button(root, text="Esci", font=("Arial", 12), fg="red", command=root.destroy)
exit_button.pack(side="bottom", pady=20)

# Avvia l'interfaccia grafica
root.mainloop()
