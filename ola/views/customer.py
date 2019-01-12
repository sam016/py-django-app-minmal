'''
customers views
'''

from django.shortcuts import render


def get_list(request):
    '''
    Shows the list of the customers
    '''
    return render(request, 'ola/customers-list.html')


def get_by_id(request, id):
    '''
    Shows a specific customer screen
    '''
    context = {
        'id': id,
    }
    return render(request, 'ola/customer-id.html', context)
