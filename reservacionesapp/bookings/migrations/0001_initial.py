# Generated by Django 4.1.7 on 2023-03-05 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
                ('status', models.CharField(choices=[('a', 'active'), ('n', 'noactive')], max_length=35)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, verbose_name='Clave')),
                ('description', models.TextField(blank=True, verbose_name='Nombre')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio')),
                ('available', models.IntegerField(null=True, verbose_name='Disponible')),
                ('has_vat', models.BooleanField(null=True, verbose_name='Tiene Iva')),
                ('status', models.CharField(choices=[('a', 'active'), ('n', 'noactive')], max_length=35)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='bookings.category', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Cantidad')),
                ('price', models.FloatField(verbose_name='Precio')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='bookings.product')),
            ],
            options={
                'verbose_name': 'Almacén',
                'verbose_name_plural': 'Almacenes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio')),
                ('quantity', models.IntegerField(default=0, verbose_name='Cantidad')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Subtotal')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_details', to='bookings.product', verbose_name='Producto')),
                ('sale_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_details', to='bookings.sale')),
            ],
            options={
                'verbose_name': 'Detalle Venta',
                'verbose_name_plural': 'Detalle Ventas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PurchaseDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio')),
                ('quantity', models.IntegerField(default=0, verbose_name='Cantidad')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Subtotal')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_details', to='bookings.product', verbose_name='Producto')),
                ('purchase_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_details', to='bookings.purchase')),
            ],
            options={
                'verbose_name': 'Detalle Compra',
                'verbose_name_plural': 'Detalle Compras',
                'ordering': ['id'],
            },
        ),
    ]
