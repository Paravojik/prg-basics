class ContactList:
    def __init__(self):
        self.contacts=[]
    
    def add_contact(self,contact):
        self.contacts.append(contact)
    
    def show_contacts(self):
        for contact in self.contacts:
            print(f"{contact.name:<20}  {contact.email:<30}  {contact.telephone:<15}  ")