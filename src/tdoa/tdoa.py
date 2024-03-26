from scipy.optimize import fsolve, least_squares
import numpy as np


def tdoa_trilateration(mic_locations: np.ndarray, time_diffs: tuple, c: float = 343.0) -> np.ndarray:
    """
    Perform trilateration using the method of least squares.

    Parameters
    ----------
    mic_locations : np.ndarray
        (N x 2) array containing microphone locations.
    time_diffs : tuple[tuple[int, int], float]
        Tuple containing pairs of microphone indices and corresponding time differences.
    c : float, optional
        Speed of sound in air (m/s), by default 343.0.

    Returns
    -------
    np.ndarray
        Estimated sound location.
    """

    def equations(p: tuple[float, float]) -> list[float]:
        x, y = p
        eqns = []
        for (i, j), time_diff in time_diffs:
            eqn = (np.sqrt((x - mic_locations[i, 0])**2 + (y - mic_locations[i, 1])**2) - np.sqrt((x - mic_locations[j, 0])**2 + (y - mic_locations[j, 1])**2)) - c * time_diff
            eqns.append(eqn)
        return eqns

    if len(time_diffs) == 2:
        return fsolve(equations, (0, 0))

    return least_squares(equations, (0, 0)).x
