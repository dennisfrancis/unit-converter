from django.shortcuts import render
from django.views import View


class LengthView(View):
    template_name = "convert/convert.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class WeightView(View):
    template_name = "convert/convert.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class TemperatureView(View):
    template_name = "convert/convert.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)
