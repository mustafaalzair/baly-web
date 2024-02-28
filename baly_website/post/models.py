from django.db import models

# Create your models here.

typPost = {
    ('logo', 'Logo'),
    ('competition', 'Competition'),
    ('post', 'Post'),
    ('video', 'video')
}


class posts(models.Model):


    post=models.CharField( max_length=150)
    type=models.CharField(max_length=150,choices=typPost)
    description=models.TextField()
    image=models.ImageField( upload_to='image/', height_field=None, width_field=None, max_length=None,blank=False,null=False)
    title=models.CharField( max_length=150,blank=True,null=True)
    link=models.CharField( max_length=150,blank=True,null=True)
 
    def __str__(self):
        return self.post
    
        