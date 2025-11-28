import matplotlib.pyplot as plt
from astropy.io import fits

# Open the FITS file
filename = "james.fits"
hdul = fits.open(filename)

# Print file information
print("FITS File Info:")
hdul.info()

# Check column names in the second extension
print("\nColumn Names in Second Extension:")
print(hdul[1].columns)

# Extract data from the second extension (BinTableHDU)
try:
    data = hdul[1].data

    # Check available fields in the data
    print("\nAvailable fields in the data:")
    print(data.names)

    # Adjust these field names based on actual column names
    wavelength = data['WAVE'][0]  # Assuming the column contains arrays
    flux = data['FLUX'][0]
    flux_error = data['ERR'][0]

    # Plot the spectrum
    plt.figure(figsize=(10, 6))
    plt.plot(wavelength, flux, label='Flux', color='blue')
    plt.fill_between(wavelength, flux - flux_error, flux + flux_error, color='blue', alpha=0.2, label='Flux Error')
    plt.xlabel('Wavelength (Angstrom)')
    plt.ylabel('Flux (erg/cm²/s/Angstrom)')
    plt.title('Spectrum')
    plt.legend()
    plt.grid()
    plt.show()

except KeyError as e:
    print(f"KeyError: {e}. Check the column names in the FITS file.")
except IndexError as e:
    print(f"IndexError: {e}. Verify the structure of the data arrays.")
except Exception as e:
    print(f"Unexpected error: {e}")

# Close the FITS file
hdul.close()
