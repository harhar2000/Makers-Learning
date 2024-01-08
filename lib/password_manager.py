# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#   4. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password


class PasswordManager():
    def __init__(self):
        self.passwords = {}

    def add(self, service_name, password):
        if len(password) >= 8 and any(char in password for char in '!@$%&'):
               self.passwords[service_name] = password

    def get_for_service(self, service_name):
        return self.passwords.get(service_name, None)

    def list_services(self):
        return list(self.passwords.keys())
    

password_manager = PasswordManager()
password_manager.add('gmail', '12ab5!678')   # Valid password
password_manager.add('facebook', '$abc1234') # Valid password
password_manager.add('twitter', '12345678')  # Invalid password, so ignored
print(password_manager.get_for_service('facebook'))
print(password_manager.get_for_service('not_real'))
print(password_manager.get_for_service('twitter'))
print(password_manager.list_services())
