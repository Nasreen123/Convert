import pytest
import Convert

Class TestConvert:
    def test_help():
        pass
        #assert Convert.run("help") ==

    def test_conversions():
        assert Convert.run(1, "ft", "in") == 12
        assert Convert.run(1, "ft", "cm") == 30.48
        assert Convert.run(1, "yd", "ft") == 3
        assert Convert.run(1, "yd", "in") == 36
        assert Convert.run(1, "m", "yd") == 1760
