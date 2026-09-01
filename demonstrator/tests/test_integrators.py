import numpy as np

from trias_demo.config import DemoConfig
from trias_demo.integrators import integrate_fixed
from trias_demo.metrics import position_error
from trias_demo.reference import integrate_reference


def test_u1_fixed_step_runs_are_finite_and_refine():
    cfg = DemoConfig(refinements=(50, 100), runtime_repeats=1)
    times = cfg.output_grid("u1")
    masses = cfg.system.masses_array()
    y0 = cfg.system.initial_state()
    ref = integrate_reference(
        y0,
        times,
        masses,
        cfg.system.G,
        cfg.reference_rtol,
        cfg.reference_atol,
    )
    assert ref.success
    for method in ("rk4", "verlet"):
        errs = []
        for n in cfg.refinements:
            result = integrate_fixed(
                method,
                y0,
                times,
                cfg.system.T_pub / n,
                masses,
                cfg.system.G,
                cfg.min_pair_distance_abort,
            )
            assert result.valid
            assert np.isfinite(result.states).all()
            errs.append(position_error(result.states, ref.states, y0)[-1])
        assert errs[1] < errs[0]
