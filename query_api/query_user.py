import requests
import json
################################################################################

def searchUsers():

    # Call local API for users
    response = requests.get("http://localhost:8000/query/users/") # assuming server is run localhost
    userData = response.json()

    # For debugging purposes
    #print(userData)

    name = str(input('Enter name: '))
    print('Users found: \n')
    for key in userData:    
        if (userData[key]['FirstName'] == name or userData[key]['LastName'] == name):
            print(userData[key]['FirstName'] + ' ' + userData[key]['LastName'])

################################################################################

if __name__ == '__main__':

    try:
        searchUsers()
    except KeyboardInterrupt:
        print('Cancelled')
        raise

