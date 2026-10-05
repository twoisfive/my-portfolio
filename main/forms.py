from django.forms import ModelForm, TextInput, Textarea, URLInput
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError
from django.utils import timezone

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
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()
        
        
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
    def clean_title(self):
            title = strip_tags(self.cleaned_data["title"]).strip()
            if not title:
                raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
            return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()