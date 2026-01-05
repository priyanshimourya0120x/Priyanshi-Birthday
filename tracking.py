import phonenumbers
from geopy.geocoders import Nominatim

def get_location(phone_number):
    # Parse the phone number
    parsed_number = phonenumbers.parse(phone_number, None)
    
    # Check if the number is valid
    if not phonenumbers.is_valid_number(parsed_number):
        return "Invalid phone number"
    
    # Get the country code
    country_code = phonenumbers.region_code_for_number(parsed_number)
    
    # Use geopy to get location based on country code
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(country_code)
    
    if location:
        return f"Location: {location.address}, Latitude: {location.latitude}, Longitude: {location.longitude}"
    else:
        return "Location not found"

# Example usage
phone_number = "+14155552671"  # Replace with the phone number you want to track
print(get_location(phone_number))