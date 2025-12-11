from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import Post, Comment


class Command(BaseCommand):
    help = 'Seed database with initial data (users, posts, comments, groups)'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')

        # Create users
        self.stdout.write('Creating users...')
        users = []
        user_data = [
            {'username': 'user1', 'email': 'user1@example.com', 'first_name': 'João', 'last_name': 'Silva'},
            {'username': 'user2', 'email': 'user2@example.com', 'first_name': 'Maria', 'last_name': 'Santos'},
            {'username': 'user3', 'email': 'user3@example.com', 'first_name': 'Pedro', 'last_name': 'Oliveira'},
        ]

        for data in user_data:
            user, created = User.objects.get_or_create(
                username=data['username'],
                defaults={
                    'email': data['email'],
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                    'is_staff': False,
                    'is_active': True,
                }
            )
            if created:
                user.set_password('password123')
                user.save()
                self.stdout.write(self.style.SUCCESS(f'  + Created user: {user.username}'))
            else:
                self.stdout.write(self.style.WARNING(f'  - User already exists: {user.username}'))
            users.append(user)

        # Create posts
        self.stdout.write('Creating posts...')
        posts = []
        for i in range(1, 11):
            author = users[(i - 1) % len(users)]
            post, created = Post.objects.get_or_create(
                title=f'Post {i}',
                defaults={
                    'content': f'Conteúdo do post {i}',
                    'author': author
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  + Created post: {post.title}'))
            posts.append(post)

        # Create comments
        self.stdout.write('Creating comments...')
        for i in range(1, 11):
            post = posts[(i - 1) % len(posts)]
            author = users[(i - 1) % len(users)]
            comment, created = Comment.objects.get_or_create(
                post=post,
                author=author,
                content=f'Comentário {i} no {post.title}'
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  + Created comment on: {post.title}'))

        # Create groups and permissions
        self.stdout.write('Creating groups and permissions...')

        # Get content types
        post_content_type = ContentType.objects.get_for_model(Post)
        comment_content_type = ContentType.objects.get_for_model(Comment)

        # Get permissions
        post_permissions = Permission.objects.filter(content_type=post_content_type)
        comment_permissions = Permission.objects.filter(content_type=comment_content_type)

        # Create Moderators group
        moderators_group, created = Group.objects.get_or_create(name='Moderators')
        if created:
            moderators_group.permissions.set(list(post_permissions) + list(comment_permissions))
            self.stdout.write(self.style.SUCCESS('  + Created group: Moderators'))
        else:
            self.stdout.write(self.style.WARNING('  - Group already exists: Moderators'))

        self.stdout.write(self.style.SUCCESS('\nDatabase seeded successfully!'))
        self.stdout.write(f'\nSummary:')
        self.stdout.write(f'  - Users: {User.objects.count()}')
        self.stdout.write(f'  - Posts: {Post.objects.count()}')
        self.stdout.write(f'  - Comments: {Comment.objects.count()}')
        self.stdout.write(f'  - Groups: {Group.objects.count()}')
