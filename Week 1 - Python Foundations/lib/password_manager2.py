# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None
#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#   3. Passwords must be unique (not reused in other services).

from datetime import datetime
class PasswordManager2():
    def __init__(self):
        self.passwords = {}
        self.added_on = {}

    def add(self, service_name, password):
        if len(password) >= 8 and any(char in password for char in '!@$%&') and password not in self.passwords.values():
            self.passwords[service_name] = password
            self.added_on[service_name] = datetime.now()
            
    def remove(self, service_name):
        self.passwords.pop(service_name, None)
        self.added_on.pop(service_name, None)

    def update(self, service_name, password):
        if len(password) >= 8 and any(char in password for char in '!@$%&') and password not in self.passwords.values():
            self.passwords.update({service_name: password})
            self.added_on[service_name] = datetime.now()
    
    def list_services(self):
        return list(self.passwords.keys())

    def sort_services_by(self, sort_by, reverse=False):
        if sort_by == 'service':
            return sorted(self.passwords.keys(), reverse=reverse)
        elif sort_by == 'added_on':
            return sorted(self.passwords.keys(), key=lambda k: self.added_on[k], reverse=reverse)


    def get_for_service(self, service_name):
        return self.passwords.get(service_name, None)


password_manager = PasswordManager2()
password_manager.add('gmail', '12ab5!678')   # Valid password
password_manager.add('facebook', '$abc1234') # Valid password
password_manager.add('youtube', '3@245256')  # Valid password
password_manager.add('twitter', '12345678')  # Invalid password, so ignored
print(password_manager.get_for_service('facebook')) #   '$abc1234'
print(password_manager.list_services())  #   ['gmail', 'facebook', 'youtube']
password_manager.remove('facebook')
print(password_manager.list_services()) #   ['gmail', 'youtube']
password_manager.update('gmail', '12345678')  # Invalid password, so ignored
print(password_manager.get_for_service('gmail')) #   '12ab5!678'
password_manager.update('gmail', '%21321415')  # Valid password
print(password_manager.get_for_service('gmail')) #   '%21321415'
print(password_manager.sort_services_by('service')) #   ['gmail', 'youtube']
print(password_manager.sort_services_by('added_on', reverse=False)) #   ['youtube', 'gmail']