from {{cookiecutter.package_python_name}}.dummy import dummy


def test_dummy():
    d = dummy()
    assert d
