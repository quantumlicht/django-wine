"""
py:module:: corewine

"""
import logging
from django.db import models
from django.utils import timezone
from core.validators import * 
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from .managers import ApprovedManager
from taggit.managers import TaggableManager

log = logging.getLogger(__name__) 

SCALE = [ (0.5*x, 0.5*x) for x in xrange(1,11) ]

YEARS  = [(x,x) for x in xrange(timezone.now().year, 1899, -1)]


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
        ordering = ['order']
        abstract = True


class WineType(models.Model):

    class Meta:
        abstract = True

    WINE_TYPES = (
        ('w', _('White')),
        ('r', _('Red')),
        ('n', _('None'))
    )
    wineType = models.CharField(max_length=60, choices=WINE_TYPES, verbose_name=_('Wine Type'), blank=False, default='n')
    
    def __unicode__(self):
        return self.wineType


class Approvable(models.Model):
    APPROVED = 'a'
    REJECTED = 'r'
    PENDING = 'p'

    class Meta:
        abstract = True

    # Managers
    objects = models.Manager()
    approved = ApprovedManager() 
    
    STATUSES = (
        (APPROVED, _('Approved')),
        (REJECTED, _('Rejected')),
        (PENDING, _('Pending')),
    )
    status = models.CharField(max_length=60, choices=STATUSES, default=PENDING)

    def is_approved(self):
        return self.status == self.APPROVED

    is_approved.admin_order_field = 'status'
    is_approved.boolean = True
    is_approved.short_description = _('Approved ?')


# ==================================================
#  PRIVATE MODEL CLASSES (EXPOSED TO ADMIN ONLY)
# ==================================================

# -------------------------------------------------------------
class Acidity(Orderable, Timestamp):
    '''
    Can subclass WineType,Orderable,Timestamp Meta classes if needed
    '''
    class Meta(Orderable.Meta):
        verbose_name_plural = _('Acidities')
    acidity = models.CharField(max_length=60,
                               unique=True,
                               verbose_name=_('Acidity')
                               )

    def __unicode__(self):
        return self.acidity


# -------------------------------------------------------------
class Aroma(Orderable, Timestamp):
    '''
    Aromas related to :model:`corewine.Wine`
    
    Can subclass WineType,Orderable,Timestamp Meta classes if needed
    '''
    class Meta(Orderable.Meta):
        verbose_name_plural = _('Aromas')

    aroma = models.CharField(max_length=60,
                             unique=True,
                             verbose_name=_('Aroma')
                             )


    def __unicode__(self):
        return self.aroma


# -------------------------------------------------------------
class Tanin(Orderable, Timestamp):
    '''
    Can subclass WineType,Orderable,Timestamp Meta classes if needed
    '''

    tanin = models.CharField(max_length=60,
                             unique=True,
                             verbose_name=_('Tanin')
                             )

    def __unicode__(self):
        return self.tanin


# -------------------------------------------------------------
class Teint(WineType, Orderable, Timestamp):
    '''
    Can subclass WineType,Orderable,Timestamp Meta classes if needed
    '''
    teint = models.CharField(max_length=60,
                             unique=True,
                             verbose_name=_('Teint')
                             )
    def __unicode__(self):
        return self.teint


# -------------------------------------------------------------
class Taste(Orderable, Timestamp):

    class Meta(Orderable.Meta):
        verbose_name_plural = _('Tastes')

    taste = models.CharField(max_length=60,
                             unique=True,
                             verbose_name=_('Taste')
                             )


    def __unicode__(self):
        return self.taste


# ==================================================
#  PUBLIC MODEL CLASSES (EXPOSED TO FORMS)
# ==================================================

# -------------------------------------------------------------
class Appelation(Approvable, Timestamp):
    class Meta:
        verbose_name_plural = _('Appelations')
        ordering = ['appelation']
    appelation = models.CharField(max_length=100,
                                  verbose_name=_('Appelation'),
                                  validators=[non_numeric],
                                  blank=True,
                                  unique=True
                                 )
    def __unicode__(self):
        return self.appelation

    def save(self, *args, **kwargs):
        val = getattr(self,'appelation', False)
        if val:
            setattr(self,'appelation', val.title())

        super(Appelation,self).save(*args, **kwargs)

# -------------------------------------------------------------
class Cepage(Approvable, WineType, Timestamp):

    class Meta:
        ordering = ['cepage']
    cepage = models.CharField(max_length=60,
                              validators=[non_numeric],
                              verbose_name=_('Cepage'),
                              unique=True
                              )
    
    def save(self, *args, **kwargs):
        val = getattr(self,'cepage', False)
        if val:
            setattr(self,'cepage', val.title())

        super(Cepage,self).save(*args, **kwargs)

    def __unicode__(self):
        return self.cepage


# -------------------------------------------------------------
class Country(Approvable, Timestamp):

    class Meta:
        verbose_name_plural = _('Countries')
        ordering = ['country']

    country = models.CharField(max_length=250,
                               unique=True,
                               verbose_name=_('Country')
                               )
    
    
    def __unicode__(self):
        return self.country


# -------------------------------------------------------------
class Region(Approvable, Timestamp):
    class Meta:
        verbose_name_plural = _('Regions')
        ordering = ['region']
    region = models.CharField(max_length=100,
                              verbose_name=_('Region'),
                              validators=[non_numeric],
                              unique=True
                             )
    def __unicode__(self):
        return self.region


    def save(self, *args, **kwargs):
        val = getattr(self,'region', False)
        if val:
            setattr(self,'region', val.title())

        super(Region,self).save(*args, **kwargs)


# -------------------------------------------------------------
class Producer(Approvable, Timestamp):
    class Meta:
        verbose_name_plural = _('Productors')
        ordering = ['producer']
    producer = models.CharField(max_length=100,
                                verbose_name=_('Producer'),
                                validators=[non_numeric],
                                unique=True
                                )

    def __unicode__(self):
        return self.producer


    def save(self, *args, **kwargs):
        val = getattr(self,'producer', False)
        if val:
            setattr(self,'producer', val.title())

        super(Producer,self).save(*args, **kwargs)


# -------------------------------------------------------------
class Tag(Approvable, WineType, Timestamp):

    class Meta:
        ordering = ['tag']
    tag = models.CharField(max_length=60,
                           validators=[non_numeric],
                           unique=True
                           )
    description = models.CharField(max_length=300)

    def __unicode__(self):
        return self.tag

    def save(self, *args, **kwargs):
        val = getattr(self,'tag', False)
        if val:
            setattr(self,'tag', val.title())

        super(Tag,self).save(*args, **kwargs)


# -------------------------------------------------------------
class Wine(WineType, Timestamp):
    """
    Docstring for class Wine.
    py:class:: Wine
    """
    # ------------------------------------
    # Fields


    class Meta:
        ordering = ['name']
        verbose_name_plural = _('Wines')

    slug = models.SlugField()

    name = models.CharField(max_length=100,
                            unique=True,
                            verbose_name=_('Name'),
                            validators=[non_numeric]
                            )
    
    year = models.IntegerField(choices=YEARS, verbose_name=_('Year') )
    
    alcool = models.FloatField(verbose_name=_('Alcool'),
                               validators=[percentage]
                              )
    
    date = models.DateField(_('Tasting Date'), help_text='Format : yyyy-mm-dd', validators=[validate_future_date])

    code_saq = models.CharField(unique=True,
                                max_length=255,
                                verbose_name=_('SAQ Code'),
                                validators=[numeric_only]
                                )
    
    price = models.FloatField(verbose_name=_('Price'),
                              validators=[price,price_too_high])

    mouth_intensity = models.DecimalField(choices=SCALE, max_digits=2, decimal_places=1, verbose_name=_('Mouth Intensity'))
    nose_intensity = models.DecimalField(choices=SCALE, max_digits=2, decimal_places=1, verbose_name=_('Nose Intensity'))
    persistance = models.DecimalField(choices=SCALE, max_digits=2, decimal_places=1, verbose_name=_('Persistance'))
    rating = models.DecimalField(choices=SCALE, max_digits=2, decimal_places=1, verbose_name=_('Rating'))

    # ------------------------------------
    # Foreign Keys
    producer = models.ForeignKey(Producer, verbose_name=_('Producer'))

    appelation = models.ForeignKey(Appelation, null=True, blank=True, verbose_name=_('Appelation'))
    
    country = models.ForeignKey(Country, verbose_name=_('Country'))
    
    region = models.ForeignKey(Region, verbose_name=_('Region'))
    
    teint = models.ForeignKey(Teint, verbose_name=_('Teint'))
    
    aroma = models.ForeignKey(Aroma, verbose_name=_('Aroma'))
    
    taste = models.ForeignKey(Taste, verbose_name=_('Taste'))
    
    acidity = models.ForeignKey(Acidity, verbose_name=_('Acidity'))
    
    tanin = models.ForeignKey(Tanin, verbose_name=_('Tanin'), blank=True)

    # ------------------------------------
    # Many To Many
    cepage = models.ManyToManyField(Cepage, verbose_name=_('Cepages'))
    
    tag = models.ManyToManyField(Tag, blank=True, null=True, verbose_name=_('Tags'))

    # tag_test = TaggableManager(verbose_name='Tags Test')
    # cepage_test = TaggableManager(verbose_name='Cepages Test')

    # ------------------------------------
    # Managers
    # objects = WineManager()


    # ------------------------------------
    # Model Methods
    # ------------------------------------
    
    def __unicode__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('corewine:detail', kwargs={"slug": self.slug})

    # ------------------------------------
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.name = self.name.title()
        super(Wine, self).save(*args, **kwargs)

    # ------------------------------------
    def list_cepage(obj):
        list_cepage = ', '.join([x.__unicode__() for x in obj.cepage.all() if x.is_approved()])
        return list_cepage

    list_cepage.admin_order_field = 'name'
    list_cepage.boolean = False
    list_cepage.short_description = _('Cepages')

    # ------------------------------------
    def list_tag(obj):
        list_tag = ', '.join([x.__unicode__() for x in obj.tag.all() if x.is_approved()])
        return list_tag

    list_tag.admin_order_field = 'name'
    list_tag.boolean = False
    list_tag.short_description = _('Tags')

    # ------------------------------------
    def arr_cepage(obj):
        return [x.__unicode__() for x in obj.cepage.all() if x.is_approved()]
    
    # ------------------------------------
    def arr_tag(obj):
        return [x.__unicode__() for x in obj.tag.all() if x.is_approved()]




