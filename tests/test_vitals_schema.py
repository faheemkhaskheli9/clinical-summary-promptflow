import pytest
from pydantic import ValidationError

from clinical_summary import VitalsSchema


def test_valid_vitals_are_preserved():
    vitals = VitalsSchema(
        systolic_bp_mmhg=118,
        diastolic_bp_mmhg=76,
        heart_rate_bpm=72,
        temperature_c=36.8,
        respiratory_rate_bpm=16,
        spo2_percent=98,
        weight_kg=70.5,
        height_cm=172,
    )

    assert vitals.systolic_bp_mmhg == 118
    assert vitals.temperature_c == 36.8


def test_every_field_may_be_missing():
    vitals = VitalsSchema()

    assert all(value is None for value in vitals.model_dump().values())


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("systolic_bp_mmhg", 301),
        ("diastolic_bp_mmhg", 19),
        ("heart_rate_bpm", 301),
        ("temperature_c", 46),
        ("respiratory_rate_bpm", -1),
        ("spo2_percent", 101),
        ("weight_kg", -1),
        ("height_cm", 301),
    ],
)
def test_each_out_of_range_vital_is_rejected(field, value):
    with pytest.raises(ValidationError):
        VitalsSchema.model_validate({field: value})


def test_unknown_explicit_field_is_rejected():
    with pytest.raises(ValidationError):
        VitalsSchema.model_validate({"pulse": 72})
