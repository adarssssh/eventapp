

from django.db import models

class Vendor(models.Model):
    vendor_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    membership_id = models.CharField(max_length=255)
    city = models.CharField(max_length=255,null = True)
    locality = models.CharField(max_length=255,null = True)
    information = models.TextField(null = True)
    vendor_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0,null = True)
    reviews_count = models.IntegerField(default=0,null = True)
    vendor_price = models.CharField(max_length=255,null = True)
    vendor_price_subtext = models.CharField(max_length=255,null = True)
    vendor_verification_status = models.BooleanField(default=False,null = True)
    vaccination_status = models.BooleanField(default=False,null = True)
    secret_deal_available = models.BooleanField(default=False,null = True)
    profile_pic_url = models.URLField(null = True)
    is_mynt = models.BooleanField(default=False,null = True)
    starting_price = models.CharField(max_length=255,null = True)
    show_badge_icon = models.BooleanField(default=False,null = True)

class VenueImage(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='venue_images', on_delete=models.CASCADE)
    image_url = models.URLField(null = True)

class VenueCategory(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='categories', on_delete=models.CASCADE)
    category_name = models.CharField(max_length=255,null = True)

class CityPolygon(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='city_polygon', on_delete=models.CASCADE,null = True)
    pinned_to_bottom = models.CharField(max_length=100,default=0,null = True)
    review_score = models.DecimalField(max_digits=3, decimal_places=2, default=0,null = True)
    freshness_score = models.DecimalField(max_digits=3, decimal_places=2, default=0,null = True)
    image_score = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    lrr_score = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    score = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    city_slug = models.CharField(max_length=255)
    city_name = models.CharField(max_length=255)
    is_base_city = models.IntegerField(default=0)

class Tooltip(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='tooltips', on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    description = models.TextField()

class FAQ(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='faqs', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    faq_order = models.IntegerField()

class VenueType(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='venue_types', on_delete=models.CASCADE)
    venue_type = models.CharField(max_length=255)

class GuestCount(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='guest_counts', on_delete=models.CASCADE)
    min_value = models.IntegerField()
    max_value = models.IntegerField()

class BadgeIcon(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='badge_icons', on_delete=models.CASCADE)
    web_icon = models.URLField()
    android_hdmi = models.URLField()
    android_mdpi = models.URLField()
    ios_1x = models.URLField()
    ios_2x = models.URLField()
    is_new_badge = models.BooleanField(default=False)

class VenuePricing(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='pricing', on_delete=models.CASCADE)
    destination_price_prefix = models.CharField(max_length=255)
    destination_price = models.CharField(max_length=255)
    destination_price_unit = models.CharField(max_length=255)
    vendor_currency = models.CharField(max_length=255)

