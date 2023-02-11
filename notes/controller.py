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



@verifyJwtToken
def getAllTheNotesTableRow(request, user):
    rows = Note.objects.filter(foreign_key = user)
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
    id = request.query_params.get("id")
    try:
        row = Note.objects.get(id=id, foreign_key = user)
    except:
        return Response({'error': 'note does not exist'}, 400)
    return Response(NoteSerializer(row).data)


@verifyJwtToken
def updateNotesTableRow(request, user):
    id = request.query_params.get("id")
    payload = request.POST.dict()
    try:
         row = Note.objects.get(id=id, foreign_key = user)
    except:
        return Response({'error': 'note does not exist'}, 400)
    
    row.name = payload['name']
    row.description = payload['description']
    row.save()
    return Response({'successful': True})


@verifyJwtToken
def deleteNotesTableRow(request, user):
    id = request.query_params.get("id")
    try:
         row = Note.objects.get(id=id, foreign_key = user)
    except:
        return Response({'error': 'note does not exist'}, 400)
    
    data = row.delete()
    return Response({'successful': True})


@verifyJwtToken
def deleteAllTheNotesTableRows(request, user):
    rows = Note.objects.filter(foreign_key=user).delete()
    return Response({'successful': True})


from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'access': str(refresh.access_token),
    }

def registerUser(request):
    serialized_user = UserSerializer(data=request.data)
    
    if serialized_user.is_valid():
        user = serialized_user.save()
        print(user)
        return Response(get_tokens_for_user(user))
    else:
        return Response({'error': 'invalid request'}, 400)
    


def loginUser(request):
    all_user = CustomUser.objects.filter(email=request.data['email'])
    if not all_user.exists():
        return Response({'error': 'user does not exist'}, 400)
    
    for user in all_user:
        None
    return Response(get_tokens_for_user(user))