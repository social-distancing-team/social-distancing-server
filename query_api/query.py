import requests
import json
################################################################################

def searchUsers():

    # Call local API for users
    response = requests.get("http://localhost:8000/query/users/")
    data = response.json()

    # For debugging purposes
    #print(data)

    name = str(input('Enter name: '))
    for key in data:    
        if (data[key]['FirstName'] == name or data[key]['LastName'] == name):
            print(data[key]['FirstName'] + ' ' + data[key]['LastName'])

################################################################################

if __name__ == '__main__':

    try:
        searchUsers()
    except KeyboardInterrupt:
        print('Cancelled')
        raise

