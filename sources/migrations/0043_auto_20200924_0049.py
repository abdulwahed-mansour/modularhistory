# Generated by Django 3.0.7 on 2020-09-24 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0042_auto_20200924_0047'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AlterField(
            model_name='typedsource',
            name='type',
            field=models.CharField(choices=[('sources.textualsource', 'textual source'), ('sources.sourcewithpagenumbers', 'source with page numbers'), ('sources.piece', 'piece'), ('sources.essay', 'essay'), ('sources.documentsource', 'document source'), ('sources.document', 'document'), ('sources.affidavit', 'affidavit'), ('sources.article', 'article'), ('sources.correspondence', 'correspondence'), ('sources.email', 'email'), ('sources.letter', 'letter'), ('sources.memorandum', 'memorandum'), ('sources.spokensource', 'spoken source'), ('sources.speech', 'speech'), ('sources.address', 'address'), ('sources.discourse', 'discourse'), ('sources.lecture', 'lecture'), ('sources.sermon', 'sermon'), ('sources.statement', 'statement'), ('sources.interview', 'interview'), ('sources.journalentry', 'journal entry'), ('sources.videosource', 'video source'), ('sources.documentary', 'documentary'), ('sources.webpage', 'web page')], db_index=True, max_length=255),
        ),
    ]