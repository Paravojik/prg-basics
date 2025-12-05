import contact_list
from contact import Contact

c1 = Contact("John Brown", "brown@onet.pl", "555234000")
c2 = Contact("Anna May", "am@o2.pl", "232000199")
c3 = Contact("George Small", "smallg@google.pl", "222999100")
c4 = Contact("Paola Big", "bigpaola@poczta.pl", "100200300")

my_contacts = contact_list.ContactList()
my_contacts.add_contact(c1)
my_contacts.add_contact(c2)
my_contacts.add_contact(c3)
my_contacts.add_contact(c4)


my_contacts.show_contacts()