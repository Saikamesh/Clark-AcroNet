from django.db import IntegrityError
from django.shortcuts import render
from .models import Acronym, Suggestions, Users
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AcronymSerializer, SuggestionsSerializer, UsersSerializer
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

# Get all acronyms from the database
@api_view(["GET"])
def index(request):
    acronyms = Acronym.objects.all()
    serializer = AcronymSerializer(acronyms, many=True)
    return Response(serializer.data, status=200)

# Get all the suggestions from the database
@api_view(["GET"])
def get_suggestions(request):
    suggestions = Suggestions.objects.all()
    serializer = SuggestionsSerializer(suggestions, many=True)
    return Response(serializer.data, status=200)

# Search for a specific acronym in the database
@api_view(["GET"])
def acronyms_detail(request, name):
    try:
        acronym = Acronym.objects.get(acronym_name__iexact=name)
        serializer = AcronymSerializer(acronym, many=False)
        return Response(serializer.data)
    except Acronym.DoesNotExist:
        return Response({f"Acronym with name '{name}' does not exist."}, status=404)
        
# Add a new acronym to the database
@api_view(["POST"])
def add_acronym(request):
    acronym_name = request.data.get('acronym_name')
    if Acronym.objects.filter(acronym_name__iexact=acronym_name).exists():
        return Response({f"Acronym with name '{acronym_name}' already exists."}, status=400)
    serializer = AcronymSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(["POST"])
def give_suggestion(request):
    acronym_name = request.data.get('acronym_name')
    if Acronym.objects.filter(acronym_name__iexact=acronym_name).exists():
        return Response({f"Acronym with name '{acronym_name}' already exists."}, status=400)
    if Suggestions.objects.filter(acronym_name__iexact=acronym_name).exists():
        return Response({f"Acronym with name '{acronym_name}' already suggested and is being Reviewed."}, status=400)
    serializer = SuggestionsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(["PUT"])
def update_suggestion(request):
    try:
        acronym_name = request.data.get('acronym_name')
        suggested_acronym = Suggestions.objects.get(acronym_name__iexact=acronym_name)
        serializer = SuggestionsSerializer(suggested_acronym, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except Suggestions.DoesNotExist:
        return Response({f"Acronym with name '{acronym_name}' does not exist."}, status=404)

# Delete an existing suggested acronym from the database
@api_view(["DELETE"])
def delete_suggestion(request, acronym):
    try:
        acronym = Suggestions.objects.get(acronym_name__iexact=acronym)
        acronym.delete()
        suggestions = Suggestions.objects.all()
        serializeredUsers = SuggestionsSerializer(suggestions, many=True)
        return Response(serializeredUsers.data, status=201)
    except Acronym.DoesNotExist:
        return Response({f"Acronym with name '{acronym}' does not exist."}, status=404)

# Update an existing acronym in the database
@api_view(["PUT"])
def update_acronym(request):
    try:
        name = acronym_name = request.data.get('acronym_name')
        acronym = Acronym.objects.get(acronym_name__iexact=name)
        serializer = AcronymSerializer(acronym, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except Acronym.DoesNotExist:
        return Response({f"Acronym with name '{name}' does not exist."}, status=404)

# Delete an existing acronym from the database
@api_view(["DELETE"])
def delete_acronym(request, name):
    try:
        acronym = Acronym.objects.get(acronym_name__iexact=name)
        acronym.delete()
        acronyms = Acronym.objects.all()
        serializer = AcronymSerializer(acronyms, many=True)
        return Response(serializer.data, status=200)
    except Acronym.DoesNotExist:
        return Response({f"Acronym with name '{name}' does not exist."}, status=404)

@api_view(["POST"])
def user_signup(request):
    username = request.data.get('user_name')
    email = request.data.get('email')
    password = request.data.get('password')
    user_type = request.data.get('user_type')

    if not username or not email or not password or not user_type:
        return Response({"All fields are required."}, status=400)

    try:
        user = Users.objects.get(Q(user_name=username) | Q(email=email))
        return Response({"Username or email already exists."}, status=400)
    except Users.DoesNotExist:
        user = Users.objects.create(user_name=username, email=email, password=password, user_type = user_type)
        serializer = UsersSerializer(user)
        return Response(serializer.data, status=201)

@api_view(["GET"])
def get_all_users(request):
    try:
        users = Users.objects.all()
        serializeredUsers = UsersSerializer(users, many=True)
        return Response(serializeredUsers.data, status=201)
    except Users.DoesNotExist:
        return Response({"No users found."}, status=404)
    
# Delete an existing user from the database
@api_view(["DELETE"])
def delete_user(request, email):
    try:
        user = Users.objects.get(Q(email=email))
        user.delete()
        users = Users.objects.all()
        serializeredUsers = UsersSerializer(users, many=True)
        return Response(serializeredUsers.data, status=201)
    except Users.DoesNotExist:
        return Response({f"User with email '{email}' does not exist."}, status=404)
    
# Update an existing acronym in the database
@api_view(["PUT"])
def update_User(request):
    try:
        email = request.data.get('email')
        user = Users.objects.get(Q(email=email))
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except Acronym.DoesNotExist:
        return Response({f"Acronym with name '{email}' does not exist."}, status=404)

@api_view(["POST"])
def user_login(request):
    username = request.data.get("user_name")
    password = request.data.get("password")

    if not username or not password:
        return Response({"Both username and password are required."}, status=400)
    
    try:
        user = Users.objects.get(user_name=username , password=password)
        request.session['user_name'] = user.user_name
        request.session['user_id'] = user.id
        request.session['email'] = user.email
        request.session['is_logged_in'] = True
        return Response({
            "message": "You have been logged in.",
            "user_name": user.user_name,
            "user_id": user.id,
            "email": user.email,
            "user_type": user.user_type
        }, status=200)
    except Users.DoesNotExist:
        return Response({"Invalid credentials"}, status=400)


@api_view(["POST"])
def user_logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'user_name' in request.session:
        del request.session['user_name']
    if 'email' in request.session:
        del request.session['email']
    if 'is_logged_in' in request.session:
        del request.session['is_logged_in']
    logout(request)
    return Response({"message": "You have been logged out."}, status=200)