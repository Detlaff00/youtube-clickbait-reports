import os
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def write_csv(path: Path, rows: list[str]) -> None:
    path.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        + "\n".join(rows)
        + "\n",
        encoding="utf-8",
    )


def run_cli(args: list[str]) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(PROJECT_ROOT / "src")
    return subprocess.run(
        [sys.executable, "-m", "youtube_reports", *args],
        capture_output=True,
        check=False,
        cwd=PROJECT_ROOT,
        env=env,
        text=True,
    )


def test_cli_outputs_clickbait_report_from_multiple_files(tmp_path: Path) -> None:
    first_file = tmp_path / "stats1.csv"
    second_file = tmp_path / "stats2.csv"
    write_csv(
        first_file,
        [
            "Second,18.2,35,45200,1240,4.2",
            "Ignored,9.5,82,31500,890,8.9",
        ],
    )
    write_csv(second_file, ["First,25.0,22,254000,8900,2.5"])

    result = run_cli(
        [
            "--files",
            str(first_file),
            str(second_file),
            "--report",
            "clickbait",
        ]
    )

    assert result.returncode == 0
    assert "First" in result.stdout
    assert "Second" in result.stdout
    assert "Ignored" not in result.stdout
    assert result.stdout.index("First") < result.stdout.index("Second")


def test_cli_returns_error_for_unknown_report(tmp_path: Path) -> None:
    stats_file = tmp_path / "stats.csv"
    write_csv(stats_file, ["Video,18.2,35,45200,1240,4.2"])

    result = run_cli(
        ["--files", str(stats_file), "--report", "unknown"]
    )

    assert result.returncode == 2
    assert "unknown report" in result.stderr


def test_cli_returns_error_for_missing_file(tmp_path: Path) -> None:
    missing_file = tmp_path / "missing.csv"

    result = run_cli(
        ["--files", str(missing_file), "--report", "clickbait"]
    )

    assert result.returncode == 1
    assert "file not found" in result.stderr
