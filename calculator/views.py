from django.shortcuts import render
from datetime import datetime, timedelta
import pytz

def time_calculator(request):
    result = None
    moscow_tz = pytz.timezone('Europe/Moscow')

    if request.method == 'POST':
        time1 = request.POST.get('time1')
        time2 = request.POST.get('time2')
        operation = request.POST.get('operation')

        try:
            time1 = datetime.strptime(time1, '%H:%M').replace(tzinfo=moscow_tz)
            time2 = datetime.strptime(time2, '%H:%M').replace(tzinfo=moscow_tz)

            if operation == 'add':
                result_time = (time1 + timedelta(hours=time2.hour, minutes=time2.minute)).time()
            elif operation == 'subtract':
                result_time = (time1 - timedelta(hours=time2.hour, minutes=time2.minute)).time()

            result = result_time.strftime('%H:%M')
        except ValueError:
            result = 'Пожалуйста, введите корректный формат. ЧЧ:ММ.'
        
    return render(request, 'calculator/time_calculator.html', {'result': result})
