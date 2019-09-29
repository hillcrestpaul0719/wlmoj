# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-31 22:18
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0001_squashed_0086_contest_formats'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmissionSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.TextField(max_length=65536, verbose_name='source code')),
                ('submission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='judge.Submission', verbose_name='associated submission')),
            ],
        ),
        migrations.RunSQL(
            ['''INSERT INTO judge_submissionsource (source, submission_id)
                SELECT source, id AS 'submission_id' FROM judge_submission;'''],
            ['''UPDATE judge_submission sub
                INNER JOIN judge_submissionsource src ON sub.id = src.submission_id
                SET sub.source = src.source;'''],
            elidable=True,
        ),
        migrations.RemoveField(
            model_name='submission',
            name='source',
        ),
        migrations.AlterField(
            model_name='submissionsource',
            name='submission',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='judge.Submission', verbose_name='associated submission'),
        ),
    ]
