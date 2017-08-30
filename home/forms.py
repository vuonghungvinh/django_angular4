from django import forms
from .models import AdName,AdImage,AdFeatures,AdFeaturesPricing,AdPricing
# from django.forms.models import inlineformset_factory
from django_countries.widgets import CountrySelectWidget
from django.utils.translation import ugettext_lazy as _

class AdNameForm(forms.ModelForm):

	ad_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Enter Ad Title')}),required=True, label = 'Ad Title')
	ad_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Enter Ad Description'),'rows':2}),required=True, label = _('Ad Description'))
	ad_type = forms.ChoiceField(widget=forms.RadioSelect, choices=(('0', _('Products'),), ('1', _('Services'),)), required=False, label = _('Ad Type'), initial=0)

	
	class Meta:
		model = AdName
		fields = ('ad_title','ad_description','ad_type')


class AdImageForm(forms.ModelForm):

	#image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,'id': 'filer_input2',}))
	image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	
	
	class Meta:
		model = AdImage
		fields = ('image',)


class AdFeaturesForm(forms.ModelForm):

	condition_of_item = forms.ChoiceField(choices=[('','Condition of Items')] + [('Brand New Still in Packing', 'Brand New Still in Packing',), 
		('New without original packing', 'New without original packing',), ('Sparingly used', 'Sparingly used',), ('Used', 'Used',), ('Canadians', 'Canadians',), 
		('In good condition', 'In good condition',), ('Used with a few notable damage','Used with a few notable damage'),('Needs Repair','Needs Repair')],
		widget=forms.Select(attrs={'class': 'form-control'}),required=False)

	period_used = forms.ChoiceField(choices=[('','Period Used')] + [('Not Used', 'Not Used',), 
		('Few Days', 'Few Days',), ('1 Month', '1 Month',), ('2-6 months', '2-6 months',),
		('6-12 months','6-12 months'),('above 12 months','above 12 months'),
		('1 to 2 years used','1 to 2 years used'),('used above 2 years','used above 2 years')],
		widget=forms.Select(attrs={'class': 'form-control'}),required=False)

	warranty = forms.ChoiceField(choices=[('','Warranty')] + [('Full Warranty Available', 'Full Warranty Available',), ('No Warranty', 'No Warranty',), ('Does not Apply', 'Does not Apply',)],
		widget=forms.Select(attrs={'class': 'form-control'}),required=False)

	address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Location of Item')}),required=False)
	
	
	class Meta:
		model = AdFeatures
		fields = ('condition_of_item','period_used','warranty','position','address')



#testFormset = inlineformset_factory(AdFeatures, AdFeaturesPricing, form=AdFeaturesForm ,extra=3)


class AdFeaturesPricingForm(forms.ModelForm):

	
	price = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'USD', 'required':'required'}),required=True)
	currency = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required':'required'}),required=True)
	negotiable = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),required=False)
	delivery_included = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),required=False)
	delivery_comments = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),required=False)
	
	class Meta:
		model = AdFeaturesPricing
		fields = ('country','price','currency','negotiable','delivery_included','delivery_comments')
		widgets = {'country': forms.Select(attrs={'class': 'form-control','onchange': 'GetCurrency(this.value,0);', 'required':'required'})}
		
# testFormset = inlineformset_factory(AdFeatures,AdFeaturesPricing,form=AdFeaturesPricingForm,extra=3)

class AdPricingForm(forms.ModelForm):

	#ad_option = forms.ChoiceField(widget=forms.RadioSelect, choices=(('1', _('Featured Ad (2$)'),), ('2', _('Push to Top (2$)'),),('3',_('Premium Ad (3$)'))), required=False, label = _('Ad Option'))
	#ad_featured = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),required=False)
	#ad_push_to_top = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),required=False)
	#ad_premium = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),required=False)
	ad_featured = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),required=False, label = _('Featured Ad (2$)'))
	ad_push_to_top = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),required=False, label = _('Push to Top (2$)'))
	ad_premium = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}),required=False, label = _('Premium Ad (3$)'))

	class Meta:
		model = AdPricing
		fields = ('ad_featured','ad_push_to_top','ad_premium')

	
	


		
		
        
	     
