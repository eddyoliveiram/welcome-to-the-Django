from django.db import migrations
from django.contrib.auth.models import Permission, Group


def create_groups_with_permissions(apps, schema_editor):
    # Get permission objects
    post_add = Permission.objects.get(codename='add_post')
    post_change = Permission.objects.get(codename='change_post')
    post_delete = Permission.objects.get(codename='delete_post')
    post_view = Permission.objects.get(codename='view_post')

    comment_add = Permission.objects.get(codename='add_comment')
    comment_change = Permission.objects.get(codename='change_comment')
    comment_delete = Permission.objects.get(codename='delete_comment')
    comment_view = Permission.objects.get(codename='view_comment')

    # Create Moderators group
    # Moderators can manage all posts and comments (including from other users)
    moderators_group, created = Group.objects.get_or_create(name='Moderators')
    if created:
        moderators_group.permissions.add(
            post_add, post_change, post_delete, post_view,
            comment_add, comment_change, comment_delete, comment_view
        )


def delete_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name__in=['Moderators']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial_data'),
    ]

    operations = [
        migrations.RunPython(create_groups_with_permissions, delete_groups),
    ]
