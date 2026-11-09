from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Experience, Project


class ProjectSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id", "title", "description", "role", "tech_stack",
            "thumbnail", "project_url", "repo_url", "started_at", "ended_at",
            "star_count", "is_starred", "starred_by_names", "tech_list", "is_ongoing"
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_tech_stack(self, value):
        return strip_tags(value)

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())

class ExperienceSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()
    
    class Meta:
        model = Experience
        fields = [
            "id", "title", "description", "category", "thumbnail", "started_at", "ended_at",
            "star_count", "is_starred", "starred_by_names",
        ]
        
    def validate_title(self, value):
        value = strip_tags(value).strip()
        if (not value):
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
            return strip_tags(value)
    
    def validate_category(self, value):
        return strip_tags(value)
    
    def validate(self, attrs):
        # For PATCH, attrs may only contain some fields — fall back to the instance
        started_at = attrs.get("started_at", getattr(self.instance, "started_at", None))
        ended_at   = attrs.get("ended_at",   getattr(self.instance, "ended_at",   None))

        if started_at and ended_at and ended_at < started_at:
            raise serializers.ValidationError({
                "ended_at": "Tanggal selesai tidak boleh lebih awal dari tanggal mulai."
            })
        return attrs

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())
    
        

