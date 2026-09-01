import numpy as np

from trias_demo.config import DemoConfig
from trias_demo.metrics import position_error
from trias_demo.reference import integrate_reference


def test_tight_reference_is_close_on_u1():
    cfg = DemoConfig(runtime_repeats=1)
    times = cfg.output_grid("u1")
    masses = cfg.system.masses_array()
    y0 = cfg.system.initial_state()
    main = integrate_reference(
        y0,
        times,
        masses,
        cfg.system.G,
        cfg.reference_rtol,
        cfg.reference_atol,
    )
    tight = integrate_reference(
        y0,
        times,
        masses,
        cfg.system.G,
        cfg.tight_reference_rtol,
        cfg.tight_reference_atol,
    )
    assert main.success and tight.success
    gap = position_error(main.states, tight.states, y0)
    assert np.max(gap) < 1e-8
