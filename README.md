# Election-Analysis

## Objectives
we analyzed the performance of twelve different stocks across two years in order to identify trends and help guide clients in their portfolio decisions. To this end. We created a program that can take raw stock data from an Excel sheet and create a chart that, on an accessible glance, gives each stock, how active that stock was in a given year, and where that stock ended out in comparison to its start price for the year. 

##results
This selection of data allows a user to not only see what stocks have the greatest volume, but also to compare stocks' growth from year to year. For example, in the below images you can see that, while most of the stocks performed well in 2017, only  two stocks maintained growth through the difficult 2019 fiscal year. Comparing these we may recommend that an investor may prefer to shift their portfolio to favor ENPH, as it's the only stock on the list which performed well both years. 

![2017 stock analysis results](https://github.com/Mickie-n-s/Election-Analysis/blob/main/stocks_performance_2017.png) 
![2018 stock analysis results](https://github.com/Mickie-n-s/Election-Analysis/blob/main/stocks_performance_2018.png)

##Summary
After our initial scriptwriting, we refactored the script to run more efficiently. Our initial script ran a full analysis and formatting for each stock in a given list, and as such was doing a lot of reduntant processes. by streamlining the process to only do setup and formatting once, and making the analysis process more efficient as well, we reduced the processing time from .66 seconds to .05 seconds. While that may seem negligible, consider that this dataset only had twelve stocks- if you had a dataset with dozens or hundreds of stocks, that 10 reduction in processing time would become a substantial timesave. The downside of the refactoring we did is that the scriptwriter needs to know exactly how many stocks are being analyzed before running, which can become something of a hassle if the users want to consider varied sets of data. 
