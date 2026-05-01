import argparse
from pathlib import Path
from typing import Sequence

from youtube_reports.csv_reader import read_video_metrics
from youtube_reports.renderer import render_table
from youtube_reports.reports import UnknownReportError, get_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="youtube-reports",
        description="Build reports from YouTube video metric CSV files.",
    )
    parser.add_argument(
        "--files",
        nargs="+",
        type=Path,
        required=True,
        help="Path to one or more CSV files with video metrics.",
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Report name. Currently supported: clickbait.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        report = get_report(args.report)
        metrics = read_video_metrics(args.files)
    except UnknownReportError as error:
        parser.exit(2, f"error: {error}\n")
    except FileNotFoundError as error:
        parser.exit(1, f"error: file not found: {error.filename}\n")

    print(render_table(report.generate(metrics)))
    return 0
