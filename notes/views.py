from rest_framework.response import Response
from rest_framework.decorators import api_view
from .controller import *


@api_view(['GET'])
def getAllTheNotes(request):
    notes = getAllTheNotesTableRow()
    return Response(notes)


@api_view(['GET'])
def getNote(request):
    name = request.query_params.get("name")
    note = getSingleNotesTableRow(name)
    return Response(note)


@api_view(['POST'])
def addNote(request):
    note = insertRowInNotesTable(request)
    return Response(note)