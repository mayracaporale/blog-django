
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_alter_publicacion_autor"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Publicacion",
            new_name="Post",
        ),
        migrations.AddField(
            model_name="post",
            name="estado",
            field=models.CharField(
                choices=[
                    ("borrador", "Borrador"),
                    ("publicado", "Publicado"),
                    ("archivado", "Archivado"),
                ],
                default="borrador",
                max_length=20,
            ),
        ),
    ]
