# Exoplanet Spectrum & Light Curve Analysis

This project analyzes an exoplanet observation using both **TESS light curves** and **spectral FITS data**.  
It performs three main tasks:

1. **Light Curve Processing** — load, clean, and fold a TESS light curve.  
2. **Spectrum Visualization** — read a spectral FITS file and plot wavelength vs flux.  
3. **Spectral Line Detection** — normalize the spectrum, smooth noise, and detect peaks that correspond to possible atmospheric elements.

---
Features
- Opens and inspects FITS files using **Astropy**
- Processes TESS light curves using **Lightkurve**
- Normalizes and smooths spectral flux
- Detects prominent spectral lines using **SciPy**
- Plots raw and processed data using **Matplotlib**

---

Project Structure
exoplanet-spectrum-analysis/
│
├── src/
│ ├── lightcurve_analysis.py # TESS light curve loading & folding
│ ├── spectrum_plot.py # Basic spectrum plot (flux vs wavelength)
│ └── peak_detection.py # Normalization + smoothing + peak detection
│
├── data/
│ └── example.fits # Sample FITS file (optional)
│
├── requirements.txt
└── README.md

How to Run

###1. Install dependencies

pip install -r requirements.txt
2. Run individual scripts
bash
Copy code
python src/lightcurve_analysis.py
python src/spectrum_plot.py
python src/peak_detection.py
Each script will load the james.fits (or your chosen FITS file) and generate the output plots.

📘 Requirements
See requirements.txt for all packages needed.
