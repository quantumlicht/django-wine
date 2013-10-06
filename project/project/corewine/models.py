from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

SCALE = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)
# ==================================================
#  VALIDATOR CLASSES
# ==================================================
validate_non_numeric = RegexValidator(regex='[^0-9]*',
                                      message='Expression contains numeric values',
                                      code='no_numeric_expected'
                                      )

# ==================================================
#  ABSTRACT CLASSES
# ==================================================


class WineType(models.Model):

    class Meta:
        abstract = True

    WINE_TYPES = (
        ('White', 'White'),
        ('Red', 'Red'),
        ('Rose', 'Rose'),
        ('Sparkling', 'Sparkling'),

    )
    wineType = models.CharField(max_length=60, choices=WINE_TYPES)


class Approvable(models.Model):
    APPROVED = 'Approved'
    REJECTED = 'Rejected'
    PENDING = 'Pending'

    class Meta:
        abstract = True

    STATUSES = (
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (PENDING, 'Pending'),
    )
    status = models.CharField(max_length=60, choices=STATUSES, default=PENDING)

    def is_approved(self):
        return self.status == self.APPROVED

    is_approved.admin_order_field = 'status'
    is_approved.boolean = True
    is_approved.short_description = 'Approved ?'


# ==================================================
#  MODEL CLASSES
# ==================================================

class Acidity(models.Model):
    acidity = models.CharField(max_length=60)

    def __unicode__(self):
        return self.acidity


class Aroma(WineType):
    aroma = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s (%s)' % (self.aroma, self.wineType)


class Cepage(Approvable, WineType):
    cepage = models.CharField(max_length=60,
                              validators=[validate_non_numeric])

    def __unicode__(self):
        return self.cepage


class Tag(Approvable, WineType):
    tag = models.CharField(max_length=60,
                           validators=[validate_non_numeric])

    def __unicode__(self):
        return '%s (%s)' % (self.tag, self.wineType)


class Taste(models.Model):
    taste = models.CharField(max_length=60)

    def __unicode__(self):
        return self.taste


class Tanin(models.Model):
    tanin = models.CharField(max_length=60)

    def __unicode__(self):
        return self.tanin


class Teint(WineType):
    teint = models.CharField(max_length=60)


class Wine(WineType):
    name = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    year = models.IntegerField()
    appelation = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    alcool = models.FloatField()
    date = models.DateTimeField('Tasting Date')
    code_saq = models.IntegerField()
    price = models.FloatField()
    nose_intensity = models.IntegerField(choices=SCALE)
    mouth_intensity = models.IntegerField(choices=SCALE)
    persistance = models.IntegerField(choices=SCALE)
    rating = models.FloatField()

    teint = models.ForeignKey(Teint)
    aroma = models.ForeignKey(Aroma)
    taste = models.ForeignKey(Taste)
    acidity = models.ForeignKey(Acidity)
    tanin = models.ForeignKey(Tanin)
    cepage = models.ManyToManyField(Cepage)
    tag = models.ManyToManyField(Tag)
