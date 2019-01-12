'''
Welcome index page
'''

from django.shortcuts import render

def index(request):
    '''
    serves the index.html at /
    '''
    return render(request, 'ola/index.html')
