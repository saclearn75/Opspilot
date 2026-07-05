# BUG REPORT: Biomarker Cards Layout Overflow on Mobile Viewports

## Description

When the dashboard is viewed on mobile screens or when browser window widths are reduced, the biomarker cards fail to scale properly. The current static widths cause the biomarker values and titles to aggressively overflow, overlap, and clip out of their container borders, making the metrics unreadable for clinical staff.

## Requested Fixes

1. Modify the biomarker card layout container inside `main.py`. Remove the rigid width/height constraints.

2. Use modern, responsive Tailwind utilities (like a responsive grid `grid-cols-1 md:grid-cols-3` or flexbox with `flex-wrap`) to ensure the cards stack vertically on mobile layouts and line up cleanly side-by-side on desktop.

3. Ensure padding, spacing, and text sizes dynamically scale so no clinical data is truncated.