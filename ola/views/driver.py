'''
Drivers vierws
'''

from django.shortcuts import render


def get_list(request):
    '''
    Shows the list of the drivers
    '''
    return render(request, 'ola/drivers-list.html')


def get_by_id(request id):
    '''
    Shows a specific driver screen
    '''
    return render(request, 'ola/drivers-id.html')
