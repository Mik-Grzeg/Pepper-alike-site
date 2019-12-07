from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
# ----------------------Models----------------------------------------------


class Category(models.Model):
    """
    Model of a category of items,
    contains also subcategories
    """
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def getting_parent_category(self):
        while self.parent is not None:
            self = self.parent
        return self


class Item(models.Model):
    """
    Model of an item with reduced price.
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    original_price = models.FloatField(blank=True, null=True)
    retail_price = models.FloatField(blank=True, null=True)
    still_up_to_date = models.BooleanField(default=True)
    pub_date = models.DateTimeField(default=timezone.now)
    img = models.ImageField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % slugify(self.title)

    class Meta:
        ordering = ['-pub_date']

# ----------------------Models----------------------------------------------
