import requests
import json
################################################################################

def searchLists():

    # Call local API for lists
    response = requests.get("http://localhost:8000/query/lists/") # assuming server is run localhost
    listData = response.json()

    # For debugging purposes
    #print(listData)

    print("Lists available: \n")
    for key in listData:
        print(str(listData[key].get('Name')) + ' by ' + str(listData[key].get('Users')))
        print(str(listData[key].get('Items')) + '\n')



################################################################################

if __name__ == '__main__':

    try:
        searchLists()
    except KeyboardInterrupt:
        print('Cancelled')
        raise

