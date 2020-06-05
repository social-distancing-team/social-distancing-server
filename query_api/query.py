import requests
import json
import argparse
import sys
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

    parser = argparse.ArgumentParser()
    parser.add_argument('query_type', help='Type of query requested: user, list')

    # Get and check options
    args = None

    if(len(sys.argv) == 1):
        parser.print_help()
        sys.exit(0)
    elif(sys.argv[1] == '-h' or \
         sys.argv[1] == '--h' or \
         sys.argv[1] == '-help' or \
         sys.argv[1] == '--help'):
         parser.print_help()
         sys.exit(0)
    else:
        args = parser.parse_args()
        print("Query type: ")
        print(args.query_type)

    try:
        if(args.query_type == 'user'):
            searchUsers()
        elif(args.query_type == 'list'):
            searchLists()
    except KeyboardInterrupt:
        print('Cancelled')
        raise

