from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.core.exceptions import ObjectDoesNotExist
import requests
from .models import Vendor, VenueImage, VenueCategory, CityPolygon, Tooltip, FAQ, VenueType, GuestCount, BadgeIcon, VenuePricing





def fetch_data(request):
    cities = [
    'Himachal-Pradesh', 'Maharashtra', 'Haryana', 'Uttar-Pradesh', 'Uttarakhand', 
    'Punjab', 'Manipur', 'Arunachal-Pradesh', 'Dubai', 'Thailand', 'Bali', 
    'Abu Dhabi'
    ]


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

# def save_vendor_data(data):
    try:
        # Check if the vendor already exists in the database
        vendor, created = Vendor.objects.update_or_create(
            vendor_id=data["id"],  # Assuming the vendor_id is unique
            defaults={
                'name': data["name"],
                'membership_id': data["membership_id"],
                'city': data["city"],
                'locality': data["locality"],
                'information': data["information"],
                'vendor_rating': data["vendor_rating"],
                'reviews_count': data["reviews_count"],
                'vendor_price': data["vendor_price"],
                'vendor_price_subtext': data["vendor_price_subtext"],
                'vendor_verification_status': data["vendor_verification_status"],
                'vaccination_status': data["vaccination_status"],
                'secret_deal_available': data["secret_deal_available"],
                'profile_pic_url': data["profile_pic_url"],
                'is_mynt': data["is_mynt"],
                'starting_price': data["starting_price"],
                'show_badge_icon': data["show_badge_icon"]
            }
        )

        # Save venue images
        for image_url in data["cover_images"]:
            VenueImage.objects.update_or_create(vendor=vendor, image_url=image_url)

        # Save venue categories
        for category in data["venue_type"]:
            VenueCategory.objects.update_or_create(vendor=vendor, category_name=category)

        # Save city polygon data
        CityPolygon.objects.update_or_create(
            vendor=vendor,
            defaults={
                'pinned_to_bottom': data["city_polygon"]["pinnedToBottom"],
                'review_score': data["city_polygon"]["reviewScore"],
                'freshness_score': data["city_polygon"]["freshnessScore"],
                'image_score': data["city_polygon"]["imageScore"],
                'lrr_score': data["city_polygon"]["lrrScore"],
                'score': data["city_polygon"]["score"],
                'city_slug': data["city_polygon"]["citySlug"],
                'city_name': data["city_polygon"]["cityName"],
                'is_base_city': data["city_polygon"]["isBaseCity"]
            }
        )

        # Save tooltips
        for tooltip in data["tooltip"]:
            Tooltip.objects.update_or_create(vendor=vendor, heading=tooltip["tooltip_heading"], description=tooltip["tooltip_heading_answer"])

        # Save FAQ data
        for faq in data["faq_texts_on_vendor_card"]:
            FAQ.objects.update_or_create(
                vendor=vendor,
                question=faq["filter_question"],
                answer=faq["answerValue"],
                faq_order=faq["faq_order_on_vc"]
            )

        # Save venue types
        for venue_type in data["venue_type"]:
            VenueType.objects.update_or_create(vendor=vendor, venue_type=venue_type)

        # Save guest count
        for guest_count in data["num_guest_count"]:
            GuestCount.objects.update_or_create(
                vendor=vendor,
                min_value=guest_count["min_value"],
                max_value=guest_count["max_value"]
            )

        # Save badge icons
        BadgeIcon.objects.update_or_create(
            vendor=vendor,
            web_icon=data["badge_icon"]["web"],
            android_hdmi=data["badge_icon"]["android"]["hdmi"],
            android_mdpi=data["badge_icon"]["android"]["mdpi"],
            ios_1x=data["badge_icon"]["ios"]["1x"],
            ios_2x=data["badge_icon"]["ios"]["2x"],
            is_new_badge=data["badge_icon"]["is_new_badge"]
        )

        # Save pricing information
        VenuePricing.objects.update_or_create(
            vendor=vendor,
            destination_price_prefix=data["destination_price_prefix"],
            destination_price=data["destination_price"],
            destination_price_unit=data["destination_price_unit"],
            vendor_currency=data["vendor_currency"]
        )

    except Exception as e:
        print(f"Error while saving data: {e}")

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
