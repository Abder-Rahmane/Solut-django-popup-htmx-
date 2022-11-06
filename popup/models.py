from django.db import models


class EightiesKidsTVShows(models.Model):
    name = models.CharField(max_length=64)
    decade = models.IntegerField(default=1980)
    blurb = models.TextField()
    url = models.URLField()
    image_url = models.URLField()


class HubriseOrder(models.Model):
    id_order = models.CharField(max_length=999, null=True, blank=True)
    status = models.CharField(max_length=999, null=True, blank=True)
    service_type = models.CharField(max_length=999, null=True, blank=True)
    email = models.CharField(max_length=999, null=True, blank=True)
    first_name = models.CharField(max_length=999, null=True, blank=True)
    last_name = models.CharField(max_length=999, null=True, blank=True)
    phone = models.CharField(max_length=999, null=True, blank=True)
    address_1 = models.CharField(max_length=999, null=True, blank=True)
    address_2 = models.CharField(max_length=999, null=True, blank=True)
    postal_code = models.CharField(max_length=999, null=True, blank=True)
    city = models.CharField(max_length=999, null=True, blank=True)
    namePaiement = models.CharField(max_length=999, null=True, blank=True)
    amount = models.CharField(max_length=999, null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, auto_now=False, null=True, blank=True)
    created_by = models.CharField(max_length=999, blank=True)
    expected_time = models.DateTimeField(
        auto_now_add=True, auto_now=False, null=True, blank=True)
    pictureplatform = models.CharField(max_length=999, blank=True)
    statuscolor = models.CharField(max_length=999, blank=True)


class HubriseOrderItem(models.Model):
    id_order_item = models.CharField(max_length=999, null=True, blank=True)
    HubriseOrderId = models.ForeignKey(
        HubriseOrder, on_delete=models.CASCADE, related_name='entries')
    product_name = models.CharField(max_length=999, null=True, blank=True)
    priceProduct = models.CharField(max_length=999, null=True, blank=True)
    quantityProduct = models.CharField(max_length=999, null=True, blank=True)


class HubriseOrderItemOption(models.Model):
    id_order_item_option = models.CharField(
        max_length=999, null=True, blank=True)
    HubriseOrderItemId = models.ForeignKey(
        HubriseOrderItem, on_delete=models.CASCADE, related_name='entriesoption')
    nameOption = models.CharField(max_length=999, null=True, blank=True)
    priceOption = models.CharField(max_length=999, null=True, blank=True)
    quantityOption = models.CharField(max_length=999, null=True, blank=True)
