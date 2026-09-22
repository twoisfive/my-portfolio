from django.db import migrations


def create_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")

    editor_group, _ = Group.objects.get_or_create(name="Editor")

    perms = Permission.objects.filter(
        content_type__app_label="main",
        codename__in=[
            "change_project",
            "change_experience",
        ],
    )
    editor_group.permissions.set(perms)


def remove_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name="Editor").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_experience_starred_by_project_starred_by"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.RunPython(create_groups, remove_groups),
    ]