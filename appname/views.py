from django.shortcuts import render
from django.http import JsonResponse
import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase once with your credentials and database URL
# cred = credentials.Certificate('projectname/firebaseConfig.json')
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://realtime-cnn-default-rtdb.asia-southeast1.firebasedatabase.app/'
# })
ref = db.reference('progress')

def chat(request):
    return render(request, 'chat.html')

def send_random_number(request):
    if request.method == 'POST':
        message = request.POST.get('message')

        if message == 'ok':
            # Generate a random number
            random_number = random.randint(1, 100)  # Change the range as needed

            # Send the random number to Firebase Realtime Database
            ref.set(random_number)

            return JsonResponse({'success': True, 'random_number': random_number})

    return JsonResponse({'success': False, 'error_message': 'Invalid request'})
