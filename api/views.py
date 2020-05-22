from django.conf import settings
from firebase_admin import credentials, initialize_app

cred = credentials.Certificate(settings.GOOGLE_APPLICATION_CREDENTIALS)
db_app = initialize_app(cred, {'databaseURL': 'https://social-distancing-uts.firebaseio.com'}, name="db_app")
