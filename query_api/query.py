import requests
import json
import argparse
import sys
import csv
################################################################################

def tsvOutput(table):
    with open(args.tsv_output,'w') as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        for row in table:
            tsv_output.writerow(row)
    print('Query printed to ' + args.tsv_output + ' successfully.')

################################################################################

def searchUsers():

    tempTable = []

    # Call local API for users
    response = requests.get("http://localhost:8000/query/users/") # assuming server is run localhost
    print("Connected to API.")
    userData = response.json()

    # For debugging purposes
    #print(userData)

    name = str(input('Enter name: '))
    print('Users found: \n')
    for key in userData:    
        if (userData[key]['FirstName'] == name or userData[key]['LastName'] == name):
            print(userData[key]['FirstName'] + ' ' + userData[key]['LastName'])
            rows = [userData[key]['FirstName'], userData[key]['LastName']]
            tempTable.append(rows)
    tsvOutput(tempTable)

################################################################################
def searchLists():

    tempTable = []

    # Call local API for lists
    response = requests.get("http://localhost:8000/query/lists/") # assuming server is run localhost
    print("Connected to API.")
    listData = response.json()

    # For debugging purposes
    #print(listData)

    print("Lists available: \n")
    for key in listData:
        print(str(listData[key].get('Name')) + ' by ' + str(listData[key].get('Users')))
        print(str(listData[key].get('Items')) + '\n')
        rows = [listData[key].get('Items')]
        tempTable.append(rows)
    tsvOutput(tempTable)

################################################################################        

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('query_type', help='Type of query requested: user, list')
    parser.add_argument('--tsv_output', type=str, default='out.tsv', help='tsv output for query')

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

