class Volunteer():
    def __init__(self, name, surname: str, neighborhood: str, city: str):
        self.__name         = name
        self.__surname      = surname
        self.__neighborhood = neighborhood
        self.__city         = city

    # Getter functions
    def get_name(self) -> str:
        return self.__name
    
    def get_surname(self) -> str:
        return self.__surname
    
    def get_neighborhood(self) -> str:
        return self.__neighborhood
    
    def get_city(self) -> str:
        return self.__city
    
    # Setter functions
    def set_name(self, new_name: str):
        self.__name = new_name
    
    def set_surname(self, new_surname: str):
        self.__surname = new_surname

    def set_neighborhood(self, new_neighborhood: str):
        self.__neighborhood = new_neighborhood

    def set_city(self, new_city: str):
        self.__city = new_city

    def to_dict(self) -> str:
        return({'name':self.__name, 'surname':self.__surname, 'neighborhood':self.__neighborhood, 'city':self.__city})

    def __str__(self) -> str:
        print('Name=' + self.__name + ' Surname=' + self.__surname + 'Neighborhood=' + self.__neighborhood + 'City=' + self.__city)