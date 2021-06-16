from pytest import mark

@mark.body
class BodyTests:

    @mark.door
    def test_body_functions_as_expected(self):
        assert True

    def test_new_second_function_as_expected(self):
        assert True