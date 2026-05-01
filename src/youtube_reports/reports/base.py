from typing import Protocol, Sequence

from youtube_reports.models import ReportRow, VideoMetric


class Report(Protocol):
    name: str

    def generate(self, metrics: Sequence[VideoMetric]) -> list[ReportRow]:
        """Build report rows from video metrics."""
