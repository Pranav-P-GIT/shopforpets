from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import PetProduct
from django.urls import reverse
class LatestNews(Feed):
    title="ShopForPets"
    link="/drcomments/"
    description="Pet food products available here."
    def items(self):
        return PetProduct.objects.all()[:4]
    def item_title(self,x):
        return x.name
    def item_description(self,y):
        return truncatewords(y.disc,10)
    def item_link(self,z):
        return reverse("homepage")