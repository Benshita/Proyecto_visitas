from django import forms
from .models import Visita

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['nombre_visitante', 'rut', 'motivo', 'empresa_procedencia']
        widgets = {
            'rut': forms.TextInput(attrs={'placeholder': '12.345.678-9'}),
            'motivo': forms.Textarea(attrs={'rows': 3}),
        }

    # Validación básica de RUT (Opcional: puedes agregar algoritmos de módulo 11 aquí)
    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not "-" in rut:
            raise forms.ValidationError("El RUT debe contener un guión.")
        return rut