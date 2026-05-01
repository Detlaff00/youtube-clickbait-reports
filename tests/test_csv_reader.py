from pathlib import Path

import pytest

from youtube_reports.csv_reader import read_video_metrics


def write_csv(path: Path, rows: list[str]) -> None:
    path.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        + "\n".join(rows)
        + "\n",
        encoding="utf-8",
    )


def test_read_video_metrics_combines_multiple_files(tmp_path: Path) -> None:
    first_file = tmp_path / "stats1.csv"
    second_file = tmp_path / "stats2.csv"
    write_csv(first_file, ["First,18.2,35,45200,1240,4.2"])
    write_csv(second_file, ["Second,21.0,30,67300,1890,4.0"])

    metrics = read_video_metrics([first_file, second_file])

    assert [metric.title for metric in metrics] == ["First", "Second"]
    assert metrics[0].ctr == 18.2
    assert metrics[1].retention_rate == 30.0


def test_read_video_metrics_raises_for_missing_file(tmp_path: Path) -> None:
    missing_file = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        read_video_metrics([missing_file])
