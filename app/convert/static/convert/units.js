
function set_different_option(target, other) {
    const unit = target.value;
    const other_unit = other.value;
    if (unit != other_unit) {
        return;
    }

    const n = target.options.length;
    for (let idx = 0; idx < n; ++idx) {
        const this_unit = target.options[idx].value;
        if (unit != this_unit) {
            target.value = this_unit;
            return;
        }
    }
}


const from_unit = document.getElementById('from_unit');
const to_unit = document.getElementById('to_unit');
const unit_form = document.getElementById('unit_form');

function swap_units() {
    const u1 = from_unit.value;
    const u2 = to_unit.value;
    from_unit.value = u2;
    to_unit.value = u1;
}

if (from_unit && to_unit && unit_form) {
    set_different_option(to_unit, from_unit);
    from_unit.addEventListener('change', function (e) {
        set_different_option(to_unit, from_unit);
    });
    to_unit.addEventListener('change', function (e) {
        set_different_option(from_unit, to_unit);
    });

    unit_form.addEventListener('reset', function (e) {
        setTimeout(function() {
            set_different_option(to_unit, from_unit);
        });
    });
}
