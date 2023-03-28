class Volunteer():
    def __init__(self, name, surname: str, neighborhood: str, city: str):
        self.name         = name
        self.surname      = surname
        self.neighborhood = neighborhood
        self.city         = city

    # Getter functions
    def get_name(self) -> str:
        return self.name
    
    def get_surname(self) -> str:
        return self.surname
    
    def get_neighborhood(self) -> str:
        return self.neighborhood
    
    def get_city(self) -> str:
        return self.city
    
    # Setter functions
    def set_name(self, new_name: str):
        self.name = new_name
    
    def set_surname(self, new_surname: str):
        self.surname = new_surname

    def set_neighborhood(self, new_neighborhood: str):
        self.neighborhood = new_neighborhood

    def set_city(self, new_city: str):
        self.city = new_city

    def __str__(self) -> str:
        print('Name=' + self.name + ' Surname=' + self.surname + 'Neighborhood=' + self.neighborhood + 'City=' + self.city)