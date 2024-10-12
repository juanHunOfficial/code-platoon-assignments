#profile have been made with _ because this is a private method
_user_db = {} #key: "name" value: "name", "email", "license_number"

class Users:
    
    def __init__(self, name: str, email: str, license_number: str) -> None:
        self._name = name
        self._email = email
        self._license_number = license_number
        _user_db.update({self._name: [self._name, self._email, self._license_number]}) #updating the master list in the program using the key above
        
    def _print_full_users_db(self):
        print(_user_db)
        
    def _update_user_email(self, name: str, new_email: str) -> None:
        _user_db[name][1] = new_email
        print("")

    def _update_user_name(self, name: str, new_name: str) -> None:


master_template = Users("Name", "template@code-platoon.com", "LXXX-XXX-XXX-XX-X")
temp_user1 = Users("Juan Hun", "juan_hun@yahoo.com", "H500-555-555-55-5")
temp_user2 = Users("Spongebob Squarepants", "bikini-bottom-chef@gmail.com", "H200-222-22-2")
temp_user3 = Users("Patrick Theadore Star", "under-a-rock@yahoo.com", "H111-111-123-45-6")

temp_user3._update_user_email("Patrick Theadore Star", "mayo_is_my_instrument@cheesecake.gov")
master_template._print_full_users_db()