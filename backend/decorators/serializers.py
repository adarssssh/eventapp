from .models import *
from rest_framework import serializers



class DecorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverImage
        fields = ['image_url']


class CityPolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityPolygon
        fields = ['city_slug', 'city_name', 'score', 'review_score']


class DecorSerializer(serializers.ModelSerializer):
    venue_images = DecorImageSerializer(many=True, read_only=True)
    city_polygon = CityPolygonSerializer(many=True, read_only=True)
    

    class Meta:
        model = ElegantDecor
        fields = [
            'vendor_id', 'name', 'membership_id','category_id', 'city', 'information',
            'vendor_rating', 'reviews_count', 'vendor_price', 'vendor_price_subtext',
            'vendor_verification_status', 'vaccination_status', 'secret_deal_available',
            'profile_pic_url', 'is_mynt', 'starting_price', 'show_badge_icon',
            'venue_images', 'city_polygon'
        ]


