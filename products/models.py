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
    counted_views = models.IntegerField(default=0)
    sells = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)
    colors = models.ManyToManyField(Color)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('-created_date',)














class Comments(models.Model):
    which_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_date",)

    def __str__(self):
        return self.name
    


class Replay(models.Model):
    which_comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_date",)

    def __str__(self):
        return str(self.which_comment)


# Create your models here.






