

# Create your models here.
from django.db import models

class ElegantDecor(models.Model):
    vendor_id = models.CharField(max_length=100)
    member_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    category_id = models.CharField(max_length=100,null = True)
    vendor_currency = models.CharField(max_length=10,null = True)
    membership_id = models.CharField(max_length=100,null = True)
    new_slug = models.CharField(max_length=255,null = True)
    city = models.CharField(max_length=100,null = True)
    information = models.TextField(null = True)
    vendor_rating = models.CharField(max_length=10,null = True)
    reviews_count = models.CharField(max_length=100,null = True)
    vendor_price = models.CharField(max_length=100,null = True)
    starting_price_new = models.CharField(max_length=100,null = True)
    vendor_price_subtext = models.CharField(max_length=100,null = True)
    vendor_verification_status = models.BooleanField(null = True)
    vaccination_status = models.IntegerField(null = True)
    secret_deal_available = models.BooleanField(null = True)
    profile_pic_url = models.URLField(null = True)
    is_mynt = models.BooleanField(null = True)
    category_price_suffix_text = models.CharField(max_length=255,null = True)
    starting_price = models.CharField(max_length=100,null = True)
    show_badge_icon = models.BooleanField(null = True)

class CoverImage(models.Model):
    elegant_decor = models.ForeignKey(ElegantDecor, on_delete=models.CASCADE)
    image_url = models.URLField()

class CityPolygon(models.Model):
    elegant_decor = models.OneToOneField(ElegantDecor, on_delete=models.CASCADE)
    pinned_to_bottom = models.IntegerField(null = True)
    review_score = models.CharField(max_length=100,null = True)
    freshness_score = models.CharField(max_length=100,null = True)
    image_score = models.CharField(max_length=100,null = True)
    lrr_score = models.CharField(max_length=100,null = True)
    membership_id = models.CharField(max_length=100, null = True)
    score = models.CharField(max_length=100,null = True)
    city_slug = models.CharField(max_length=100,null = True)
    city_name = models.CharField(max_length=100,null = True)
    is_base_city = models.CharField(max_length=10,null = True)
# ```

# Now, here's the Python code to store the data:

# ```python

