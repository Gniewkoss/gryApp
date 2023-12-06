import pytest
import math


@pytest.fixture(autouse=True)
def input_mock(request: pytest.FixtureRequest, monkeypatch: pytest.MonkeyPatch):
    try:
        mocked_data = list(reversed(request.param))

        def new_input(*args, **kwargs):
            return mocked_data.pop()

        monkeypatch.setattr("builtins.input", new_input)
    except AttributeError:
        pass


@pytest.mark.parametrize(
    "input_mock",
    (
        (
            "12",
            "10",
            "30",
            "60",
            "70",
            "80",
            "90",
            "120",
            "120",
            "130",
            "130",
            "150",
            "160",
            "482",
        ),
    ),
    indirect=True,
)
def test_all(capsys: pytest.CaptureFixture):
    import main

    assert set(
        math.ceil(int(l) / 100) * 100 for l in capsys.readouterr().out.split()
    ) == {200, 300}
