from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    

class Color(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    


class Post(models.Model):
    title = models.CharField(max_length= 255) 
    # client = models.ForeignKey(CustumUser, on_delete= models.CASCADE)
    content = models.TextField()
    image1 = models.ImageField(upload_to= 'blog', null= True, blank= True)
    image2 = models.ImageField(upload_to= 'blog', null= True, blank= True)
    image3 = models.ImageField(upload_to= 'blog', null= True, blank= True)
    image4 = models.ImageField(upload_to= 'blog', null= True, blank= True)
    image5 = models.ImageField(upload_to= 'blog', null= True, blank= True)
    image6 = models.ImageField(upload_to= 'blog', null= True, blank= True)
    published_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    counted_views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)
    colors = models.ManyToManyField(Color)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('-created_date',)


# Create your models here.





