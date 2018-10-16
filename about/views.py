from django.shortcuts import render
from .models import Person

def home(request):
    person = Person.objects.get(id=1)
    print(person.name)
    personskills = person.skills.all()
    personportfolio = person.portfolios.all()

    return render(request,'about/home.html',{'person':person})
