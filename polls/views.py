from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from polls.models import Question
from django.core.urlresolvers import reverse

# @login_required

def firstpage(request):
	logout(request)
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('polls:index'))

def index(request):
	if not request.user.is_authenticated():
		return redirect('/polls/login/?next=%s' % request.path)
	else:
		latest_question_list = Question.objects.order_by('pub_date')[:5]
		    #output = ', '.join([p.question_text for p in latest_question_list])
		    #return HttpResponse(output)
		context = {'latest_question_list': latest_question_list}
		return render(request, 'polls/index.html', context)

def logout_view(request):
    logout(request)
    return HttpResponse("yeloo")


# @login_required
def detail(request, question_id):
	if not request.user.is_authenticated():
		return redirect('/polls/login/?next=%s' % request.path)
	else:
		question=Question.objects.get(pk=question_id)
		context={'question': question}
		return render(request, 'polls/detail.html', context)

# @login_required
def results(request, question_id):
	if not request.user.is_authenticated():
		return redirect('/polls/login/?next=%s' % request.path)
	else:
		p=get_object_or_404(Question, pk=question_id)
		return render(request, 'polls/results.html', {'question':p})

	
# @login_required	
def vote(request, question_id):
	if not request.user.is_authenticated():
		return redirect('/polls/login/?next=%s' % request.path)
	else:
		p = get_object_or_404(Question, pk=question_id)
		try:
			selected_choice = p.choice_set.get(pk=request.POST['choice'])
		except (KeyError, Choice.DoesNotExist):
			return render(request, 'polls/detail.html', {
	            'question': p,
	            'error_message': "You didn't select a choice.",
	        })

		else:
			selected_choice.votes += 1
	        selected_choice.save()
	        # Always return an HttpResponseRedirect after successfully dealing
	        # with POST data. This prevents data from being posted twice if a
	        # user hits the Back button.
	        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
	        