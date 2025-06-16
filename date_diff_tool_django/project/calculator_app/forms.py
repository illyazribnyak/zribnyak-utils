from django import forms

class DateCalculationForm(forms.Form):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Початкова дата"
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Кінцева дата",
        required=False
    )
    operation = forms.ChoiceField(
        choices=[('add', 'Додати'), ('subtract', 'Відняти')],
        required=False
    )
    years_to_add = forms.IntegerField(label="Роки", required=False, initial=0)
    months_to_add = forms.IntegerField(label="Місяці", required=False, initial=0)
    days_to_add = forms.IntegerField(label="Дні", required=False, initial=0)

    days_to_add = forms.IntegerField(
        label='Кількість днів',
        required=False,
        initial=0
    )
    months_to_add = forms.IntegerField(
        label='Кількість місяців',
        required=False,
        initial=0
    )
    years_to_add = forms.IntegerField(
        label='Кількість років',
        required=False,
        initial=0
    )
