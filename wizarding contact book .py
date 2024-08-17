#CLASS 1 
class magical_contact:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def set_email(self, email):
        self.email = email

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def describe(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone_number}"

#CLASS 2
class wizard_or_witch(magical_contact):
    def __init__(self, name, email, phone_number, wand, house):
        super().__init__(name, email, phone_number)
        self.wand = wand
        self.house = house

        if house not in {"Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"}:
            raise ValueError("Invalid")

    def get_wand(self):
        wand_length = self.wand.get('length', 'Unknown length')
        wand_wood = self.wand.get('wood', 'Unknown wood')
        wand_core = self.wand.get('core', 'Unknown core')
        return f"{wand_length}, {wand_wood}, {wand_core}"

    def get_house(self):
        return self.house

    def describe(self):
        basic_description = super().describe()
        wand_description = self.get_wand()
        return f"{basic_description}, Wand: {wand_description}, House: {self.house}"

#CLASS 3
class MagicalCreature(magical_contact):
    def __init__(self, name, email, phone_number, species, istame):
        super().__init__(name, email, phone_number)
        self.species = species
        self.istame = istame

    def get_species(self):
        return self.species

    def is_tame(self):
        return self.istame

    def describe(self):
        basic_description = super().describe()
        tame_status = "Tame" if self.istame else "Untame"
        return f"{basic_description}, Species: {self.species}, Tame: {tame_status}"

#CLASS 4 
class MagicalContactBook:
    def __init__(self):
        self.__contacts = []

    def add_contact(self, contact):
        if isinstance(contact, magical_contact):
            self.__contacts.append(contact)
        else:
            raise TypeError("Contact must be an instance of MagicalContact")

    def list_contacts(self):
        for contact in self.__contacts:
            print(contact.describe())

    def find_contact(self, name):
        for contact in self.__contacts:
            if contact.get_name() == name:
                return contact.describe()
        return "Contact not found"
