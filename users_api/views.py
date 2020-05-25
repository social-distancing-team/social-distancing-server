from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
import firebase_admin
from firebase_admin import firestore
from drf_firebase_auth.authentication import FirebaseAuthentication

db = firestore.client()

# Uncomment to require Authorization from Mobile App
# For server testing purposes leave commented
@api_view(['GET'])
@authentication_classes([FirebaseAuthentication])
def list_users(request):
    users_ref = db.collection(u'Users')
    docs = users_ref.stream()
    user_list = {}
    for doc in docs:
        user_list[doc.id] = doc.to_dict()
    return Response(user_list)

#@api_view(['PUT'])
#def users(request):
