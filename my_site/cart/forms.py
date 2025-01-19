from django import forms

PRODUCT_QUANTITY_CHOISES = [(i, str(i)) for i in range(1, 11)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices = PRODUCT_QUANTITY_CHOISES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    size = forms.CharField(max_length=10, required=False, widget=forms.HiddenInput)
    # def __init__(self, *args, **kwargs):
    #     max_quantity = kwargs.pop('max_quantity', 10)
    #     super().__init__(*args, **kwargs)
    #     self.fields['quantity'].choices = [(i, str(i)) for i in range(1, max_quantity + 1)]