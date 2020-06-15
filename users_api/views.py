from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from drf_firebase_auth.authentication import FirebaseAuthentication
from firebase_admin import firestore

db = firestore.client()

# Uncomment to require Authorization from Mobile App
# For server testing purposes leave commented
@api_view(['GET'])
@authentication_classes([FirebaseAuthentication])
def users_list(request):
    docs = db.collection(u'Users').stream()
    user_list = {}
    for doc in docs:
        user_list[doc.id] = doc.to_dict()
    return Response(user_list)

#@api_view(['PUT'])
#def users_(request):
