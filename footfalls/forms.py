from django import forms

choices = (
    ('#1', 'Bar chart'),
    ('#2', 'Line chart'),
)

display_chart_by = (
    ('raw', 'Raw data'),
    ('normalize', 'Normalized data'),
)

class SearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    chart_type = forms.ChoiceField(choices=choices)
    display_chart_by = forms.ChoiceField(choices=display_chart_by)