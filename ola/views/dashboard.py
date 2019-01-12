'''
dashboard page
'''

from django.shortcuts import render

def index(request):
    '''
    serves the dashboard page at /dashboard
    '''
    return render(request, 'ola/dashboard.html')
