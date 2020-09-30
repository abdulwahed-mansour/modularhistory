# Generated by Django 3.0.10 on 2020-09-29 03:50

from django.db import migrations


class RenameModelAndBaseOperation(migrations.RenameModel):

    def __init__(self, old_name, new_name):
        super(RenameModelAndBaseOperation, self).__init__(old_name, new_name)

    def state_forwards(self, app_label, state):
        old_remote_model = '%s.%s' % (app_label, self.old_name_lower)
        new_remote_model = '%s.%s' % (app_label, self.new_name_lower)
        to_reload = []
        # change all bases affected by rename
        for (model_app_label, model_name), model_state in state.models.items():
            if old_remote_model in model_state.bases:
                new_bases_tuple = tuple(
                    new_remote_model if base == old_remote_model else base
                    for base in model_state.bases
                )
                state.models[model_app_label, model_name].bases = new_bases_tuple
                to_reload.append((model_app_label, model_name))
        super(RenameModelAndBaseOperation, self).state_forwards(app_label, state)
        state.reload_models(to_reload, delay=True)


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20200909_0442'),
        ('entities', '0012_auto_20200909_0442'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('sources', '0057_auto_20200929_0223'),
    ]

    operations = [
        RenameModelAndBaseOperation(
            old_name='TypedSource',
            new_name='Source',
        ),
    ]