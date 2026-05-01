import pytest

from youtube_reports.reports import UnknownReportError, get_report
from youtube_reports.reports.clickbait import ClickbaitReport


def test_get_report_returns_clickbait_report() -> None:
    assert isinstance(get_report("clickbait"), ClickbaitReport)


def test_get_report_raises_for_unknown_report() -> None:
    with pytest.raises(UnknownReportError, match="unknown report"):
        get_report("unknown")
