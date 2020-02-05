from django import forms


class SurveyForm(forms.Form):
    CHOICES = [(1, '1'),
               (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')]

    code = forms.CharField(label='Your alphanumeric code (6 digits)*',max_length=6, min_length=6, required=True)
    experience = forms.ChoiceField(label='How would you rate your experience with the Validation Workflow and Process? (10 being highest)*',
                                   choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'radios'}), required=True)
    CHOICES_B = [(True, 'Yes'), (False, 'No')]

    complete = forms.ChoiceField(label='Were you able to complete full validations without engaging a Network Engineer?*',
                                 choices=CHOICES_B, widget=forms.RadioSelect(attrs={'class': 'radios'}), required=True)

    recommendation = forms.CharField(
        label='What improvements would you recommend?', widget=forms.Textarea(attrs={'class': 'freetext'}))
