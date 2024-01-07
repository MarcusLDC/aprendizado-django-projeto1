from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('''
                        <!DOCTYPE>
                        <html>
                            <head> <title> Hello World </title> <head>
                            <body> <h1>  Hello  World! </body>
                        </html>
                        ''')

