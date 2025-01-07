from rest_framework import serializers
from .models import University,Category,Course
from .utils import upload_image_to_supabase

#serializer for university
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = [  'id',
                    'name',
                    'location', 
                    'established_year', 
                    'website', 
                    'image',
                    'admission_requirements',
                    'contact_email',
                    'contact_phone',
                    'accreditation',
                    'rank',
                ]

    #function to handle the image upload to supabase
    def create(self, validated_data):
        image = validated_data.pop('image', None)

        # If image is provided, upload it to Supabase
        if image:
            file_name = validated_data['name']  # You can use the university name or any other unique identifier
            image_url = upload_image_to_supabase(image, file_name)
            validated_data['image_url'] = image_url

        return super().create(validated_data)


#serializer for course
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['name',
                'description',
                'duration',
                'level',
                'university',
                'fees',
                'prerequisites',
                'credits',
                'start_date',
                'application_deadline',
                'category',
            ]
        

#serializer for category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name',
                'description',
                'active',
                'created_at',
                'updated_at'
            ]
        