class SocialCause():
    def __init__(self, name: str, institution_name: str, adress: str, description: str):
        self.__name             = name
        self.__institution_name = institution_name
        self.__adress           = adress
        self.__description      = description

    # Getter functions
    def get_name(self) -> str:
        return self.__name
    
    def get_institution_name(self) -> str:
        return self.__institution_name
    
    def get_adress(self) -> str:
        return self.__adress
    
    def get_description(self) -> str:
        return self.__description
    
    # Setter functions
    def set_name(self, new_name: str):
        self.__name = new_name
    
    def set_institution_name(self, new_institution_name: str):
        self.__institution_name = new_institution_name

    def set_adress(self, new_adress: str):
        self.__adress = new_adress

    def set_description(self, new_description: str):
        self.__description = new_description

    def to_dict(self):
        return({'name':self.__name, 'institution_name':self.__institution_name, 'adress':self.__adress, 'description':self.__description})

    def __str__(self) -> str:
        print('Name=' + self.__name + ' Institution_name=' + self.__institution_name + 'Adress=' + self.__adress + 'Description=' + self.__description)