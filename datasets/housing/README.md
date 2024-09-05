# California Housing

## Source

From url[AGeron]{https://github.com/ageron/handson-ml2}

> This dataset is a modified version of the California Housing dataset available from Luís Torgo's page (University of Porto). Luís Torgo obtained it from the StatLib repository (which is closed now). The dataset may also be downloaded from StatLib mirrors.
>
> This dataset appeared in a 1997 paper titled Sparse Spatial Autoregressions by Pace, R. Kelley and Ronald Barry, > published in the Statistics and Probability Letters journal. They built it using the 1990 California census data. It > contains one row per census block group. A block group is the smallest geographical unit for which the U.S. Census > Bureau publishes sample data (a block group typically has a population of 600 to 3,000 people).
> 
> ## Tweaks
> 
> The dataset in this directory is almost identical to the original, with two differences:
>
> - 207 values were randomly removed from the total_bedrooms column, so we can discuss what to do with missing data.
> - An additional categorical attribute called ocean_proximity was added, indicating (very roughly) whether each block group is near the ocean, near the Bay area, inland or on an island. This allows discussing what to do with categorical data.
> 
> Note that the block groups are called "districts" in the Jupyter notebooks, simply because in some contexts the name "block group" was confusing.