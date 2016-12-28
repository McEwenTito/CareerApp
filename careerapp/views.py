from django.shortcuts import render
from django.views.generic import View
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.
cluster1 = CareerCluster.objects.get(id = 1)

cluster2 = CareerCluster.objects.get(id = 2)

cluster3 = CareerCluster.objects.get(id = 3)

cluster4 = CareerCluster.objects.get(id = 4)

cluster5 = CareerCluster.objects.get(id = 5)

cluster6 = CareerCluster.objects.get(id = 7)

cluster7 = CareerCluster.objects.get(id = 8)

cluster8 = CareerCluster.objects.get(id = 9)

cluster9 = CareerCluster.objects.get(id = 10)

cluster10 = CareerCluster.objects.get(id = 11)

cluster11 = CareerCluster.objects.get(id = 12)

cluster12 = CareerCluster.objects.get(id = 13)

cluster13 = CareerCluster.objects.get(id = 14)

cluster14 = CareerCluster.objects.get(id = 15)

cluster15 = CareerCluster.objects.get(id = 16)

cluster16 = CareerCluster.objects.get(id = 17)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')

    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.html', token)

def registration_complete(request):
    return render_to_response('registration/registration_complete.html')

	
@login_required(login_url="login/")
def	index(request):
	return	render(request, 'careerapp/index.html', {})

def self_assessment(request):
	return render(request, 'careerapp/self_assessment.html', {})


class EnterGrades(View):
    form_class = GradesForm
    template_name = 'careerapp/enter_grades.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        data = []
        form = self.form_class(request.POST)
        allprog = Programme.objects.all()
        programmes = {}
        facultys = []
        institutions = []

        context = {'form': form, 'data': data, 'allprog':allprog, 'programmes':programmes, 'facultys':facultys, 'institutions':institutions,}

        if form.is_valid():

            for i in range(6):
                data.append(form.cleaned_data['grade%s' %i])

            for i in allprog:

                if set(i.prereq.all()) < set(data):
                    programmes.update({str(i.name):str(i.faculty.school.name)})
                    facultys.append(str(i.faculty.school.name))

            return render(request, 'careerapp/programmes.html', context)
        return render(request, self.template_name, context)


class ChooseInterests(View):
    form_class = ClusterForm
    template_name = 'careerapp/career_interests.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        activities = ClusterActivity.objects.all()
        paths = CareerPathway.objects.all()
        data = {}
        zipped = []
        mylist = {}
        clusters = []
        sorted_clusters = []
        form = self.form_class(request.POST)
        context = {'form': form, 'data': data, 'clusters':clusters, 'sorted_clusters':sorted_clusters,
                    'activities': activities, 'mylist': mylist}

        if form.is_valid():
            for i in range(1, 16):
                data.update({'cluster%s' %i: form.cleaned_data['cluster%s' %i]})

            #sort the dictionary
            for k in sorted(data, key = lambda k:len(data[k]), reverse=True):
                if (len(data[k])!=0):
                    sorted_clusters.append(k)
            for i in sorted_clusters:
                clusters.append(str(eval(i+'.name')))
            for i in clusters:
                mylist.update({clusters.index(i): i})

            return render(request, 'careerapp/careers.html', context)
        return render(request, self.template_name, context)

def viewcareers(request):
	empty = {}
	for i in range(1, 5):
		empty.update({'cluster%s' %i:  CareerPathway.objects.get(pk=i)})

	return render(request, 'careerapp/care.html', {'cluster1':cluster1, 'empty':empty})

def institutions(request):
	return render(request, '../interface/chanco.html')
