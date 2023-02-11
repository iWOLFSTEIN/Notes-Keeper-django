from rest_framework.decorators import api_view
from .controller import *


@api_view(['GET'])
def getAllTheNotes(request):
    response = getAllTheNotesTableRow(request)
    return response


@api_view(['GET'])
def getNote(request):
    response = getSingleNotesTableRow(request)
    return response


@api_view(['POST'])
def addNote(request):
    response = insertRowInNotesTable(request)
    return response


@api_view(['POST'])
def updateNote(request):
    response = updateNotesTableRow(request)
    return response


@api_view(['GET'])
def deleteNote(request):
    response = deleteNotesTableRow(request)
    return response

@api_view(['GET'])
def deleteAllTheNotes(request):
    response = deleteAllTheNotesTableRows(request)
    return response


@api_view(['POST'])
def register(request):
    response = registerUser(request)
    return response


@api_view(['POST'])
def login(request):
    response = loginUser(request)
    return response