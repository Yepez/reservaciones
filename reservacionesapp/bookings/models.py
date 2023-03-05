from django.db import models
from .choices import STATUS_CHOICE


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripción')
    status = models.CharField(
        max_length=35,
        null=False,
        choices=STATUS_CHOICE,
    )
    created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='Fecha Creación')
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.CharField(max_length=200, null=False, verbose_name='Clave')
    description = models.TextField(blank=True, verbose_name='Nombre')
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio')
    available = models.IntegerField(null=True, verbose_name='Disponible')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Categoría'
    )
    has_vat = models.BooleanField(null=True, verbose_name='Tiene Iva')
    status = models.CharField(
        max_length=35,
        null=False,
        choices=STATUS_CHOICE,
    )
    created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='Fecha Creación')
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

    def __str__(self):
        return self.description

    @classmethod
    def productosRegistrados(self):
        objetos = self.objects.all().order_by('descripcion')
        return objetos

    @classmethod
    def preciosProductos(self):
        objetos = self.objects.all().order_by('id')
        arreglo = []
        etiqueta = True
        extra = 1

        for indice, objeto in enumerate(objetos):
            arreglo.append([])
            if etiqueta:
                arreglo[indice].append(0)
                arreglo[indice].append("------")
                etiqueta = False
                arreglo.append([])

            arreglo[indice + extra].append(objeto.id)
            precio_producto = objeto.precio
            arreglo[indice + extra].append("%d" % (precio_producto))

        return arreglo


class Purchase(models.Model):
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='Fecha')
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}'

    @property
    def get_total(self):
        if self.pk:
            pd = self.purchase_details.filter(purchase_id=self.pk).values_list('price', 'quantity') or 0
            t = 0 if isinstance(pd, int) else sum(map(lambda q: q[0] * q[1], pd))
            return t
        else:
            return 0

    def save(self):
        self.total = self.get_total
        super(Purchase, self).save()


class PurchaseDetail(models.Model):
    purchase_id = models.ForeignKey(
        Purchase,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="purchase_details"
    )
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Producto',
        related_name='purchase_details'
    )
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio')
    quantity = models.IntegerField(default=0, verbose_name='Cantidad')
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Subtotal')
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        verbose_name = 'Detalle Compra'
        verbose_name_plural = 'Detalle Compras'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk} - {self.purchase_id.pk} - {self.product_id}'

    @property
    def get_subtotal(self):
        return self.quantity * (self.price or 0)

    def save(self):
        self.subtotal = self.get_subtotal
        super(PurchaseDetail, self).save()


class Sale(models.Model):
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='Fecha')
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}'

    @property
    def get_total(self):
        if self.pk:
            sd = self.sale_details.filter(sale_id=self.pk).values_list('price', 'quantity') or 0
            t = 0 if isinstance(sd, int) else sum(map(lambda q: q[0] * q[1], sd))
            return t
        else:
            return 0

    def save(self):
        self.total = self.get_total
        super(Sale, self).save()


class SaleDetail(models.Model):
    sale_id = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="sale_details"
    )
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Producto',
        related_name='sale_details'
    )
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio')
    quantity = models.IntegerField(default=0, verbose_name='Cantidad')
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Subtotal')
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalle Ventas'
        ordering = ['id']

    @property
    def get_subtotal(self):
        return self.quantity * (self.price or 0)

    def save(self):
        self.subtotal = self.get_subtotal
        super(SaleDetail, self).save()


class Store(models.Model):
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="stores")
    quantity = models.IntegerField(null=False, verbose_name='Cantidad')
    price = models.FloatField(null=False, verbose_name='Precio')
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        verbose_name = 'Almacén'
        verbose_name_plural = 'Almacenes'
        ordering = ['id']
