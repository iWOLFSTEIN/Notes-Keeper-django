from rest_framework.response import Response
from rest_framework.decorators import api_view
from .controller import *


@api_view(['GET'])
def getAllTheNotes(request):
    notes = getAllTheNotesTableRow()
    return Response(notes)


@api_view(['GET'])
def getNote(request):
    note = getSingleNotesTableRow(request)
    return Response(note)


@api_view(['POST'])
def addNote(request):
    note = insertRowInNotesTable(request)
    if note.get('error'):
        return Response(note, 400)
    return Response(note)


@api_view(['POST'])
def updateNote(request):
    response = updateNotesTableRow(request)
    return Response(response)


@api_view(['GET'])
def deleteNote(request):
    response = deleteNotesTableRow(request)
    return Response(response)