from pytest import mark


def test_this_should_always_pass():
    assert True


@mark.skip(reason="Boken, fixing next sprint")
def test_this_needs_work():
    assert False


@mark.xfail(reason="This feature should hae been deprecated")
def test_this_should_always_fail():
    assert False
