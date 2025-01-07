
from supabase import create_client
from django.conf import settings
import io
from decouple import config

def upload_image_to_supabase(image_file, file_name):
    # Initialize the Supabase client
    supabase = create_client(config('SUPABASE_URL'), config('SUPABASE_API_KEY'))

    image_data = image_file.read()

    # Upload image to Supabase storage
    response = supabase.storage.from_('university-logos').upload(f'{file_name}.jpg', image_data)

    if response.status_code == 200:
        # Generate the public URL of the uploaded image
        image_url = supabase.storage.from_('university-logos').get_public_url(f'{file_name}.jpg').public_url
        return image_url
    else:
        raise Exception('Error uploading image to Supabase')
