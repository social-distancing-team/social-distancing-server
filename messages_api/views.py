from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
import firebase_admin
from firebase_admin import firestore
from drf_firebase_auth.authentication import FirebaseAuthentication

db = firestore.client()

# Uncomment to require Authorization from Mobile App
# For server testing purposes leave commented
#@authentication_classes([FirebaseAuthentication])
@api_view(['GET'])
def list_messages(request):
    messages_ref = db.collection(u'Messages')
    docs = messages_ref.stream()
    message_list = {}
    for doc in docs:
        message_list[doc.id] = doc.to_dict()
    return Response(message_list)

#@api_view(['PUT'])
#def users(request):
