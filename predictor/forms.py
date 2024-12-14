from django import forms 
class BreastCancerForm(forms.Form): 
	radius = forms.FloatField( 
		label='Mean Radius', 
		min_value=0, 
		widget=forms.NumberInput(attrs={'class': 'form-control'}), 
	) 
	texture = forms.FloatField( 
		label='Mean Texture', 
		min_value=0, 
		widget=forms.NumberInput(attrs={'class': 'form-control'}), 
	) 
	perimeter = forms.FloatField( 
		label='Mean Perimeter', 
		min_value=0, 
		widget=forms.NumberInput(attrs={'class': 'form-control'}), 
	) 
	area = forms.FloatField( 
		label='Mean Area', 
		min_value=0, 
		widget=forms.NumberInput(attrs={'class': 'form-control'}), 
	) 
	smoothness = forms.FloatField( 
		label='Mean Smoothness', 
		min_value=0, 
		widget=forms.NumberInput(attrs={'class': 'form-control'}), 
	) 
class SignInForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

from django import forms

class PredictionForm(forms.Form):
    mean_radius = forms.FloatField(label='Mean Radius')
    mean_texture = forms.FloatField(label='Mean Texture')
    mean_perimeter = forms.FloatField(label='Mean Perimeter')
    mean_area = forms.FloatField(label='Mean Area')
    mean_smoothness = forms.FloatField(label='Mean Smoothness')
    mean_compactness = forms.FloatField(label='Mean Compactness')
    mean_concavity = forms.FloatField(label='Mean Concavity')
    mean_concave_points = forms.FloatField(label='Mean Concave Points')
    mean_symmetry = forms.FloatField(label='Mean Symmetry')
    mean_fractal_dimension = forms.FloatField(label='Mean Fractal Dimension')
