from pyparts.logic.pid_controller import PIDController


class TestClass:
    def test_one(self):
        controller = PIDController(1, 2, 3)
        assert controller.get_output(1) != 0
