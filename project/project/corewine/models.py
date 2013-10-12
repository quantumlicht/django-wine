from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

SCALE = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)
# ==================================================
#  VALIDATOR CLASSES
# ==================================================
validate_non_numeric = RegexValidator(regex='^[a-zA-Z\s-]*$',
                                      message='Expression contains numeric values',
                                      code='no_numeric_expected'
                                      )
validate_numeric_only = RegexValidator(regex='^[0-9\s-]*$',
                                      message='Expression contains letters',
                                      code='numeric_only_expected'
                                      )

# ==================================================
#  ABSTRACT CLASSES
# ==================================================


class Orderable(models.Model):
    order = models.IntegerField()

    class Meta:
        abstract = True


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
#  PRIVATE MODEL CLASSES (EXPOSED TO ADMIN ONLY)
# ==================================================

class Acidity(Orderable):
    acidity = models.CharField(max_length=60,
                               unique=True
                               )

    def __unicode__(self):
        return self.acidity


class Aroma(Orderable):
    aroma = models.CharField(max_length=60,
                             unique=True
                             )

    def __unicode__(self):
        return self.aroma


class Tanin(Orderable):
    tanin = models.CharField(max_length=60,
                             unique=True
                             )

    def __unicode__(self):
        return self.tanin


class Teint(WineType, Orderable):
    teint = models.CharField(max_length=60,
                             unique=True
    
                             )
    def __unicode__(self):
        return self.teint


class Taste(Orderable):
    taste = models.CharField(max_length=60,
                             unique=True
                             )

    def __unicode__(self):
        return self.taste
# ==================================================
#  PUBLIC MODEL CLASSES (EXPOSED TO FORMS)
# ==================================================


class Cepage(Approvable, WineType):
    cepage = models.CharField(max_length=60,
                              validators=[validate_non_numeric])

    def __unicode__(self):
        return self.cepage


class Tag(Approvable, WineType):
    tag = models.CharField(max_length=60,
                           validators=[validate_non_numeric],
                           unique=True
                           )
    description = models.CharField(max_length=300)

    def __unicode__(self):
        return '%s (%s)' % (self.tag, self.wineType)


class Wine(WineType):
    name = models.CharField(max_length=100,
                            unique=True
                            )
    producer = models.CharField(max_length=100)
    year = models.IntegerField()
    appelation = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    alcool = models.FloatField()
    date = models.DateTimeField('Tasting Date')
    code_saq = models.CharField(unique=True,
                                 max_length=255,
                                validators=[validate_numeric_only]
        )
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


    def list_cepage(obj):
        list_cepage = ', '.join([x.__unicode__() for x in obj.cepage.all() if x.is_approved()])
        return list_cepage

    list_cepage.admin_order_field = 'name'
    list_cepage.boolean = False
    list_cepage.short_description = 'Cepages'
