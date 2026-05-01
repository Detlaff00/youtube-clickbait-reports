from youtube_reports.renderer import render_table


def test_render_table_keeps_headers_for_empty_report() -> None:
    output = render_table([])

    assert "title" in output
    assert "ctr" in output
    assert "retention_rate" in output
