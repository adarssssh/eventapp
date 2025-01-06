from django.http import HttpResponse,HttpRequest
from django.shortcuts import render
from .models import ElegantDecor,CoverImage,CityPolygon
import requests
# Create your views here.





def fetch_data(request):
    cities = [
    'Kochi', 'Jaisalmer', 
    'kozhikode-calicut', 'Nagpur', 'Dehradun', 'Patna', 'Thane', 'Surat', 
    'Vadodara', 'Raipur', 'Mysore', 'Hubli', 'Dhitara', 'Kerala', 'Rajasthan', 
    'Himachal Pradesh', 'Maharashtra', 'Haryana', 'Uttar Pradesh', 'Uttarakhand', 
    'Punjab', 'Manipur', 'Arunachal Pradesh', 'Dubai', 'Thailand', 'Bali', 
    'Abu Dhabi'
    ]

    j = 0
    i = 1
    city = cities[j].lower()
    print(cities)
    while True:
        
        Decor_URL = f"https://www.wedmegood.com/node/v1/vendor/list?category_slug=wedding-decorators&city_slug={city}&filter_option=&offset=0&device_type=1&page={i}"

        # response = requests.get(Decor_URL)
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    }
        response = requests.get(Decor_URL, headers=headers, timeout=10)
        
        data = response.json()
        print(data)
        if data['data'] == []:
            j += 1
            try:
                city = cities[j].lower()
                print(city)
                i = 1
                continue
            except:
                break

            

        
        store_elegant_decor_data(data)
        i += 1

    return HttpResponse(data['data'])



def store_elegant_decor_data(json_data):

    for i in range (len(json_data.get('data', []))):
        data = json_data['data'][i]
        
        # Create main record
        existing_elegant_decor = ElegantDecor.objects.filter(vendor_id=data.get('id')).first()

        if not existing_elegant_decor:  # If no existing record found, create a new one
            # Create main record for ElegantDecor
            elegant_decor = ElegantDecor.objects.create(
                vendor_id=data.get('id'),
                member_id=data.get('member_id', 'Not Available'),
                name=data.get('name'),
                category_id=data.get('category_id'),
                vendor_currency=data.get('vendor_currency'),
                membership_id=data.get('membership_id'),
                new_slug=data.get('new_slug'),
                city=data.get('city'),
                information=data.get('information'),
                vendor_rating=data.get('vendor_rating', 'Not Available'),
                reviews_count=data.get('reviews_count', 'Not Available'),
                vendor_price=data.get('vendor_price', 'Not Available'),
                starting_price_new=data.get('starting_price_new', 'Not Available'),
                vendor_price_subtext=data.get('vendor_price_subtext', 'Not Available'),  # Added default
                vendor_verification_status=data.get('vendor_verification_status', 'Not Available'),  # Added default
                vaccination_status=data.get('vaccination_status', 'Not Available'),  # Added default
                secret_deal_available=data.get('secret_deal_available', 'Not Available'),  # Added default
                profile_pic_url=data.get('profile_pic_url', 'Not Available'),  # Added default
                is_mynt=data.get('is_mynt', 'Not Available'),  # Added default
                category_price_suffix_text=data.get('category_price_suffix_text', 'Not Available'),  # Added default
                starting_price=data.get('starting_price', 'Not Available'),  # Added default
                show_badge_icon=data.get('show_badge_icon', 'Not Available')  # Added default
            )

            # Store cover images (Ensure it's a list before iterating)
            cover_images = data.get('cover_images', [])  # Default to an empty list if missing
            for image_url in cover_images:
                CoverImage.objects.create(
                    elegant_decor=elegant_decor,
                    image_url=image_url
                )

            # Store city polygon data (Ensure it's a dictionary)
            city_polygon = data.get('city_polygon', {})  # Default to an empty dictionary if missing
            CityPolygon.objects.create(
                elegant_decor=elegant_decor,
                pinned_to_bottom=city_polygon.get('pinnedToBottom'),  # Add default
                review_score=city_polygon.get('reviewScore', 'Not Available'),
                freshness_score=city_polygon.get('freshnessScore', 'Not Available'),
                image_score=city_polygon.get('imageScore', 'Not Available'),
                lrr_score=city_polygon.get('lrrScore', 'Not Available'),
                membership_id=city_polygon.get('membershipId', 'Not Available'),
                score=city_polygon.get('score', 'Not Available'),
                city_slug=city_polygon.get('citySlug', 'Not Available'),
                city_name=city_polygon.get('cityName', 'Not Available'),
                is_base_city=city_polygon.get('isBaseCity', 'Not Available')
            )