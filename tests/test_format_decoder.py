import pytest
from gen_diff.engine import format_decoder, jsn_open, yml_open

def test_format_decoder():
    f1 = 'tests/fixtures/file1.json'
    f2 = 'tests/fixtures/file2.yml'
    f3 = 'tests/fixtures/result.txt'
    assert format_decoder(f1) == jsn_open(f1)
    assert format_decoder(f2) == yml_open(f2)
    with pytest.raises(ValueError):
        format_decoder(f3)
