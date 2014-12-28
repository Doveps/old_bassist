import pytest

import parser.log_file.common

@pytest.fixture(scope='function')
def common_log():
    return parser.log_file.common.Log('path/to/nonexistent')

def test_path(common_log):
    assert common_log.path == 'path/to/nonexistent'

def test_log(common_log):
    assert common_log.log == 'common'