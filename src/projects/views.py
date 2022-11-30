from django.shortcuts import render
from datetime import datetime

today = datetime.now()
time = today.strftime('%H:%M:%S')
list_of_projects = [
    {'id':'1', 'title': 'E-commerce Website', 'description': 'Fully functional ecommerce website'},
    {'id':'2', 'title': 'Portfolio Website', 'description': 'My portfolio website of awesomeness'},
    {'id':'3', 'title': 'Social Network', 'description': 'Awesome project I am still working on'},
]

def projects(request):
    return render(request, 'projects/projects.html', {
        'time': time,
        'projects': list_of_projects,
    })
def project(request, pk):
    project_obj = None
    for item in list_of_projects:
        if item.get("id", None) == pk:
            project_obj = item
    return render(request, 'projects/single-project.html', {
        'project': project_obj,
    })
