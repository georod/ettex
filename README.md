# ettex

The Ecuador Travel and Tourism Explorer (ETTEX) is a bilingual (Spanish/English) interactive web map displaying 200+ points of interest. The aim of this web map is to help travellers find tourism attractions in Ecuador.

The web map is built with HTML, CSS and JavaScript. It uses Mapbox GL JS for the map and clustering, and Papa Parse to read the CSV in the browser. Pop-ups and a detail panel show photos, descriptions, and climate variables. Visitors can search keywords or phrases and filter by categories, province, and numeric variables. Images are served and resized by Cloudinary, and the static site is hosted on GitHub Pages. No backend or database is needed.

The web map app is powered by a CSV file that contains the data. The bulk of the data comes from Ecuador's Ministry of Tourism (MINTUR 2019). The original data, an Excel file, was imported to a PostgreSQL (+ PostGIS) database where the records were cleaned, validated, and standarized. The original data came with coordinates and pictures. Using GIS operations, the coordinates were used to enrich the data with climate and environmental variables.

This project is based on a travel web map I built back in 2019. This current version was created with the help of Anthropic's Claude (Desktop version).  This is my first time using AI to build an app and I am amazed by the tech. It only took me about three days to finish this first version of the app. (Note: the data were already collected, cleaned, validated, integrated, and ready to go.) 

With AI, coding up an app is no longer the hardest part. Rather, the hardest step seems to be procuring the different data and putting it all together in a way that allows the AI to easily use it.

## Data sources

1. Ministerio de Turismo del Ecuador (MINTUR). Atractivos turisticos del Ecuador (2019).
2. Koppen-Geigen climate regions
3. NASA Shuttle Radar Topography Mission Elevation (resolution: 30 m)
4. NASA Ambient Air Temperature (resolution: monthly, 0.5x0.5 decimal degrees)
5. NASA Precipitation (resolution: monthly, 0.5x0.5 decimal degrees)
