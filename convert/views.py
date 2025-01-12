from django.shortcuts import render
from django.views import View

from enum import Enum
from typing import List, Dict, Optional


def get_str_units_list(enum_class) -> List[str]:
    return [unit.name.lower() for unit in enum_class]


def get_str_units_map(enum_class) -> Dict[str, Enum]:
    return {unit.name.lower(): unit for unit in enum_class}


def get_result(enum_map, get_params, converter, ctx) -> Optional[float]:
    got_units = True
    from_unit = None
    to_unit = None
    units_in_dict = ("from_unit" in get_params and "to_unit" in get_params)
    try:
        from_unit, to_unit = \
            enum_map[get_params["from_unit"]], \
            enum_map[get_params["to_unit"]]
    except Exception:
        if units_in_dict:
            ctx["error_msg"] = "Invalid units!"
        got_units = False

    got_value = True
    value_in_dict = False
    if "input_value" in get_params:
        value_in_dict = True
    input_value = 0.0
    try:
        input_value = float(get_params["input_value"])
    except Exception:
        if value_in_dict:
            ctx["error_msg"] = "Invalid input value"
        got_value = False

    if got_units and from_unit is not None and to_unit is not None:
        ctx["from_unit"], ctx["to_unit"] = from_unit.name.lower(), \
                to_unit.name.lower()
    if got_value:
        ctx["input_value"] = str(input_value)

    return converter(from_unit, to_unit, input_value) \
        if got_value and got_units else None


class LengthUnits(Enum):
    Millimeter = 1.0
    Centimeter = Millimeter / 10.0
    Meter = Centimeter / 100.0
    Kilometer = Meter / 1000.0
    Inch = Millimeter / 25.4
    Foot = Inch / 12.0
    Yard = Foot / 3.0
    Mile = Yard / 1760.0

    @staticmethod
    def convert(src: "LengthUnits", dest: "LengthUnits",
                value: float) -> float:
        return (value / src.value) * dest.value


class LengthView(View):
    template_name = "convert/length.html"
    convert_type = "length"
    units = get_str_units_list(LengthUnits)
    units_map = get_str_units_map(LengthUnits)

    def get(self, request):
        ctx = {"units": self.units,
               "convert_type": self.convert_type,
               }

        result = get_result(self.units_map,
                            request.GET,
                            LengthUnits.convert, ctx)
        if result is not None:
            ctx["result"] = str(result)

        return render(request,
                      self.template_name,
                      ctx)


class WeightUnits(Enum):
    Milligram = 1.0
    Gram = Milligram / 1000.0
    Kilogram = Gram / 1000.0
    Ounce = Milligram / 28349.5
    Pound = Ounce / 16.0

    @staticmethod
    def convert(src: "WeightUnits", dest: "WeightUnits",
                value: float) -> float:
        return (value / src.value) * dest.value


class WeightView(View):
    template_name = "convert/weight.html"
    convert_type = "weight"
    units = get_str_units_list(WeightUnits)
    units_map = get_str_units_map(WeightUnits)

    def get(self, request):
        ctx = {"units": self.units,
               "convert_type": self.convert_type,
               }
        result = get_result(self.units_map,
                            request.GET,
                            WeightUnits.convert, ctx)
        if result is not None:
            ctx["result"] = str(result)
        return render(request,
                      self.template_name,
                      ctx)


class TemperatureUnits(Enum):
    Celsius = 1
    Fahrenheit = 2
    Kelvin = 3

    @staticmethod
    def convert(src: "TemperatureUnits", dest: "TemperatureUnits",
                value: float) -> float:
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
    units_map = get_str_units_map(TemperatureUnits)
    unit_set = set(units)

    def get(self, request):
        ctx = {"units": self.units,
               "convert_type": self.convert_type,
               }
        result = get_result(self.units_map,
                            request.GET,
                            TemperatureUnits.convert, ctx)
        if result is not None:
            ctx["result"] = str(result)
        return render(request,
                      self.template_name,
                      ctx)
