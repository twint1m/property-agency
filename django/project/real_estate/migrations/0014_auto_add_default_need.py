from django.db import migrations, models

def set_default_need(apps, schema_editor):
    Need = apps.get_model('real_estate', 'Need')
    default_need = Need.objects.first()
    if default_need:
        Deal = apps.get_model('real_estate', 'Deal')
        for deal in Deal.objects.filter(need__isnull=True):
            deal.need = default_need
            deal.save()

class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0013_event'),
    ]

    operations = [
        migrations.RunPython(set_default_need),
        migrations.AlterField(
            model_name='deal',
            name='need',
            field=models.ForeignKey(on_delete=models.CASCADE, to='real_estate.Need', null=False),
        ),
    ]