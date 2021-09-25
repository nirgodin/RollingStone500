# RollingStone

## About
This project analyses the new RollingStone magazine [500 best songs of all time](https://www.rollingstone.com/music/music-lists/best-songs-of-all-time-1224767/) list, released on 05/09/2021, and compares this list to the [previous version](https://www.rollingstone.com/music/music-lists/500-greatest-songs-of-all-time-151127/) of this list from 2004.
Most of the analysis is done by parsing the raw text from the rolling stone website. Supplementary data is drawn from the Spotify API, using Python's [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/) module.

## Project requirements
To install the required modules for this project, just run the following command on terminal:
```pip install -r .\resources\requirements.txt```

To run the entire projcet just set the main folder as the project's directory and run ```main.py``` file

## Porject structure
<p align="center">
  <img src="/resources/project_structure.png" width="600"/>
</p>

## Key results

### Genres
<p align="center">
  <img src="/charts/Genres.png" width="600"/>
</p>

### Release Year
<p align="center">
  <img src="/charts/YearHistogram.png" width="600"/>
</p>

### Popularity
<p align="center">
  <img src="/charts/Popularity.png" width="600"/>
</p>

### Songs duration
<p align="center">
  <img src="/charts/DurationHistogram.png" width="600"/>
</p>

### Black Artists
<p align="center">
  <img src="/charts/BlackPercentage.png" width="600"/>
</p>

### Female Artists
<p align="center">
  <img src="/charts/FemalePercentage.png" width="600"/>
</p>

### Black Female Artists
<p align="center">
  <img src="/charts/BlackFemalePercentage.png" width="600"/>
</p>
