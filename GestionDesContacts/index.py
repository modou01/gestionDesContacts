import tkinter as tk
from tkinter import messagebox
import json

def ajouter_contact():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    numero = entry_numero.get()

    if nom and prenom and numero:
        contact = {"Nom": nom, "Prénom": prenom, "Numéro": numero}
        contacts_list.append(contact)
        sauvegarder_contacts()
        effacer_champs()
        update_contact_page()

def sauvegarder_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts_list, file)

def charger_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def effacer_champs():
    entry_nom.delete(0, tk.END)
    entry_prenom.delete(0, tk.END)
    entry_numero.delete(0, tk.END)

def selectionner_contact(event):
    selected_contact_index = contact_listbox.curselection()
    if selected_contact_index:
        index = selected_contact_index[0]
        contact = contacts_list[index]
        entry_nom.delete(0, tk.END)
        entry_nom.insert(0, contact['Nom'])
        entry_prenom.delete(0, tk.END)
        entry_prenom.insert(0, contact['Prénom'])
        entry_numero.delete(0, tk.END)
        entry_numero.insert(0, contact['Numéro'])

def supprimer_contact():
    selected_contact_index = contact_listbox.curselection()
    if selected_contact_index:
        index = selected_contact_index[0]
        contacts_list.pop(index)
        sauvegarder_contacts()
        effacer_champs()
        update_contact_page()

def update_contact_page():
    contact_listbox.delete(0, tk.END)
    for contact in contacts_list:
        contact_listbox.insert(tk.END, f"{contact['Nom']} {contact['Prénom']} {contact['Numéro']}")
        import tkinter as tk
import json

def ajouter_contact():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    numero = entry_numero.get()

    if nom and prenom and numero:
        contact = {"Nom": nom, "Prénom": prenom, "Numéro": numero}
        
        # Vérifier si le contact existe déjà dans la liste
        for idx, existing_contact in enumerate(contacts_list):
            if existing_contact["Nom"] == nom and existing_contact["Prénom"] == prenom:
                contacts_list[idx] = contact
                break
        else:
            contacts_list.append(contact)
        
        sauvegarder_contacts()
        effacer_champs()
        update_contact_page()

# ...

def selectionner_contact(event):
    selected_contact_index = contact_listbox.curselection()
    if selected_contact_index:
        index = selected_contact_index[0]
        contact = contacts_list[index]
        entry_nom.delete(0, tk.END)
        entry_nom.insert(0, contact['Nom'])
        entry_prenom.delete(0, tk.END)
        entry_prenom.insert(0, contact['Prénom'])
        entry_numero.delete(0, tk.END)
        entry_numero.insert(0, contact['Numéro'])

def update_contact_page():
    contact_listbox.delete(0, tk.END)
    for contact in contacts_list:
        contact_listbox.insert(tk.END, f"{contact['Nom']} {contact['Prénom']} {contact['Numéro']}")

# ...


root = tk.Tk()
root.title("Gestionnaire de Contacts")

contacts_list = charger_contacts()

frame_saisie = tk.Frame(root)
frame_saisie.pack()

label_nom = tk.Label(frame_saisie, text="Nom:")
label_nom.grid(row=0, column=0)
entry_nom = tk.Entry(frame_saisie)
entry_nom.grid(row=0, column=1)

label_prenom = tk.Label(frame_saisie, text="Prénom:")
label_prenom.grid(row=1, column=0)
entry_prenom = tk.Entry(frame_saisie)
entry_prenom.grid(row=1, column=1)

label_numero = tk.Label(frame_saisie, text="Numéro:")
label_numero.grid(row=2, column=0)
entry_numero = tk.Entry(frame_saisie)
entry_numero.grid(row=2, column=1)

ajouter_button = tk.Button(frame_saisie, text="Ajouter Contact", command=ajouter_contact)
ajouter_button.grid(row=3, column=0, columnspan=2)

frame_contacts = tk.Frame(root)
frame_contacts.pack()

contact_listbox = tk.Listbox(frame_contacts)
contact_listbox.pack()

contact_listbox.bind("<<ListboxSelect>>", selectionner_contact)

modifier_button = tk.Button(frame_contacts, text="Modifier Contact", command=ajouter_contact)
modifier_button.pack()

supprimer_button = tk.Button(frame_contacts, text="Supprimer Contact", command=supprimer_contact)
supprimer_button.pack()

update_contact_page()

root.mainloop()
