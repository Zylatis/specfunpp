from hypothesis import given, settings
import hypothesis.strategies as st

from mpmath import besselj
import numpy as np
import interfaces.bessel_cyl_jvz as j0


@given(st.floats(min_value = 0.0, max_value = 5.0, allow_nan=False))
@settings(max_examples=1000)
def test_j0_smallz(z):
    assert np.isclose(j0.j0z(z), float(besselj(0, z)), rtol=5e-15)