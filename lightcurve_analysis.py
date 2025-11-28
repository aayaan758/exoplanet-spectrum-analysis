# Import required libraries
from astropy.io import fits
from lightkurve import TessLightCurveFile
import matplotlib.pyplot as plt

# Step 1: Specify the path to your FITS file
file_path = "james.fits"  # Replace with the actual path to your FITS file

# Step 2: Inspect the FITS file
print("Inspecting the FITS file...")
hdul = fits.open(file_path)
hdul.info()  # View the structure of the file

# Optional: Check the header of the primary or secondary extension
print("\nPrimary Header:")
print(hdul[0].header)  # Metadata about the observation
print("\nData Header (Extension 1):")
print(hdul[1].header)  # Header for the first data extension (if available)

# Step 3: Analyze the light curve using Lightkurve
print("\nLoading the light curve...")
lc_file = TessLightCurveFile(file_path)  # Load the FITS file as a TESS Light Curve file
lc = lc_file.PDCSAP_FLUX  # Extract the Pre-search Data Conditioning Simple Aperture Photometry flux

# Step 4: Plot the raw light curve
print("Plotting the light curve...")
plt.figure(figsize=(10, 6))
lc.plot(title="TESS Light Curve (Raw)")
plt.show()

# Step 5: Clean the light curve (optional)
print("Cleaning the light curve...")
lc_cleaned = lc.remove_nans().remove_outliers(sigma=5)

# Step 6: Plot the cleaned light curve
print("Plotting the cleaned light curve...")
plt.figure(figsize=(10, 6))
lc_cleaned.plot(title="TESS Light Curve (Cleaned)")
plt.show()

# Step 7: Fold the light curve (optional)
# If you know the orbital period of the exoplanet, fold the light curve to align all transits
period = 2.204735  # Example period in days (replace with your target's period if known)
print(f"Folding the light curve with a period of {period} days...")
lc_folded = lc_cleaned.fold(period=period)

# Step 8: Plot the folded light curve
print("Plotting the folded light curve...")
plt.figure(figsize=(10, 6))
lc_folded.plot(title=f"TESS Light Curve (Folded at {period} days)")
plt.show()

# Close the FITS file to free resources
hdul.close()
