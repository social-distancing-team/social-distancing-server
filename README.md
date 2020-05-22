# social-distancing-server  
The backend for the Social Distancing Mobile Application

## Install project requirements  
	python -m pip install -r requirements.txt

## Run Server  
	python .manage.py runserver 0.0.0.0:8000 

## The following is an example of an API endpoint that allows an authenticated user to get all users and their data  
	# Change to the root directory of the repository
	cd project/root/directory
	# Create a new app using the following
	django-admin startapp users_api

### Configuration of the app requires the following  
1. Adding the created app to the projects settings INSTALLED_APPS
2. Developing the functionality
3. Configuring the url routes

#### 1. Adding the created app to the projects settings INSTALLED_APPS  
	## social_distancing_server/settings.py
	# Add the following to INSTALLED_APPS
	INSTALLED_APPS = [
		'users_api.apps.UsersApiConfig',
	]

#### 2. Developing the functionality  
	## users_api/views.py
	from rest_framework.response import Response
	from rest_framework.decorators import api_view, authentication_classes
	import firebase_admin
	from firebase_admin import firestore
	from drf_firebase_auth.authentication import FirebaseAuthentication
	
	db = firestore.client()
	
	@api_view(['GET'])
	@authentication_classes([FirebaseAuthentication])
	def list(request):
		users_ref = db.collection(u'Users')
		docs = users_ref.stream()
		user_list = {}
		for doc in docs:
			user_list[doc.id] = doc.to_dict()
		return Response(user_list)

#### 3. Configuring the url routes  
1. Pointing the main urls to the created apps urls
2. Pointing the apps urls to individual functions found in views.py

##### 1. Pointing the main urls to the created apps urls  
	## api/urls.py
	from django.urls import path, include
	from . import views

	urlpatterns = [
		path('users/', include('users_api.urls'))
	]

##### 2. Pointing the apps urls to individual functions found in views.py  
	## users_api/urls.py
	from django.urls import path, include
	from . import views
	
	urlpatterns = [
		path('list/', views.list, name='api-users-list')
	]

