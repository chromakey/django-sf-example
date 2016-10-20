from salesforce import models


class Lead(models.SalesforceModel):
    name = models.CharField(max_length=121, verbose_name='Full Name', sf_read_only=models.READ_ONLY)
    last_name = models.CharField(max_length=80)
    first_name = models.CharField(max_length=40, blank=True)
    company = models.CharField(max_length=255)
    phone = models.CharField(max_length=40, blank=True)
    mobile_phone = models.CharField(max_length=40, blank=True)
    other_phone = models.CharField(custom=True, db_column='Other_Phone__c', max_length=40, verbose_name='Other Phone',
                                   blank=True)
    email = models.EmailField(blank=True, null=True)
    alternate_email = models.EmailField(custom=True, db_column='Alternate_email__c', verbose_name='Alternate email',
                                        blank=True, null=True)
    country = models.CharField(max_length=80, blank=True)
    street = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=40, blank=True)
    state = models.CharField(max_length=80, verbose_name='State/Province', blank=True)
    postal_code = models.CharField(max_length=20, verbose_name='Zip/Postal Code', blank=True)
    created_date = models.DateTimeField(sf_read_only=models.READ_ONLY)


    class Meta(models.Model.Meta):
        db_table = 'Lead'
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
        # keyPrefix = '00Q'
