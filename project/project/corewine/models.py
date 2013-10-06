from django.db import models
APPROVED = 'Approved'
REJECTED = 'Rejected'
PENDING = 'Pending'

WINE_TYPES = (
    ('White', 'White'),
    ('Red', 'Red'),
    ('Rose', 'Rose'),
    ('Sparkling', 'Sparkling'),
)

STATUSES = (
    (APPROVED, 'Approved'),
    (REJECTED, 'Rejected'),
    (PENDING, 'Pending'),
)

SCALE = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)


class Acidity(models.Model):
    acidity = models.CharField(max_length=60)

    def __unicode__(self):
        return self.acidity


class Aroma(models.Model):
    aroma = models.CharField(max_length=60)
    wineType = models.CharField(max_length=60, choices=WINE_TYPES)

    def __unicode__(self):
        return '%s (%s)' % (self.aroma, self.wineType)


class Cepage(models.Model):
    APPROVED = 'Approved'
    REJECTED = 'Rejected'
    PENDING = 'Pending'

    STATUSES = (
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (PENDING, 'Pending'),
    )

    cepage = models.CharField(max_length=60)
    wineType = models.CharField(max_length=60, choices=WINE_TYPES)
    status = models.CharField(max_length=60, choices=STATUSES, default=PENDING)

    def is_approved(self):

        return self.status == 'Approved'
    is_approved.admin_order_field = 'status'
    is_approved.boolean = True
    is_approved.short_description = 'Approved ?'

    def __unicode__(self):
        return self.cepage


class Tag(models.Model):
    APPROVED = 'Approved'
    REJECTED = 'Rejected'
    PENDING = 'Pending'

    STATUSES = (
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (PENDING, 'Pending'),
    )

    tag = models.CharField(max_length=60)
    wineType = models.CharField(max_length=60, choices=WINE_TYPES)
    status = models.CharField(max_length=60, choices=STATUSES, default=PENDING)

    def is_approved(self):
        return self.status == REJECTED

    is_approved.boolean = True
    is_approved.short_description = 'Approved ?'

    def __unicode__(self):
        return '%s (%s)' % (self.tag, self.wineType)


class Taste(models.Model):
    taste = models.CharField(max_length=60)


class Tanin(models.Model):
    tanin = models.CharField(max_length=60)


class Teint(models.Model):
    teint = models.CharField(max_length=60)
    wineType = models.CharField(max_length=60, choices=WINE_TYPES)


class Wine(models.Model):
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
    wineType = models.CharField(max_length=60, choices=WINE_TYPES)
    rating = models.FloatField()

    teint = models.ForeignKey(Teint)
    aroma = models.ForeignKey(Aroma)
    taste = models.ForeignKey(Taste)
    acidity = models.ForeignKey(Acidity)
    tanin = models.ForeignKey(Tanin)
    cepage = models.ManyToManyField(Cepage)
    tag = models.ManyToManyField(Tag)
