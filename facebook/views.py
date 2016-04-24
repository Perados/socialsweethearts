from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

def login(request):
    facebook_social_auth = request.user.social_auth.get(provider='facebook') if hasattr(request.user, 'social_auth') else None
    return render_to_response('login.html', {'request': request, 'facebook_social_auth': facebook_social_auth })

@login_required()
def home(request):
    return render_to_response('home.html')

def logout(request):
    auth_logout(request)
    return redirect('/')
