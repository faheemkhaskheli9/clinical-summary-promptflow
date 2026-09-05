from pydantic import BaseModel, ConfigDict, Field


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
