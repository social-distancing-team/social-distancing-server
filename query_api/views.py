from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
import firebase_admin
from firebase_admin import firestore
from drf_firebase_auth.authentication import FirebaseAuthentication

db = firestore.client()

#authentication_classes commented for testing, uncomment to allow authorisation

@api_view(['GET'])
#@authentication_classes([FirebaseAuthentication])
# users API call
def list_users(request): 

    docs = db.collection(u'Users').stream()
    users_list = {}
    for doc in docs:
        users_list[doc.id] = doc.to_dict()
    return Response(users_list)

@api_view(['GET'])
#@authentication_classes([FirebaseAuthentication])
# chats API call
def list_chats(request):
    
    docs = db.collection(u'Chats').stream()
    chats_list = {}
    for doc in docs:
        chats_list[doc.id] = doc.to_dict()
    return Response(chats_list)

@api_view(['GET'])
#@authentication_classes([FirebaseAuthentication])
# lists API call
def list_lists(request):
    
    docs = db.collection(u'Lists').stream()
    lists_list = {}
    for doc in docs:
        lists_list[doc.id] = doc.to_dict()
    return Response(lists_list)