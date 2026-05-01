from dataclasses import dataclass


@dataclass(frozen=True)
class VideoMetric:
    title: str
    ctr: float
    retention_rate: float


@dataclass(frozen=True)
class ReportRow:
    title: str
    ctr: float
    retention_rate: float
