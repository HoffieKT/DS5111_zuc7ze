import sys
import io
import pytest
from clean_ids import main

def test_script_execution(monkeypatch, capsys):
    fake_input = io.StringIO("kcFsuxaJ1es\nasd123\n")
    monkeypatch.setattr(sys, "stdin", fake_input)

    main()

    captured = capsys.readouterr()

    assert captured.out == "kcFsuxaJ1es\n"

def test_bad_lines(monkeypatch, capsys):
    fake_input = io.StringIO("aaa\n123\naaa123\n")
    monkeypatch.setattr(sys, "stdin", fake_input)

    main()

    captured = capsys.readouterr()

    assert captured.out == ""

def test_good_lines(monkeypatch, capsys):
    fake_input = io.StringIO("h3llt4ria9e\nngeeg01ba9w\n")
    monkeypatch.setattr(sys, "stdin", fake_input)

    main()

    captured = capsys.readouterr()

    assert captured.out == "h3llt4ria9e\nngeeg01ba9w\n"

def test_empty_line(monkeypatch, capsys):
    fake_input = io.StringIO("")
    monkeypatch.setattr(sys, "stdin", fake_input)

    main()

    captured = capsys.readouterr()

    assert captured.out == ""

def test_too_long(monkeypatch, capsys):
    fake_input = io.StringIO("123456789abcdefghijklmnop")
    monkeypatch.setattr(sys, "stdin", fake_input)

    main()

    captured = capsys.readouterr()

    assert captured.out == ""

def test_not_ready(monkeypatch, capsys):
    pass

def test_python_version():
    assert sys.version_info >= (3, 14)

@pytest.mark.xfail
def test_decorator_failure(monkeypatch, capsys):
    fake_input = io.String("")
    monkeypatch.setattr(sys, "stdin", fake_input)

    main()

    captured = capsys.readouterr()

    assert captured.out != ""

@pytest.mark.parametrize(
    "input_data,  output",
    [
        ("aaaa", ""),
        ("h3llt4ria9e\n", "h3llt4ria9e\n")
    ]
)
def test_parametrize(monkeypatch, capsys, input_data, output):
    fake_input = io.StringIO(input_data)

    monkeypatch.setattr(sys, "stdin", fake_input)

    main()

    captured = capsys.readouterr()

    assert captured.out == output
