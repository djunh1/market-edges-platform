from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from users.models import Profile

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class Portfolio(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tag',  blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset



class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    # One comment on a portfolio per user
    # class Meta:
    #     unique_together = [['owner', 'portfolio']]

    def __str__(self):
        return self.value
    
    class Meta:
        ordering = ['-created']
    
class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Stock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    ticker = models.CharField(max_length=6)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    company_name = models.TextField(null=True, blank=True)
    sector = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.portfolio.name + '_' + self.ticker

    class Meta:
        ordering = ['ticker']

    
    

