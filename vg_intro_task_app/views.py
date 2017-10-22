from django.shortcuts import render
from django.template import engines
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Entry
from django.db.models import F, ExpressionWrapper, FloatField
from django.db.models.functions import Cast


def index(request):
    machine_model = request.POST['machine_model']

    entries = Entry.objects.annotate(
    current_overload=ExpressionWrapper(100*(Cast(F('current_weight'), FloatField()) - Cast(F('max_load'), FloatField()))/Cast(F('max_load'), FloatField()), output_field=FloatField())).all()
    machine_model_list = entries.values_list('machine_model', flat=True).distinct()
    if machine_model != "ALL":
        entries = entries.filter(machine_model=machine_model)
     
    result_template = '''<!DOCTYPE html>
    <html>
    <head>
      <title>VIST-Group Intro Task</title>
    </head>
    <body>
    <form action="/" method="post">  
    <select size="1" name="machine_model">
    {% for item in machine_model_list %}   
    <option value="{{ item }}">{{ item }}</option>
    {% endfor %}
    <option value="ALL">ВСЕ</option>
    </select>
    <input type="submit" value="Применить">
    </form>
    <table border=1>
    <tr>
        <td>Бортовой номер</td>
        <td>Модель</td>
        <td>Макс. грузоподъемность, т</td>
        <td>Текущий вес, т</td>
        <td>Перегруз, %</td>
    </tr>
    {% for item in entries %}
    <tr>
        <td>{{ item.machine_id }}</td>
        <td>{{ item.machine_model }}</td>
        <td>{{ item.max_load }}</td>
        <td>{{ item.current_weight }}</td>
        <td>{{ item.current_overload | floatformat:2}}</td>
    </tr>
    {% endfor %}     
    </body>
    </html>    
    '''    
    
    django_engine = engines['django']
    template = django_engine.from_string(result_template)
    html = template.render({'entries':entries, 'machine_model_list':machine_model_list})

    return HttpResponse(html)

