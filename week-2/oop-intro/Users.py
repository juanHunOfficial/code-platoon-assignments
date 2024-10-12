#profile have been made with _ because this is a private method
_user_db = {} #key: "id nummber" value: "name", "email", "license number"

class Users:
    
    def __init__(self, name: str, email: str, license_number: str) -> None:
        self._name = name
        self._email = email
        self._license_number = license_number
        
        unique_ID = (len(_user_db.keys()) + 1000)
        _user_db.update({unique_ID: [self._name, self._email, self._license_number]}) #updating the master list in the program using the key above
        print(f"Congradulations! Your account has been created, your ID number is: {unique_ID}")
        
    def _print_full_users_db(self):
        for key in _user_db:
            print(_user_db[key])
        
    def _update_user_email(self, id_number: int, new_email: str) -> None:
        _user_db[id_number][1] = new_email
        print(f"Done! Your email hase been updated to: {_user_db[id_number][1]}")

    def _update_user_name(self, id_number: str, new_name: str) -> None:
        _user_db[id_number][0] = new_name
        print(f"Done! Your name has been updated to: {_user_db[id_number][0]}")

# master_template = Users("Name", "template@code-platoon.com", "LXXX-XXX-XXX-XX-X")
# temp_user1 = Users("Juan Hun", "juan_hun@yahoo.com", "H500-555-555-55-5")
# temp_user2 = Users("Spongebob Squarepants", "bikini-bottom-chef@gmail.com", "H200-222-22-2")
# temp_user3 = Users("Patrick Theadore Star", "under-a-rock@yahoo.com", "H111-111-123-45-6")

# temp_user3._update_user_email(1003, "mayo_is_my_instrument@cheesecake.gov")
# temp_user1._update_user_name(1001, "Juan Pablo Hun")
# master_template._print_full_users_db()
