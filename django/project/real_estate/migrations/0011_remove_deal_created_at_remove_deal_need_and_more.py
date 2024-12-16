from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ("real_estate", "0010_alter_deal_need_alter_deal_offer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="deal",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="deal",
            name="need",
        ),
        migrations.RemoveField(
            model_name="deal",
            name="offer",
        ),
        migrations.RemoveField(
            model_name="deal",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="deal",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="deal",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="deal",
            name="need",
            field=models.ForeignKey(on_delete=models.CASCADE, to="real_estate.Need"),
        ),
        migrations.AddField(
            model_name="deal",
            name="offer",
            field=models.ForeignKey(on_delete=models.CASCADE, to="real_estate.Offer"),
        ),
    ]