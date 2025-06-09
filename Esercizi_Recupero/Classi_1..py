#Esercizio contatti telefonici

class ContactManager:

    def __init__(self):

        self.contacts:dict[str,list[str]] = {}

    def create_contact(name: str, phone_numbers: list[str]) -> dict[str, list[str]]:
        '''
        Qualcosa riguardo la funzione
        '''

        if name in self.contacts:

            raise ValueError("Errore, il contatto esiste già!") 
        
        else: 
            self.contacts[name] = phone_numbers

        return {name: phone_numbers}
    
    def add_phone_number(self, contact_name: str, phone_number: str) -> dict[str,list[str]]:

        if contact_name in self.contacts:

            if phone_number not in self.contacts[contact_name]:

                self.contacts[contact_name].append(phone_number)
            else:
                raise ValueError("Errore: il contatto già esiste!")
            
        else:
            raise ValueError("Errore: il contatto non è all'interno del dizionario!")
        
        def remove_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:

            if contact_name not in self.contacts:

                raise ValueError("Erorre: il contatto non è presente nel dizionario!")
            
            if phone_number not in self.contacts[contact_name]:

                raise ValueError("Errore: il numero di telefono non è presente!")
            
            self.comtacts[contact_name].remove(phone_number)

            return {contact_name: self.contacts[contact_name]}
        
        def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number:str) -> dict [str,list[str]]:

            if contact_name not in self.contacts:

                raise ValueError("Errore: ...!")

            if old_phone_number not in self.contacts[contact_name]:

                raise ValueError("Errore:....!")

            index: int = self.contacts[contact_name].index(old_phone_number)

            self.contacts[contact_name][index] = new_phone_number

            return {contact_name: self.contacts[contact_name]}

        def list_contacts(self) -> list[str]:

            return list(self.contacts.keys())

        def list_phone_numbers(self, contact_name: str) -> list[str]:

            if contact_name not in self.contacts:

                raise ValueError("Errore: ...!")

            return self.contacts[contact_name]

                    



        


