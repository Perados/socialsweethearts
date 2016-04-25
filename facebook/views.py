from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from annoying.functions import get_object_or_None
from social.apps.django_app.default.models import UserSocialAuth

from facebook.utils import load_signed_request
from socialsweethearts import settings

def login(request):
    facebook_social_auth = request.user.social_auth.get(provider='facebook') if hasattr(request.user, 'social_auth') else None
    return render_to_response('login.html', {'request': request, 'facebook_social_auth': facebook_social_auth })

@login_required()
def home(request):
    return render_to_response('home.html')

@csrf_exempt
def deauthorize(request):
    if request.method == 'POST':
        signed_request = request.POST.get('signed_request')
        data = load_signed_request(signed_request, settings.SOCIAL_AUTH_FACEBOOK_SECRET)
        user_id = data.get('user_id')
        social_user = get_object_or_None(UserSocialAuth, uid=user_id)
        social_user.user.is_active = False
        social_user.user.save()
        return HttpResponse(status=200)
    return HttpResponse(status=405)

def logout(request):
    auth_logout(request)
    return redirect('/')
