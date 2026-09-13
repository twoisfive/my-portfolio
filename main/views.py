from django.shortcuts import render

from main.models import Experience, Project


def show_main(request):
    context = {
        "name": "Faaiz",
        "npm": "2506610286",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Sistem Informasi Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Faaiz",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_projects(request):
    context = {
        "name": "Faaiz",
        "project_list": Project.objects.all(),
    }
    return render(request, "projects.html", context)