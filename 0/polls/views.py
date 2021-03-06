# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Poll, Choice

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_poll_list' 

	def get_queryset(self):
	 	return Poll.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView): 
	model = Poll
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView): 
	model = Poll
	template_name = "polls/results.html"

# def index(request):
#     latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     return HttpResponseRedirect(reverse('/static/html/polls/index.html', args=(latest_poll_list, )))

# def detail(request, poll_id):
# 	try:
# 		poll = Poll.objects.get(pk=poll_id)
# 	except Poll.DoesNotExist:
# 		raise Http404
# 	return HttpResponseRedirect(reverse('/static/html/polls/detail.html', args=(poll, )))

# def results(request, poll_id):
#     poll = get_object_or_404(Poll, pk=poll_id)
    
#     return HttpResponseRedirect(reverse('/static/html/polls/results.html', args=(poll, )))

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist): 
		return render(request, 'polls/detail.html', {
			'poll': p,
			'error_message' : "You didn't select a choice"
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
	return HttpResponse("You're voting on poll %s" % poll_id)

