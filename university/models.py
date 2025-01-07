from django.db import models

#model to store the university detail
class University(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    rank = models.IntegerField(null=True, blank=True) 
    website = models.URLField()
    image=models.URLField(blank=True, null=True)
    established_year = models.IntegerField()
    admission_requirements = models.TextField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    accreditation = models.CharField(max_length=255, null=True, blank=True)  

    def __str__(self):
        return self.name
    
#model to store the category of the courses
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


#model to store the course detail
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=50) 
    level = models.CharField(max_length=50)  
    university = models.ForeignKey(University, related_name='courses', on_delete=models.CASCADE)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    prerequisites = models.TextField()
    credits = models.IntegerField()
    start_date = models.DateField()
    application_deadline = models.DateField()
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.university.name})"
    
