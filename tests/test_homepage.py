def test_gotohomepage(driver_mock, homep):
    homep.gotohomepage()
    assert driver_mock.get.called
