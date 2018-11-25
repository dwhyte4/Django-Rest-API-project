# Generated by Django 2.1.3 on 2018-11-25 14:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergic_ingredients', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(max_length=50)),
                ('comment', models.TextField(blank=True)),
                ('temperature', models.BooleanField()),
                ('time', models.TimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('contact_number', models.CharField(max_length=15)),
                ('picture', models.ImageField(blank=True, upload_to='images/users_img')),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=250)),
                ('postcode', models.CharField(max_length=30)),
                ('terms_conditions', models.BooleanField(default=False)),
                ('validation', models.BooleanField(default=False)),
                ('company', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='requests',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Requests_address', to='Myapp.Users'),
        ),
        migrations.AddField(
            model_name='requests',
            name='allergic_ingredients',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Requests_ingredient', to='Myapp.Allergies'),
        ),
        migrations.AddField(
            model_name='requests',
            name='contact_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Requests_contact_number', to='Myapp.Users'),
        ),
        migrations.AddField(
            model_name='requests',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Requests_name', to='Myapp.Users'),
        ),
        migrations.AddField(
            model_name='requests',
            name='picture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Requests_picture', to='Myapp.Users'),
        ),
        migrations.AddField(
            model_name='requests',
            name='postcode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Requests_postcode', to='Myapp.Users'),
        ),
    ]
