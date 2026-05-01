from youtube_reports.models import VideoMetric
from youtube_reports.reports.clickbait import ClickbaitReport


def test_clickbait_report_filters_and_sorts_rows_by_ctr_desc() -> None:
    metrics = [
        VideoMetric("Low CTR", 10.0, 20.0),
        VideoMetric("High retention", 20.0, 50.0),
        VideoMetric("Second", 18.0, 35.0),
        VideoMetric("First", 25.0, 22.0),
    ]

    rows = ClickbaitReport().generate(metrics)

    assert [row.title for row in rows] == ["First", "Second"]
    assert [row.ctr for row in rows] == [25.0, 18.0]


def test_clickbait_report_uses_strict_thresholds() -> None:
    metrics = [
        VideoMetric("CTR equals threshold", 15.0, 20.0),
        VideoMetric("Retention equals threshold", 16.0, 40.0),
    ]

    rows = ClickbaitReport().generate(metrics)

    assert rows == []
