class SocialCause():
    def __init__(self, name: str, institution_name: str, adress: str, description: str):
        self.name             = name
        self.institution_name = institution_name
        self.adress           = adress
        self.description      = description

    # Getter functions
    def get_name(self) -> str:
        return self.name
    
    def get_institution_name(self) -> str:
        return self.institution_name
    
    def get_adress(self) -> str:
        return self.adress
    
    def get_description(self) -> str:
        return self.description
    
    # Setter functions
    def set_name(self, new_name: str):
        self.name = new_name
    
    def set_institution_name(self, new_institution_name: str):
        self.institution_name = new_institution_name

    def set_adress(self, new_adress: str):
        self.adress = new_adress

    def set_description(self, new_description: str):
        self.description = new_description

    def __str__(self) -> str:
        print('Name=' + self.name + ' Institution_name=' + self.institution_name + 'Adress=' + self.adress + 'Description=' + self.description)