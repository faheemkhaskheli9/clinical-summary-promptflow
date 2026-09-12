from pydantic import BaseModel, TypeAdapter, ValidationError
import pytest

from clinical_summary import SymptomSchema, SymptomSeverity


def test_valid_symptom_is_preserved():
    symptom = SymptomSchema(
        description="dull headache behind the eyes",
        onset="3 days ago",
        severity=SymptomSeverity.MODERATE,
        duration="intermittent, a few hours at a time",
    )

    assert symptom.description == "dull headache behind the eyes"
    assert symptom.severity is SymptomSeverity.MODERATE


def test_only_description_is_required():
    symptom = SymptomSchema(description="mild cough")

    assert symptom.onset is None
    assert symptom.severity is None
    assert symptom.duration is None


def test_empty_description_is_rejected():
    with pytest.raises(ValidationError):
        SymptomSchema(description="")


def test_severity_rejects_free_text_outside_the_enum():
    with pytest.raises(ValidationError):
        SymptomSchema.model_validate({"description": "chest pain", "severity": "excruciating"})


def test_severity_accepts_each_enum_value():
    for value in ("mild", "moderate", "severe"):
        symptom = SymptomSchema.model_validate({"description": "sore throat", "severity": value})
        assert symptom.severity == SymptomSeverity(value)


def test_unknown_explicit_field_is_rejected():
    with pytest.raises(ValidationError):
        SymptomSchema.model_validate({"description": "fatigue", "notes": "unrelated"})


def test_conversation_may_report_zero_symptoms():
    symptoms = TypeAdapter(list[SymptomSchema]).validate_python([])

    assert symptoms == []


def test_conversation_may_report_multiple_symptoms():
    payload = [
        {"description": "headache", "severity": "mild"},
        {"description": "nausea", "severity": "severe", "onset": "this morning"},
    ]

    symptoms = TypeAdapter(list[SymptomSchema]).validate_python(payload)

    assert len(symptoms) == 2
    assert symptoms[0].description == "headache"
    assert symptoms[1].severity is SymptomSeverity.SEVERE


def test_symptom_list_field_defaults_to_empty_on_a_container_model():
    class ConversationExtraction(BaseModel):
        symptoms: list[SymptomSchema] = []

    extraction = ConversationExtraction()

    assert extraction.symptoms == []
