from django import forms
from .models import Tarea
from datetime import date


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'completo', 'fecha_vencimiento', 'prioridad']

        widgets = {
            'fecha_vencimiento': forms.DateInput(
                attrs={
                    'type': 'date',
                    # Añade el atributo 'min' con la fecha de hoy
                    'min': date.today().strftime('%Y-%m-%d')
                }
            ),
        }

    def clean_fecha_vencimiento(self):
        fecha = self.cleaned_data.get('fecha_vencimiento')
        if fecha is None:
            return fecha
        if fecha < date.today():
            raise forms.ValidationError("¡No puedes seleccionar una fecha anterior a la de hoy!")
        return fecha
