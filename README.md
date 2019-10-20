![Carpe Datum!](images/head.png)

### Motivation
How do we make mission critical decisions with incomplete data? Can we derive insights from the missing data? Our team is "chasing lost data" by developing an auto-ML imputation tool to mitigate data loss.


### The Challenge
Help find ways to improve the performance of machine learning and predictive models by filling in gaps in the datasets prior to model training. This entails finding methods to computationally recover or approximate data that is missing due to sensor issues or signal noise that compromises experimental data collection. This work is inspired by data collection during additive manufacturing (AM) processes where sensors capture build characteristics in-situ, but it has applications across many NASA domains.

#### Seal_Team_404
* Abhi Banerjee
* Kevin Africa
* Chris Bowers
* Grace Shea
* Jared Anderson
* Michael Palmer
* Shubha Rajan

**Space Apps Challenge Hackathon** - Seattle, WA - October 18-20, 2019

<p align="center">
  <img src="images/space_apps.png" width="350" title="NASA SpaceApps 2019 - Seattle ">
</p>

### Our Project
Carpe Datum, Utilize an ensemble of various cross-sectional & time series imputation techniques including mean, MICE, KNN & moving window to mitigate data loss.

Our solution is:

* A fully scalable Auto-ML Imputation web application
* Can be adapted easily for different data & file formats
* Helps users mitigate data loss easily with our tool
* Easily interpret model performance via custom scoring metrics

### Scope
### Data
We used turbo fan sensor data from NASA. Consists of 21 censor readings over time.

### Muting Data (Creating Nulls)
In order to train our model we needed a complete data set to determine how well we filled in nulls. There were no nulls in this dataset. We mimicked sensor failures by simulating sensors intermittently malfunctioning for durations of time. We felt this was more realistic than a sensor flickering one random unit of time to the next.

### Modeling
We used Imputation Methods from the impyute library 
* Mean - A benchmark to use a sensor's mean to fill in missing data
* MICE - Multiple Imputation by Chained Equations
* Fast KNN - Does an initial mean imputation to get a working array, then fill in nulls with weighted average of the K-nearest neighbors from the working array
* Moving Window - 

### Cross Validation
We compared model performance using Root Mean Square Error and compared our imputed results to the original data set. Our benchmark metric was based on the Mean Imputation.

### Links
- Presentation Slides: http://bit.ly/32siTkd
- GitHub: https://github.com/drunkONdata/carpe_datum
- SpaceApps Project Page: https://bit.ly/2VW9HC6

### Future Work
* Expand model offerings with additional models like: Bayesian No-U-Turn, Spline & Polynomial interpolation, GANs etc.
* Validate work & data pipeline with different types of data
* Expand error handling mechanisms
* Create dashboard that automatically updates population forecasts with updated satellite imagery data

### MIT License
Copyright (c) 2019 Carpe Datum

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
