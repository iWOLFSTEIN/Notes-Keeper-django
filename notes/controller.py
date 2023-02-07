from .models import Note
from .serialize import NoteSerializer


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
        Exception('Invalid Request')


def getSingleNotesTableRow(name):
    row = Note.objects.get(name=name)
    serialized_note = NoteSerializer(row)
    return serialized_note.data