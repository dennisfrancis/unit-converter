from django.shortcuts import render
from django.views import View


class LengthView(View):
    template_name = "convert/length.html"
    convert_type = "length"
    units = ['millimeter', 'centimeter', 'meter',
             'kilometer', 'inch', 'foot', 'yard', 'mile']

    def get(self, request):
        ctx = {"units": self.units,
               "convert_type": self.convert_type,
               }
        return render(request,
                      self.template_name,
                      ctx)

    def post(self, request):
        return render(request, self.template_name)


class WeightView(View):
    template_name = "convert/weight.html"
    convert_type = "weight"
    units = ['milligram', 'gram', 'kilogram', 'ounce', 'pound']

    def get(self, request):
        ctx = {"units": self.units,
               "convert_type": self.convert_type,
               }
        return render(request,
                      self.template_name,
                      ctx)

    def post(self, request):
        return render(request, self.template_name)


class TemperatureView(View):
    template_name = "convert/temperature.html"
    convert_type = "temperature"
    units = ['celsius', 'fahrenheit', 'kelvin']

    def get(self, request):
        ctx = {"units": self.units,
               "convert_type": self.convert_type,
               }
        return render(request,
                      self.template_name,
                      ctx)

    def post(self, request):
        return render(request, self.template_name)


class ResultView(View):
    template_name = "convert/result.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)
