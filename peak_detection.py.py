import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from scipy.signal import find_peaks
from scipy.ndimage import gaussian_filter

# Open the FITS file
filename = "james.fits"
hdul = fits.open(filename)

# Extract data
data = hdul[1].data
wavelength = data['WAVE'][0]
flux = data['FLUX'][0]
flux_error = data['ERR'][0]

# Normalize the flux values
flux_min, flux_max = np.min(flux), np.max(flux)
flux_normalized = (flux - flux_min) / (flux_max - flux_min)

# Apply Gaussian smoothing to reduce noise
flux_smooth = gaussian_filter(flux_normalized, sigma=2)

# Find peaks in the spectrum (potential spectral lines)
peaks, _ = find_peaks(flux_smooth, height=0.5, distance=5)

# Plot the spectrum with detected peaks
plt.figure(figsize=(10, 6))
plt.plot(wavelength, flux_smooth, label='Smoothed Flux', color='blue')
plt.scatter(wavelength[peaks], flux_smooth[peaks], color='red', label='Peaks')
plt.fill_between(wavelength, flux_smooth - flux_error, flux_smooth + flux_error, color='blue', alpha=0.2, label='Flux Error')
plt.xlabel('Wavelength (Angstrom)')
plt.ylabel('Normalized Flux')
plt.title('Preprocessed Spectrum with Detected Peaks')
plt.legend()
plt.grid()
plt.show()

# Close the FITS file
hdul.close()
