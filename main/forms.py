from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Project, Experience

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "role",
            "tech_stack",
            "project_url",
            "repo_url",
            "started_at",
            "ended_at",
            "thumbnail",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "repo_url": "URL Repository",
            "started_at": "Tanggal Mulai",
            "ended_at": "Tanggal Selesai",
            "thumbnail": "Thumbnail",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "repo_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "started_at": TextInput(
                attrs={
                    "placeholder": "2023-01-01",
                }
            ),
            "ended_at": TextInput(
                attrs={
                    "placeholder": "2023-01-01",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }
        
class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "started_at",
            "ended_at",
            "thumbnail",
        ]

        labels = {
            "title": "Nama Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
            "started_at": "Tanggal Mulai",
            "ended_at": "Tanggal Selesai",
            "thumbnail": "Thumbnail",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Software Engineer Intern at Google",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pengalamanmu",
                    "rows": 3,
                }
            ),
            "started_at": TextInput(
                attrs={
                    "placeholder": "2023-01-01",
                }
            ),
            "ended_at": TextInput(
                attrs={
                    "placeholder": "2023-01-01",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }