from rest_framework import serializers
from .models import *

# Serializer for VenueImage
class VenueImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueImage
        fields = ['image_url']

# Serializer for VenueCategory
class VenueCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueCategory
        fields = ['category_name']

# Serializer for CityPolygon
class CityPolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityPolygon
        fields = ['city_slug', 'city_name', 'score', 'review_score']

# Serializer for Tooltip
class TooltipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tooltip
        fields = ['heading', 'description']

# Serializer for Vendor (with nested serializers)
class VendorSerializer(serializers.ModelSerializer):
    venue_images = VenueImageSerializer(many=True, read_only=True)
    categories = VenueCategorySerializer(many=True, read_only=True)
    city_polygon = CityPolygonSerializer(many=True, read_only=True)
    tooltips = TooltipSerializer(many=True, read_only=True)

    class Meta:
        model = Vendor
        fields = [
            'vendor_id', 'name', 'membership_id', 'city', 'locality', 'information',
            'vendor_rating', 'reviews_count', 'vendor_price', 'vendor_price_subtext',
            'vendor_verification_status', 'vaccination_status', 'secret_deal_available',
            'profile_pic_url', 'is_mynt', 'starting_price', 'show_badge_icon',
            'venue_images', 'categories', 'city_polygon', 'tooltips'
        ]
