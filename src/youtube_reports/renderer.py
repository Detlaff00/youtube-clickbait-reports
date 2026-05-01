from tabulate import tabulate

from youtube_reports.models import ReportRow

HEADERS = ["title", "ctr", "retention_rate"]


def render_table(rows: list[ReportRow]) -> str:
    table_rows = [
        [row.title, row.ctr, row.retention_rate]
        for row in rows
    ]

    return tabulate(
        table_rows,
        headers=HEADERS,
        tablefmt="github",
        floatfmt=".1f",
    )
