from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import ReserveTicketsForm

def reserve_tickets(request):
    if request.method == 'POST':
        form = ReserveTicketsForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ReserveTicketsForm()
    return render_to_response('rezervace/base.html', {
        'reserve_tickets_form': form,
    }, context_instance=RequestContext(request))
