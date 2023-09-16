from main import main


def test_main():
    actual = main().to_csv()
    expected = open("expected.csv").read()

    assert actual == expected
