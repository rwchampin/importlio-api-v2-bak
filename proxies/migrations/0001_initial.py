# Generated by Django 4.2.3 on 2023-07-07 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proxy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('asn', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('port', models.PositiveIntegerField()),
                ('protocol', models.CharField(choices=[('HTTP', 'HTTP'), ('HTTPS', 'HTTPS')], max_length=10)),
                ('isp', models.CharField(max_length=100)),
                ('google', models.BooleanField(default=False)),
                ('last_checked', models.DateTimeField()),
                ('org', models.CharField(max_length=100)),
                ('latency', models.PositiveIntegerField()),
                ('country', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('times_used', models.PositiveIntegerField(default=0)),
                ('connection_time', models.PositiveIntegerField(default=0)),
                ('speed', models.PositiveIntegerField(default=0)),
                ('response_time', models.PositiveIntegerField(default=0)),
                ('anonymity_level', models.CharField(blank=True, max_length=100)),
                ('usage_count', models.PositiveIntegerField(default=0)),
                ('failure_count', models.PositiveIntegerField(default=0)),
                ('last_used_at', models.DateTimeField(blank=True, null=True)),
                ('up_time', models.PositiveIntegerField(default=0)),
                ('up_time_success_count', models.PositiveIntegerField(default=0)),
                ('up_time_try_count', models.PositiveIntegerField(default=0)),
                ('working_percent', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
