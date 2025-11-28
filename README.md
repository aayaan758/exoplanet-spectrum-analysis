#Exoplanet Spectrum & Light Curve Analysis

This project analyzes an exoplanet observation using both TESS light curves and spectral FITS data.
It includes three core components:

Light Curve Processing – Load, inspect, clean, and fold a TESS light curve.

Spectrum Visualization – Read a spectral FITS file and plot wavelength vs flux.

Spectral Line Detection – Normalize the spectrum, smooth noise, and detect peaks corresponding to possible atmospheric absorption/emission lines.


#Features

-Reads and inspects FITS files using Astropy

-Processes TESS light curves via Lightkurve

-Normalizes and smooths flux values

-Detects prominent spectral lines using SciPy

-Produces clear scientific plots using Matplotlib

#Project Structure
exoplanet-spectrum-analysis/
│
├── src/
│   ├── lightcurve_analysis.py     # TESS light curve loading and folding
│   ├── spectrum_plot.py           # Basic spectrum visualization
│   └── peak_detection.py          # Preprocessing and spectral line detection
│
├── data/
│   └── example.fits               # Sample FITS file (optional)
│
├── requirements.txt
└── README.md

#Installation

Install all requirements using:
pip install -r requirements.txt
Usage
Run each script independently:
python src/lightcurve_analysis.py
python src/spectrum_plot.py
python src/peak_detection.py

Each script will load the FITS file (default: james.fits) and generate the corresponding plot.

#Notes
The spectral FITS file must contain fields such as WAVE, FLUX, and ERR.
You may update the filename inside the scripts to use a different dataset.
The detected peaks indicate potential spectral lines but are not yet matched to specific elements. Line identification can be added as an extension.

#Future Improvements
Implement spectral line identification using atomic/molecular line lists
Add atmospheric retrieval methods
Automate transit parameter extraction from the light curve
License
This project is open-source and available under the MIT License.


