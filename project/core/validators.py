from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

non_numeric = RegexValidator(regex='^[a-zA-Z\s-]*$',
                                      message=_('Expression should not contain numeric values'),
                                      code='no_numeric_expected'
                                      )

numeric_only = RegexValidator(regex='^[0-9\s-]*$',
                                      message=_('Expression contains letters'),
                                      code='numeric_only_expected'
                                      )

float_string = RegexValidator(regex='^\d+\.?\d+$',
                                      message=_('This is not a valid number'),
                                      code='not_float_formatted'
                                      )
price = RegexValidator(regex='^\d+\.?\d{1,2}$',
                                      message=_('Not a valid price. 2 decimals maximum and numbers only is allowed.'),
                                      code='not_float_formatted'
                                      )
price_too_high = RegexValidator(regex='^\d{1,5}\.?\d{1,2}$',
                                      message=_('This price seems too high. Please make sure it is correct.'),
                                      code='not_float_formatted'
                                      )

percentage = RegexValidator(regex='^\d{1,2}\.?\d{1,2}$',
                                      message=_('This is not a valid percentage. Maximum is 100% and only put 1 decimal maximum.'),
                                      code='not_float_formatted'
                                      )

