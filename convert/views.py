from django.shortcuts import render
from django.views import View

from enum import Enum
from typing import List, Set


def get_str_units_list(enum_class) -> List[str]:
    return [unit.name.lower() for unit in enum_class]


def get_str_units_set(enum_class) -> Set[str]:
        return set(get_str_units_list(enum_class))


class LengthUnits(Enum):
    Millimeter = 1.0
    Centimeter = 10.0 * Millimeter
    Meter = 100.0 * Centimeter
    Kilometer = 1000.0 * Meter
    Inch = 25.4 * Millimeter
    Foot = 12 * Inch
    Yard = 3 * Foot
    Mile = 1760 * Yard

    @staticmethod
    def convert(src: "LengthUnits", dest: "LengthUnits", value: float) -> float:
        return (value / src.value) * dest.value


class LengthView(View):
    template_name = "convert/length.html"
    convert_type = "length"
    units = get_str_units_list(LengthUnits)
    unit_set = set(units)

    def get(self, request):
        ctx = {"units": self.units,
               "convert_type": self.convert_type,
               }
        return render(request,
                      self.template_name,
                      ctx)

    def post(self, request):
        return render(request, self.template_name)


class WeightUnits(Enum):
    Milligram = 1.0
    Gram = 1000.0 * Milligram
    Kilogram = 1000.0 * Gram
    Ounce = 28349.5 * Milligram
    Pound = 16.0 * Ounce

    @staticmethod
    def convert(src: "WeightUnits", dest: "WeightUnits", value: float) -> float:
        return (value / src.value) * dest.value


class WeightView(View):
    template_name = "convert/weight.html"
    convert_type = "weight"
    units = get_str_units_list(WeightUnits)
    unit_set = set(units)

    def get(self, request):
        ctx = {"units": self.units,
               "convert_type": self.convert_type,
               }
        return render(request,
                      self.template_name,
                      ctx)

    def post(self, request):
        return render(request, self.template_name)


class TemperatureUnits(Enum):
    Celsius = 1
    Fahrenheit = 2
    Kelvin = 3

    @staticmethod
    def convert(src: "TemperatureUnits", dest: "TemperatureUnits", value: float) -> float:
        if src == dest:
            return value
        tu = TemperatureUnits
        if src == tu.Celsius:
            if dest == tu.Fahrenheit:
                return (value * 9.0 / 5.0) + 32.0
            else:  # dest == tu.Kelvin
                return value + 273.15
        elif src == tu.Fahrenheit:
            if dest == tu.Celsius:
                return (value - 32) * 5.0 / 9.0
            else:  # dest == tu.Kelvin
                return ((value - 32) * 5.0 / 9.0) + 273.15
        else:
            if dest == tu.Celsius:
                return value - 273.15
            else:  # dest == tu.Fahrenheit
                return ((value - 273.15) * 9.0 / 5.0) + 32.0


class TemperatureView(View):
    template_name = "convert/temperature.html"
    convert_type = "temperature"
    units = get_str_units_list(TemperatureUnits)
    unit_set = set(units)

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
