from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from drf_firebase_auth.authentication import FirebaseAuthentication
from firebase_admin import firestore 

db = firestore.client()

@api_view(['GET'])
#@authentication_classes([FirebaseAuthentication])
def query_users(request):
    docs = db.collection(u'Users').stream()
    users_list = {}
    for doc in docs:
        users_list[doc.id] = doc.to_dict()
    return Response(users_list)

@api_view(['GET'])
#@authentication_classes([FirebaseAuthentication])
def query_chats(request):
    docs = db.collection(u'Chats').stream()
    chats_list = {}
    for doc in docs:
        chats_list[doc.id] = doc.to_dict()
    return Response(chats_list)

@api_view(['GET'])
#@authentication_classes([FirebaseAuthentication])
def query_lists(request):
    docs = db.collection(u'Lists').stream()
    lists_list = {}
    for doc in docs:
        lists_list[doc.id] = doc.to_dict()
    return Response(lists_list)
