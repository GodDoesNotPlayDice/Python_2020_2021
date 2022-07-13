from io import open
import os
def UserSelect():
    userSelect = os.listdir('C:/Users')
    for i in userSelect:
        if i == 'All Users' and 'Default' and 'Default User' and 'desktop.ini' and 'Public':
            pass
        else:
            user = i
    return user
def DocsLocation(user):
    docs = os.listdir(f'C:/Users/{user}')
    for i in docs:
        if i != 'Documents':
            pass
        else:
            documents = i
            docsOpen = os.listdir(f'C:/Users/{user}/{documents}')
            return docsOpen

def ExtractDocs(docs):
    for i in docs:
        txtSearch = os.listdir() 

    