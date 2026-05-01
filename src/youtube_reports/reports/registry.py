from youtube_reports.reports.base import Report
from youtube_reports.reports.clickbait import ClickbaitReport


class UnknownReportError(ValueError):
    pass


REPORTS: dict[str, Report] = {
    ClickbaitReport.name: ClickbaitReport(),
}


def get_report(report_name: str) -> Report:
    try:
        return REPORTS[report_name]
    except KeyError as error:
        available_reports = ", ".join(sorted(REPORTS))
        message = (
            f"unknown report '{report_name}'. "
            f"Available reports: {available_reports}"
        )
        raise UnknownReportError(message) from error
