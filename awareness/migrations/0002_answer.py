# Generated by Django 2.2 on 2020-04-11 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0001_initial'),
        ('awareness', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reply', to='awareness.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermanagement.UserProfile')),
            ],
        ),
    ]
