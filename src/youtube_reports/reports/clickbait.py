from typing import Sequence

from youtube_reports.models import ReportRow, VideoMetric


class ClickbaitReport:
    name = "clickbait"
    min_ctr = 15
    max_retention_rate = 40

    def generate(self, metrics: Sequence[VideoMetric]) -> list[ReportRow]:
        rows = [
            ReportRow(
                title=metric.title,
                ctr=metric.ctr,
                retention_rate=metric.retention_rate,
            )
            for metric in metrics
            if metric.ctr > self.min_ctr
            and metric.retention_rate < self.max_retention_rate
        ]

        return sorted(rows, key=lambda row: row.ctr, reverse=True)
