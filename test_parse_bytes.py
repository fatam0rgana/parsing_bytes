import pytest
from parse_bytes import parse_bytes, get_data_from_payload
from test_data import test_data


@pytest.mark.parametrize('payload, expected_result', [('10FA0E00', ['00010000',
                                                                    '11111010',
                                                                    '00001110',
                                                                    '00000000']),
                                                      ('11111111', ['00010001',
                                                                    '00010001',
                                                                    '00010001',
                                                                    '00010001']),
                                                      ('00000000', ['00000000',
                                                                    '00000000',
                                                                    '00000000',
                                                                    '00000000'])])
def test_parse_bytes(payload, expected_result):
    assert parse_bytes(payload) == expected_result


def test_value_error_in_byte_parsing():
    with pytest.raises(ValueError):
        parse_bytes('qwe')


@pytest.mark.parametrize('payload, expected_result', [(test_data[0][0], test_data[0][1]),
                                                      (test_data[1][0], test_data[1][1]),
                                                      (test_data[2][0], test_data[2][1])])
def test_getting_data_from_payload(payload, expected_result):
    assert get_data_from_payload(payload) == expected_result


def test_value_error_in_getting_data():
    with pytest.raises(ValueError):
        get_data_from_payload('qwe')


def test_len_control_in_getting_data():
    with pytest.raises(IndexError):
        get_data_from_payload('10FA0E000')
