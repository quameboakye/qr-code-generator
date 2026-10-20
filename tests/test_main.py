import main


def test_valid_url_accepted():
    assert main.is_valid_url("https://github.com/quameboakye")


def test_invalid_url_rejected():
    assert not main.is_valid_url("not a url")


def test_qr_code_file_created(tmp_path):
    out = tmp_path / "qr.png"
    main.generate_qr_code("https://example.com", out)
    assert out.exists() and out.stat().st_size > 0


def test_invalid_url_creates_no_file(tmp_path):
    out = tmp_path / "qr.png"
    main.generate_qr_code("not a url", out)
    assert not out.exists()