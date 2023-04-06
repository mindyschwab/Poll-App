from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('who', models.CharField(max_length=150)),
                ('what', models.CharField(max_length=150)),
                ('where', models.CharField(max_length=100)),
                ('when', models.DateField(verbose_name='event Date')),
                ('why', models.TextField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('creator', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('choice_one', models.CharField(max_length=100, null=True)),
                ('choice_two', models.CharField(max_length=100, null=True)),
                ('choice_three', models.CharField(max_length=100, null=True)),
                ('choice_one_count', models.IntegerField(default=0, null=True)),
                ('choice_two_count', models.IntegerField(default=0, null=True)),
                ('choice_three_count', models.IntegerField(default=0, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.event')),
            ],
        ),
    ]
