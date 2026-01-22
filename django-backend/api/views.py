import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from api.models import Profile


# @csrf_exempt
def signup(request): # this is the signup creating account
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    data = json.loads(request.body)

    username = data.get("username")
    password = data.get("password")
    email = data.get("email", "")

    if not username or not password:
        return JsonResponse({"error": "missing fields"}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "user exists"}, status=400)

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
    )

    Profile.objects.create(
        user=user,
        first_name="",
        last_name="",
        bio=""
    )

    login(request, user)

    return JsonResponse(
        {"id": user.id, "username": user.username},
        status=201
    )


# @csrf_exempt
def login_view(request): # this will be used to login (not setup currently)
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    data = json.loads(request.body)

    user = authenticate(
        username=data.get("username"),
        password=data.get("password"),
    )

    if not user:
        return JsonResponse({"error": "invalid credentials"}, status=401)

    login(request, user)

    return JsonResponse({"ok": True})


def me(request): # this is used in the auth when loading the page
    if not request.user.is_authenticated:
        return JsonResponse({"error": "unauthorized"}, status=401)
    
    profile = Profile.objects.get(user=request.user)
    
    return JsonResponse({
        "id": request.user.id,
        "username": request.user.username,
        "first_name": profile.first_name,
        "last_name": profile.last_name,
        "bio": profile.bio,
    })


@require_http_methods(["GET"])
def get_profile(request): # this is used to get the profile information
    if not request.user.is_authenticated:
        return JsonResponse({"error": "unauthenticated"}, status=401)
    
    profile = Profile.objects.get(user=request.user)

    return JsonResponse({
        "first_name": profile.first_name,
        "last_name": profile.last_name,
        "bio": profile.bio,
    })

@require_http_methods(["POST"])
def update_profile(request): # this is used to update the profile
    if not request.user.is_authenticated:
        return JsonResponse({"error": "unauthenticated"}, status=401)
    
    data = json.loads(request.body)

    profile = Profile.objects.get(user=request.user)

    profile.first_name = data.get("first_name", "")
    profile.last_name = data.get("last_name", "")
    profile.bio = data.get("bio", "")[:256]

    profile.save()

    return JsonResponse({"ok": True})

@require_http_methods(["POST"])
def logout_view(request):
    logout(request)
    return JsonResponse({"ok": True})