from django.db import models

class Slideshows(models.Model):
    title = models.CharField(max_length=1000)
    desc = models.CharField(max_length=2000)
    pictureLocation = models.CharField(max_length=200)
    isActive = models.BooleanField()
    slideshow_id = models.IntegerField()
    order_id = models.IntegerField()
    pub_date = models.DateTimeField('date_pubished')

    def __unicode__(self):
        return "Title: \"%s\" for Slideshow: \"%s\"" % (self.title, str(self.slideshow_id))
