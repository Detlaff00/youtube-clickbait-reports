import csv
from pathlib import Path
from typing import Iterable

from youtube_reports.models import VideoMetric


def read_video_metrics(file_paths: Iterable[Path]) -> list[VideoMetric]:
    metrics: list[VideoMetric] = []

    for file_path in file_paths:
        with file_path.open(encoding="utf-8", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                metrics.append(
                    VideoMetric(
                        title=row["title"],
                        ctr=float(row["ctr"]),
                        retention_rate=float(row["retention_rate"]),
                    )
                )

    return metrics
