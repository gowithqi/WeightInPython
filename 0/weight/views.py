# Create your views here.
# Create your views here.
from datetime import datetime, tzinfo
from decimal import *

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader, Context
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.db.models import Avg
from django.views import generic

from weight.models import User, WeightRecord

# now = datetime.utcnow().replace(tzinfo=CST)

def index(request):
	template = loader.get_template("login.html")
	context = RequestContext(request, {
		"id": "5"
		})

	return HttpResponse(template.render(context))

def login(request):
	try:
		user = User.objects.get(username=request.POST['username'])
		if (user.password != request.POST['password']): 
			return HttpResponseRedirect('/weight')
	except User.DoesNotExist:
		user = User(username=request.POST['username'], password=request.POST['password'])
		user.save()

	template = loader.get_template("userpage.html")
	# user = user.values()
	print user.username
	context = RequestContext(request,{
		'u': user,
		})
	return HttpResponse(template.render(context))

def requestweightdata(request, user_id, year, month, day):
	user = User.objects.get(id=user_id)
	weights = user.weightrecord_set.filter(date__gte=datetime(year=int(year), month=int(month), day=int(day))).order_by('date').values('date').annotate(avgw=Avg('weight'))
	res = ""
	for w in weights:
		res = res + str(w['date'].year) + '-' + str(w['date'].month) + '-' + str(w['date'].day) + '-' + str(w['avgw'])+"\n"
	print res
	res = res[:-1]	
	print res

	return HttpResponse(res)

def submit(request):
	print request.GET['user_id']
	user = User.objects.get(id=long(request.GET['user_id']))
	print "midle"
	record = WeightRecord.objects.create(user=user, weight=Decimal(request.GET['weight']).quantize(Decimal('100.0')))
	print "aaaa"	

	return HttpResponse(request.GET['weight'])

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

# def vote(request, poll_id):
# 	p = get_object_or_404(Poll, pk=poll_id)
# 	try:
# 		selected_choice = p.choice_set.get(pk=request.POST['choice'])
# 	except (KeyError, Choice.DoesNotExist): 
# 		return render(request, 'polls/detail.html', {
# 			'poll': p,
# 			'error_message' : "You didn't select a choice"
# 			})
# 	else:
# 		selected_choice.votes += 1
# 		selected_choice.save()
# 		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
# 	return HttpResponse("You're voting on poll %s" % poll_id)

