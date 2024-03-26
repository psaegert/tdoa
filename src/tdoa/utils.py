import numpy as np
import random


def generate_random_tdoa_data(xmin: float, xmax: float, c: float = 343.0, n: int = 3, epsilon: float = 1, noise: float = 0.0) -> tuple[np.ndarray, np.ndarray, list[tuple[tuple[int, int], float]]]:
    """
    Generate random TDOA data for testing purposes.

    Parameters
    ----------
    xmin : float
        Minimum value for x and y coordinates.
    xmax : float
        Maximum value for x and y coordinates.
    c : float, optional
        Speed of sound in air (m/s), by default 343.0.
    n : int, optional
        Number of microphones, by default 3.
    epsilon : float, optional
        Minimum distance between microphones, by default 1.
    noise : float, optional
        Amount of noise to add to time differences, by default 0.0.
    """

    # Generate random sound location
    sound_loc = (random.uniform(xmin, xmax), random.uniform(xmin, xmax))

    # Generate random microphone locations
    mic_locations = [(random.uniform(xmin, xmax), random.uniform(xmin, xmax))]

    # Calculate time differences between pairs of microphones
    time_diffs = []
    for i in range(1, n):
        # Add a new microphone
        mic_locations.append((random.uniform(xmin, xmax), random.uniform(xmin, xmax)))

        # Ensure that new points are at least epsilon distance away from each other
        while np.sqrt((mic_locations[i][0] - mic_locations[i - 1][0])**2 + (mic_locations[i][1] - mic_locations[i - 1][1])**2) < epsilon:
            mic_locations[i] = (random.uniform(xmin, xmax), random.uniform(xmin, xmax))

        # Select one of the previous microphones as a parther for the new microphone
        j = random.randint(0, i - 1)

        d1 = np.sqrt((sound_loc[0] - mic_locations[i][0])**2 + (sound_loc[1] - mic_locations[i][1])**2)
        d2 = np.sqrt((sound_loc[0] - mic_locations[j][0])**2 + (sound_loc[1] - mic_locations[j][1])**2)
        time_diff = (d1 - d2) / c
        time_diff += random.uniform(-noise, noise)
        time_diffs.append(((i, j), time_diff))

    return np.array(sound_loc), np.array(mic_locations), time_diffs
