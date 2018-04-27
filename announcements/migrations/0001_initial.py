# Generated by Django 2.0.2 on 2018-04-27 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('announce_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('announce_text', models.TextField()),
                ('announce_title', models.CharField(max_length=20)),
                ('submit_date', models.DateField()),
                ('expire_date', models.DateField()),
                ('approve_status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='AnnounceTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_announcement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='announcements.Announcement')),
            ],
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(default='', max_length=50)),
                ('first', models.CharField(default='', max_length=20)),
                ('last', models.CharField(default='', max_length=30)),
                ('admin_status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_announce', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='announcements.Announcement')),
                ('saver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='announcements.Individual')),
            ],
        ),
        migrations.CreateModel(
            name='SubmitTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('tag_text', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('approved', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TagSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_search_time', models.TimeField()),
                ('tag_search_date', models.DateField()),
                ('searched_tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='announcements.Tags')),
                ('user_searching_tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='announcements.Individual')),
            ],
        ),
        migrations.CreateModel(
            name='UserSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_time', models.TimeField()),
                ('search_date', models.DateField()),
                ('searched_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='searched', to='announcements.Individual')),
                ('user_searching_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='searcher', to='announcements.Individual')),
            ],
        ),
        migrations.AddField(
            model_name='submittag',
            name='submitted_tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announcements.Tags'),
        ),
        migrations.AddField(
            model_name='submittag',
            name='tag_submitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='announcements.Individual'),
        ),
        migrations.AddField(
            model_name='announcetags',
            name='the_tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='announcements.Tags'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='approver',
            field=models.ForeignKey(default='mark.penrod@gmail.com', on_delete=django.db.models.deletion.PROTECT, related_name='approver', to='announcements.Individual'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='submitter',
            field=models.ForeignKey(default='mark.penrod@gmail.com', on_delete=django.db.models.deletion.PROTECT, related_name='submitter', to='announcements.Individual'),
        ),
        migrations.AlterUniqueTogether(
            name='usersearch',
            unique_together={('user_searching_user', 'searched_user')},
        ),
        migrations.AlterUniqueTogether(
            name='tagsearch',
            unique_together={('user_searching_tag', 'searched_tag')},
        ),
        migrations.AlterUniqueTogether(
            name='submittag',
            unique_together={('tag_submitter', 'submitted_tag')},
        ),
        migrations.AlterUniqueTogether(
            name='save',
            unique_together={('saver', 'saved_announce')},
        ),
        migrations.AlterUniqueTogether(
            name='announcetags',
            unique_together={('the_announcement', 'the_tag')},
        ),
    ]
