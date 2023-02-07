from .models import Note
from .serialize import NoteSerializer
from rest_framework.response import Response



def getAllTheNotesTableRow():
    rows = Note.objects.all()
    #converts the Note class into json format
    serialized_rows = NoteSerializer(rows, many= True)
    return serialized_rows.data


def insertRowInNotesTable(request):
    serialized_note = NoteSerializer(data= request.data)
    if serialized_note.is_valid():
        serialized_note.save()
        return serialized_note.data
    else:
        return {'error': 'invalid request'}
    

def getSingleNotesTableRow(request):
    name = request.query_params.get("name")
    row = Note.objects.get(name=name)
    serialized_note = NoteSerializer(row)
    return serialized_note.data


def updateNotesTableRow(request):
    name = request.query_params.get("name")
    payload = request.POST.dict()
    row = Note.objects.get(name=name)
    row.name = name
    row.description = payload['description']
    row.save()
    return {'successful': True}


def deleteNotesTableRow(request):
    name = request.query_params.get("name")
    row = Note.objects.get(name=name)
    data = row.delete()
    print(data)
    return {'successful': True}