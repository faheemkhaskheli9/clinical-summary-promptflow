from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class SymptomSeverity(str, Enum):
    """Bounded severity scale for a reported symptom.

    An enum (rather than free text or an unbounded int) keeps downstream
    aggregation and evaluation comparable across extractions.
    """

    MILD = "mild"
    MODERATE = "moderate"
    SEVERE = "severe"


class SymptomSchema(BaseModel):
    """A single patient-reported symptom extracted from a conversation.

    ``description`` keeps the original free-text mention for traceability;
    ``onset``, ``severity``, and ``duration`` are the structured fields a
    downstream summarization/evaluation node can rely on being consistent.
    """

    model_config = ConfigDict(extra="forbid")

    description: str = Field(min_length=1)
    onset: str | None = Field(default=None, description="When the symptom started, e.g. '3 days ago'.")
    severity: SymptomSeverity | None = Field(default=None)
    duration: str | None = Field(default=None, description="How long the symptom has lasted, e.g. '2 hours'.")


class VitalsSchema(BaseModel):
    """Validated vital signs extracted from a clinical conversation.

    Every field is optional because a conversation may omit any measurement.
    Units are fixed in field names so downstream nodes cannot confuse them.
    """

    model_config = ConfigDict(extra="forbid")

    systolic_bp_mmhg: int | None = Field(default=None, ge=40, le=300)
    diastolic_bp_mmhg: int | None = Field(default=None, ge=20, le=200)
    heart_rate_bpm: int | None = Field(default=None, ge=0, le=300)
    temperature_c: float | None = Field(default=None, ge=25, le=45)
    respiratory_rate_bpm: int | None = Field(default=None, ge=0, le=100)
    spo2_percent: float | None = Field(default=None, ge=0, le=100)
    weight_kg: float | None = Field(default=None, ge=0, le=500)
    height_cm: float | None = Field(default=None, ge=0, le=300)
