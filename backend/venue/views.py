from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
import requests
from .models import Vendor, VenueImage, VenueCategory, CityPolygon, Tooltip, FAQ, VenueType, GuestCount, BadgeIcon, VenuePricing
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import VendorSerializer



def fetch_data(request):
    cities = ["Gurgaon","Udaipur","Agra","Kanpur","Kochi","Jaisalmer"]


    j = 0
    i = 1
    city = cities[j].lower()
    # print(cities)
    
    while True:
        
        Decor_URL = f"https://www.wedmegood.com/node/v1/vendor/list?category_slug=wedding-venues&city_slug={city}&filter_option=&offset=0&device_type=1&page={i}"

        # response = requests.get(Decor_URL)
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    }
        response = requests.get(Decor_URL, headers=headers, timeout=10)
        
        data = response.json()
        
        if data['data'] == []:
            j += 1
            try:
                city = cities[j].lower()
                print(city)
                i = 1
                continue
            except:
                break

            

        
        save_vendor_data(data)
        i += 1

    return HttpResponse(data['data'])


    

def save_vendor_data(json_data):
    
    for i in range (len(json_data.get('data', []))):
        data = json_data['data'][i]
        try:
            # Get the id safely
            vendor_id = data.get("id")
            print(vendor_id)
            if not vendor_id:
                raise ValueError("Vendor ID is missing from the data.")
            
            # Check if the vendor already exists in the database
            vendor, created = Vendor.objects.update_or_create(
                vendor_id=vendor_id,  
                defaults={
                    'name': data.get("name"),
                    'membership_id': data.get("membership_id"),
                    'city': data.get("city"),
                    'locality': data.get("locality"),
                    'information': data.get("information"),
                    'vendor_rating': data.get("vendor_rating"),
                    'reviews_count': data.get("reviews_count"),
                    'vendor_price': data.get("vendor_price"),
                    'vendor_price_subtext': data.get("vendor_price_subtext"),
                    'vendor_verification_status': data.get("vendor_verification_status"),
                    'vaccination_status': data.get("vaccination_status"),
                    'secret_deal_available': data.get("secret_deal_available"),
                    'profile_pic_url': data.get("profile_pic_url"),
                    'is_mynt': data.get("is_mynt"),
                    'starting_price': data.get("starting_price"),
                    'show_badge_icon': data.get("show_badge_icon")
                }
            )

            # Save venue images
            for image_url in data.get("cover_images", []):
                VenueImage.objects.update_or_create(vendor=vendor, image_url=image_url)

            # Save venue categories
            for category in data.get("venue_type", []):
                VenueCategory.objects.update_or_create(vendor=vendor, category_name=category)

            # Save city polygon data
            city_polygon = data.get("city_polygon", {})
            CityPolygon.objects.update_or_create(
                vendor=vendor,
                defaults={
                    'pinned_to_bottom': city_polygon.get("pinnedToBottom", 0),
                    'review_score': city_polygon.get("reviewScore", 0),
                    'freshness_score': city_polygon.get("freshnessScore", 0),
                    'image_score': city_polygon.get("imageScore", 0),
                    'lrr_score': city_polygon.get("lrrScore", 0),
                    'score': city_polygon.get("score", 0),
                    'city_slug': city_polygon.get("citySlug", ""),
                    'city_name': city_polygon.get("cityName", ""),
                    'is_base_city': city_polygon.get("isBaseCity", 0)
                }
            )

            # Save tooltips
            for tooltip in data.get("tooltip", []):
                Tooltip.objects.update_or_create(vendor=vendor, heading=tooltip.get("tooltip_heading", ""), description=tooltip.get("tooltip_heading_answer", ""))

            # Save FAQ data
            for faq in data.get("faq_texts_on_vendor_card", []):
                FAQ.objects.update_or_create(
                    vendor=vendor,
                    question=faq.get("filter_question", ""),
                    answer=faq.get("answerValue", ""),
                    faq_order=faq.get("faq_order_on_vc", 0)
                )

            # Save venue types
            for venue_type in data.get("venue_type", []):
                VenueType.objects.update_or_create(vendor=vendor, venue_type=venue_type)

            # Save guest count
            for guest_count in data.get("num_guest_count", []):
                GuestCount.objects.update_or_create(
                    vendor=vendor,
                    min_value=guest_count.get("min_value", ""),
                    max_value=guest_count.get("max_value", "")
                )

            # Save badge icons
            badge_icon = data.get("badge_icon", {})
            BadgeIcon.objects.update_or_create(
                vendor=vendor,
                web_icon=badge_icon.get("web", ""),
                android_hdmi=badge_icon.get("android", {}).get("hdmi", ""),
                android_mdpi=badge_icon.get("android", {}).get("mdpi", ""),
                ios_1x=badge_icon.get("ios", {}).get("1x", ""),
                ios_2x=badge_icon.get("ios", {}).get("2x", ""),
                is_new_badge=badge_icon.get("is_new_badge", False)
            )

            # Save pricing information
            VenuePricing.objects.update_or_create(
                vendor=vendor,
                destination_price_prefix=data.get("destination_price_prefix", ""),
                destination_price=data.get("destination_price", ""),
                destination_price_unit=data.get("destination_price_unit", ""),
                vendor_currency=data.get("vendor_currency", "")
            )

        except Exception as e:
            print(f"Error while saving data: {e}")




class VendorDetailView(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(vendor_id=vendor_id)
            serializer = VendorSerializer(vendor)
            return Response(serializer.data)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=404)


class CityVendorSearchView(APIView):
    def get(self, request, city_name):
        
        vendors = Vendor.objects.filter(city__iexact=city_name)
    
        # Implement pagination
        paginator = PageNumberPagination()
        paginator.page_size = 20  # Set the number of records per page
        paginated_vendors = paginator.paginate_queryset(vendors, request)

        # Serialize the paginated data
        serializer = VendorSerializer(paginated_vendors, many=True)
        return paginator.get_paginated_response(serializer.data)