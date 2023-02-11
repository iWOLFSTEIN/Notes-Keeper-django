from .models import Note
from .serialize import *
from .models import *
import jwt
from rest_framework.response import Response
from notes_keeper import settings
from functools import wraps
from django.contrib.auth import authenticate


def verifyJwtToken(func):
    @wraps(func)
    def decorator(request):
        token = str(request.auth)
        try:
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
            user = CustomUser.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()
            return func(request, user)
        except jwt.ExpiredSignatureError as e:
            return Response({'error': 'Activations link expired'}, status=400)
        except jwt.exceptions.DecodeError as e:
            return Response({'error': 'Invalid Token'}, status=400)
    return decorator


def getAllTheNotesTableRow():
    rows = Note.objects.all()
    '''
    converts the Note class into json format
    '''
    serialized_rows = NoteSerializer(rows, many = True)
    return Response(serialized_rows.data)


@verifyJwtToken
def insertRowInNotesTable(request, user):
    serialized_note = NoteSerializer(data= request.data) 
    if serialized_note.is_valid():
        serialized_note.save(foreign_key=user)
        return Response(serialized_note.data)
    else:
        return Response({'error': 'invalid request'}, 400)
    

@verifyJwtToken
def getSingleNotesTableRow(request, user):
    name = request.query_params.get("name")
    rows = (Note.objects.filter(foreign_key = user) & Note.objects.filter(name__startswith= name))
    response = []
    for row in rows:
        serialized_note = NoteSerializer(row).data
        response.append(serialized_note)

    return Response(response)


@verifyJwtToken
def updateNotesTableRow(request, user):
    name = request.query_params.get("name")
    payload = request.POST.dict()
    row = Note.objects.get(name=name)
    row.name = name
    row.description = payload['description']
    row.save()
    return Response({'successful': True})


@verifyJwtToken
def deleteNotesTableRow(request, user):
    name = request.query_params.get("name")
    row = Note.objects.get(name=name)
    data = row.delete()
    print(data)
    return Response({'successful': True})


def deleteAllTheNotesTableRows():
    rows = Note.objects.all().delete()
    return Response({'successful': True})


from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def registerUser(request):
    serialized_user = UserSerializer(data=request.data)
    
    if serialized_user.is_valid():
        user = serialized_user.save()
        return Response(get_tokens_for_user(user))
    else:
        return Response({'error': 'invalid request'}, 400)
    


def loginUser(request):
    user = authenticate(email=request.data['email'],password=request.data['password'])
    print(user)
    if user is not None:
        print('user exist')
    return Response({})