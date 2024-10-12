

class Users:
    
    def __init__(self, name, email, license_number):
        self._name = name
        self._email = email
        self._license_number = license_number
        
        self._user_db = {} #key: "name" value: "name", "email", "license_number"
        self._user_db.update({self._name: [self._name, self._email, self._license_number]})
        print(self._user_db)
        
temp_user1 = Users("Juan", "juan_hun@yahoo.com", "H500-555-555-55-5")
temp_user2 = Users("Alyssa", "alyssanickole97@gmail.com", "H200-222-22-2")