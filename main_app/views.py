from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SurveyForm
from .models import Survey


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SurveyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cd = form.cleaned_data['code']  # code
            exp = form.cleaned_data['experience']  # experience
            completion = form.cleaned_data['complete']  # ease of completion
            recommend = form.cleaned_data['recommendation']  # recommendation
            survey = Survey(code=cd, experience=exp,
                            form_completion=completion, recommendation=recommend)
            survey.save()
            # redirect to a new URL:
            return render(request, 'thanks.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SurveyForm()

    return render(request, 'index.html', {'form': form})
