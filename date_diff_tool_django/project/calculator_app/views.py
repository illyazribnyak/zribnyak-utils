from django.shortcuts import render
from django.http import JsonResponse
from .forms import DateCalculationForm
from datetime import timedelta
from dateutil.relativedelta import relativedelta


def working_capacity(request):

    return render(request, 'calculator_app/working_capacity.html', {
        'days_form': DateCalculationForm(),
        'date_form': DateCalculationForm()
    })


def calculate_days(request):

    if request.method == 'POST':
        print(" POST-дані:", request.POST)

        days_form = DateCalculationForm(request.POST)
        if days_form.is_valid():
            start_date = days_form.cleaned_data['start_date']
            end_date = days_form.cleaned_data.get('end_date')

            if not end_date:
                return JsonResponse({"error": "Помилка: Ви не вибрали другу дату!"})

            difference_in_days = (end_date - start_date).days
            return JsonResponse({"result": f"Різниця між датами: {difference_in_days} днів"})

        else:
            print(" Помилки форми:", days_form.errors)

    return JsonResponse({"error": "Помилка в обчисленні!"})


def calculate_date(request):

    if request.method == 'POST':
        date_form = DateCalculationForm(request.POST)
        if date_form.is_valid():
            start_date = date_form.cleaned_data['start_date']
            years = date_form.cleaned_data.get('years_to_add', 0) or 0
            months = date_form.cleaned_data.get('months_to_add', 0) or 0
            days = date_form.cleaned_data.get('days_to_add', 0) or 0
            operation = date_form.cleaned_data['operation']

            if operation == 'add':
                new_date = start_date + relativedelta(years=years, months=months) + timedelta(days=days)
            else:
                new_date = start_date - relativedelta(years=years, months=months) - timedelta(days=days)

            total_days = abs((new_date - start_date).days)
            return JsonResponse(
                {"result": f"Нова дата: {new_date.strftime('%d/%m/%Y')} | Зміна в днях: {total_days} днів"})

    return JsonResponse({"error": "Помилка в обчисленні!"})
