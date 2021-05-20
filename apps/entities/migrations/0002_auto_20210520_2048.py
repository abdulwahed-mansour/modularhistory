# Generated by Django 3.1.9 on 2021-05-20 20:08

import django.db.models.deletion
from django.db import migrations, models

import apps.quotes.models.model_with_related_quotes
import core.fields.m2m_foreign_key


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0001_initial'),
        ('quotes', '0001_initial'),
        ('entities', '0001_initial'),
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quoterelation',
            name='quote',
            field=core.fields.m2m_foreign_key.ManyToManyForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='entities_quoterelations',
                to='quotes.quote',
            ),
        ),
        migrations.AddField(
            model_name='idea',
            name='promoters',
            field=models.ManyToManyField(
                blank=True, related_name='ideas', to='entities.Entity'
            ),
        ),
        migrations.AddField(
            model_name='entityimage',
            name='entity',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='image_relations',
                to='entities.entity',
            ),
        ),
        migrations.AddField(
            model_name='entityimage',
            name='image',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='entity_relations',
                to='images.image',
            ),
        ),
        migrations.AddField(
            model_name='entityidea',
            name='entity',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='entity_ideas',
                to='entities.entity',
                verbose_name='entity',
            ),
        ),
        migrations.AddField(
            model_name='entityidea',
            name='idea',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='entity_ideas',
                to='entities.idea',
                verbose_name='idea',
            ),
        ),
        migrations.AddField(
            model_name='entity',
            name='affiliated_entities',
            field=models.ManyToManyField(
                blank=True,
                related_name='_entity_affiliated_entities_+',
                through='entities.Affiliation',
                to='entities.Entity',
            ),
        ),
        migrations.AddField(
            model_name='entity',
            name='categories',
            field=models.ManyToManyField(
                blank=True,
                related_name='entities',
                through='entities.Categorization',
                to='entities.Category',
            ),
        ),
        migrations.AddField(
            model_name='entity',
            name='images',
            field=models.ManyToManyField(
                blank=True,
                related_name='entities',
                through='entities.EntityImage',
                to='images.Image',
            ),
        ),
        migrations.AddField(
            model_name='entity',
            name='related_entities',
            field=models.ManyToManyField(
                blank=True,
                related_name='entity_set',
                to='entities.Entity',
                verbose_name='related entities',
            ),
        ),
        migrations.AddField(
            model_name='entity',
            name='related_quotes',
            field=apps.quotes.models.model_with_related_quotes.RelatedQuotesField(
                blank=True,
                related_name='entity_set',
                through='entities.QuoteRelation',
                to='quotes.Quote',
                verbose_name='related quotes',
            ),
        ),
        migrations.AddField(
            model_name='entity',
            name='tags',
            field=models.ManyToManyField(
                blank=True,
                related_name='entity_set',
                to='topics.Topic',
                verbose_name='tags',
            ),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='children',
                to='entities.category',
            ),
        ),
        migrations.AddField(
            model_name='categorization',
            name='category',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='categorizations',
                to='entities.category',
                verbose_name='category',
            ),
        ),
        migrations.AddField(
            model_name='categorization',
            name='entity',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='categorizations',
                to='entities.entity',
                verbose_name='entity',
            ),
        ),
        migrations.AddField(
            model_name='affiliation',
            name='affiliated_entity',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='entities.entity',
                verbose_name='affiliated entity',
            ),
        ),
        migrations.AddField(
            model_name='affiliation',
            name='entity',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='affiliations',
                to='entities.entity',
                verbose_name='entity',
            ),
        ),
        migrations.AddField(
            model_name='affiliation',
            name='roles',
            field=models.ManyToManyField(
                blank=True,
                related_name='affiliations',
                through='entities.RoleFulfillment',
                to='entities.Role',
                verbose_name='roles',
            ),
        ),
        migrations.CreateModel(
            name='Deity',
            fields=[],
            options={
                'verbose_name_plural': 'Deities',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('entities.entity',),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[],
            options={
                'verbose_name_plural': 'Groups',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('entities.entity',),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[],
            options={
                'verbose_name_plural': 'Organizations',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('entities.entity',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[],
            options={
                'verbose_name_plural': 'People',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('entities.entity',),
        ),
        migrations.AlterUniqueTogether(
            name='rolefulfillment',
            unique_together={('affiliation', 'role', 'start_date')},
        ),
        migrations.AlterUniqueTogether(
            name='entityimage',
            unique_together={('entity', 'image')},
        ),
        migrations.AlterUniqueTogether(
            name='entityidea',
            unique_together={('entity', 'idea')},
        ),
        migrations.AlterUniqueTogether(
            name='categorization',
            unique_together={('entity', 'category')},
        ),
        migrations.AlterUniqueTogether(
            name='affiliation',
            unique_together={('entity', 'affiliated_entity', 'start_date')},
        ),
    ]