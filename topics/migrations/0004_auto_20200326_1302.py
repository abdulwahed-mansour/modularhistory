# Generated by Django 3.0.4 on 2020-03-26 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0003_auto_20200325_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='related_topics2',
            field=models.ManyToManyField(blank=True, related_name='_topic_related_topics2_+', through='topics.TopicRelation', to='topics.Topic'),
        ),
        migrations.CreateModel(
            name='TopicParentChildRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_relations', to='topics.Topic')),
                ('parent_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_relations', to='topics.Topic')),
            ],
            options={
                'unique_together': {('parent_topic', 'child_topic')},
            },
        ),
        migrations.AddField(
            model_name='topic',
            name='parent_topics',
            field=models.ManyToManyField(blank=True, related_name='_topic_parent_topics_+', through='topics.TopicParentChildRelation', to='topics.Topic'),
        ),
    ]
