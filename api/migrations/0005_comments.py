# Generated by Django 5.0.4 on 2024-04-17 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=500)),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.blog')),
                ('commenter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
    ]
