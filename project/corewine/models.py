from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
import logging
from .managers import WineManager


log = logging.getLogger(__name__) 

SCALE = [ (0.5*x, 0.5*x) for x in xrange(1,11) ]

YEARS  = [(x,x) for x in xrange(timezone.now().year, 1899, -1)]

# ==================================================
#  VALIDATOR CLASSES
# ==================================================
validate_non_numeric = RegexValidator(regex='^[a-zA-Z\s-]*$',
                                      message=_('Expression should not contain numeric values'),
                                      code='no_numeric_expected'
                                      )
validate_numeric_only = RegexValidator(regex='^[0-9\s-]*$',
                                      message=_('Expression contains letters'),
                                      code='numeric_only_expected'
                                      )

validate_float_string = RegexValidator(regex='^\d+\.?\d+$',
                                      message=_('This is not a valid number'),
                                      code='not_float_formatted'
                                      )
validate_price = RegexValidator(regex='^\d+\.?\d{1,2}$',
                                      message=_('This is not a valid price. 2 decimals maximum and numbers only is allowed.'),
                                      code='not_float_formatted'
                                      )

validate_percentage = RegexValidator(regex='^\d{1,2}\.?\d{1,2}$',
                                      message=_('This is not a valid percentage. Maximum is 100% and only put 1 decimal maximum.'),
                                      code='not_float_formatted'
                                      )
# ==================================================
#  ABSTRACT CLASSES
# ==================================================
class Timestamp(models.Model):
    last_modified = models.DateTimeField(_('Last Modified'), auto_now=True, default=timezone.now())
    created = models.DateTimeField(_('Creation Date'),  auto_now_add=True, default=timezone.now())
    
    class Meta:
        abstract = True


class Orderable(models.Model):
    order = models.IntegerField()

    class Meta:
        abstract = True


class WineType(models.Model):

    class Meta:
        abstract = True

    WINE_TYPES = (
        ('White', _('White')),
        ('Red', _('Red'))
    )
    wineType = models.CharField(max_length=60, choices=WINE_TYPES, verbose_name=_('Wine Type'))


class Approvable(models.Model):
    APPROVED = 'a'
    REJECTED = 'r'
    PENDING = 'p'

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
    class Meta:
        verbose_name_plural = _('Acidities')

    acidity = models.CharField(max_length=60,
                               unique=True,
                               verbose_name=_('Acidity')
                               )

    def __unicode__(self):
        return self.acidity


class Aroma(Orderable):
    """

    Aromas related to :model:`corewine.Wine`
    
    """
    aroma = models.CharField(max_length=60,
                             unique=True,
                             verbose_name=_('Aroma')
                             )

    class Meta:
        verbose_name_plural = _('Aromas')

    def __unicode__(self):
        return self.aroma


class Country(Approvable):
    country = models.CharField(max_length=250,
                               unique=True,
                               verbose_name=_('Country')
                               )
    
    class Meta:
        verbose_name_plural = _('Countries')
    
    def __unicode__(self):
        return self.country


class Tanin(Orderable):
    tanin = models.CharField(max_length=60,
                             unique=True,
                             verbose_name=_('Tanin')
                             )

    def __unicode__(self):
        return self.tanin


class Teint(WineType, Orderable):
    teint = models.CharField(max_length=60,
                             unique=True,
                             verbose_name=_('Teint')
                             )
    def __unicode__(self):
        return self.teint


class Taste(Orderable):
    taste = models.CharField(max_length=60,
                             unique=True,
                             verbose_name=_('Taste')
                             )

    class Meta:
        verbose_name_plural = _('Tastes')

    def __unicode__(self):
        return self.taste
# ==================================================
#  PUBLIC MODEL CLASSES (EXPOSED TO FORMS)
# ==================================================


class Cepage(Approvable, WineType, Timestamp):
    cepage = models.CharField(max_length=60,
                              validators=[validate_non_numeric],
                              verbose_name=_('Cepage')
                              )
    

    def __unicode__(self):
        return self.cepage


class Tag(Approvable, WineType ,Timestamp):
    tag = models.CharField(max_length=60,
                           validators=[validate_non_numeric],
                           unique=True
                           )
    description = models.CharField(max_length=300)

    def __unicode__(self):
        return self.tag


class Wine(WineType, Timestamp):
    # FIELDS
    
    log.debug('test Wine')
    name = models.CharField(max_length=100,
                            unique=True,
                            verbose_name=_('Name')
                            )
    
    producer = models.CharField(max_length=100,
                                verbose_name=_('Producer'),
                                validators=[validate_non_numeric])
    
    year = models.IntegerField(choices=YEARS, verbose_name=_('Year') )
    
    appelation = models.CharField(max_length=100,
                                  verbose_name=_('Appelation'),
                                  validators=[validate_non_numeric]
                                 )

    country = models.ForeignKey(Country, verbose_name=_('Country'))

    region = models.CharField(max_length=100,
                              verbose_name=_('Region'),
                              validators=[validate_non_numeric]
                             )
    alcool = models.FloatField(verbose_name=_('Alcool'),
                               validators=[validate_percentage]
                              )

    date = models.DateField(_('Tasting Date'))
    
    code_saq = models.CharField(unique=True,
                                max_length=255,
                                verbose_name=_('SAQ Code'),
                                validators=[validate_numeric_only]
                                )

    price = models.FloatField(verbose_name=_('Price'),
                              validators=[validate_price])

    mouth_intensity = models.DecimalField(choices=SCALE, max_digits=2, decimal_places=1, verbose_name=_('Mouth Intensity'))
    nose_intensity = models.DecimalField(choices=SCALE, max_digits=2, decimal_places=1, verbose_name=_('Nose Intensity'))
    persistance = models.DecimalField(choices=SCALE, max_digits=2, decimal_places=1, verbose_name=_('Persistance'))
    rating = models.DecimalField(choices=SCALE, max_digits=3, decimal_places=1, verbose_name=_('Rating'))

    teint = models.ForeignKey(Teint, verbose_name=_('Teint'))
    aroma = models.ForeignKey(Aroma, verbose_name=_('Aroma'))
    taste = models.ForeignKey(Taste, verbose_name=_('Taste'))
    acidity = models.ForeignKey(Acidity, verbose_name=_('Acidity'))
    tanin = models.ForeignKey(Tanin, verbose_name=_('Tanin'), blank=True)
    cepage = models.ManyToManyField(Cepage, verbose_name=_('Cepage'))
    tag = models.ManyToManyField(Tag, blank=True, null=True, verbose_name=_('Tags'))

    # MANAGER
    objects = WineManager()


    # MODEL METHODS
    def list_cepage(obj):
        list_cepage = ', '.join([x.__unicode__() for x in obj.cepage.all() if x.is_approved()])
        return list_cepage

    list_cepage.admin_order_field = 'name'
    list_cepage.boolean = False
    list_cepage.short_description = _('Cepages')

    def list_tag(obj):
        list_tag = ', '.join([x.__unicode__() for x in obj.tag.all() if x.is_approved()])
        return list_tag

    list_tag.admin_order_field = 'name'
    list_tag.boolean = False
    list_tag.short_description = _('Tags')


    def arr_cepage(obj):
        return [x.__unicode__() for x in obj.cepage.all() if x.is_approved()]
    
    def arr_tag(obj):
        return [x.__unicode__() for x in obj.tag.all() if x.is_approved()]




