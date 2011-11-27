from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import BookTicketsForm

def book_tickets(request):
    if request.method == 'POST':
        form = BookTicketsForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = BookTicketsForm()
    return render_to_response('booking/base.html', {
        'book_tickets_form': form,
    }, context_instance=RequestContext(request))
