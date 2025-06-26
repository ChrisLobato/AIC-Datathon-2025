# AIC Datathon 2025 - From Rate to Reality: a RateMyProfessor deepdive
# Christopher Lobato, Karen Cho


## Description
Our winning submission for the Student Life Track for a 5 hour datathon in which we did an analysis of Stony Brook University class ratings on Rate My Professor.


## Goal
Stony Brook University has many classes of varying difficult in the engineering department that have a variety of requirements like mandatory attendance or mandatory textbook and sometimes classes can be taught by different professors in the same semester. 
The mission of this project was to gain some insight on what factors students consider when they grade a class as 'difficult' to better help students who are uncertain about what classes they would enjoy, and to better help professors understand what factors cause students to do poorly.

## Google Collab Links
[Data Analysis Collab](https://colab.research.google.com/drive/1pMhZbP_V2k7COGfLxRUEfZjKBviP8oxq?usp=sharing)


[Web Scraping Collab](https://colab.research.google.com/drive/1m0FziomUFKMj_hT0vHceA2DGkpMg9L3Y?usp=sharing)

## Repo overview
The **AIC Datathon 2025.pdf** is our presentation submission which we presented infront of the Stony Brook University faculty judging the competition. In this presentation we included the visual insights of the project, like correlation matrix and distribution graphs. **rmpScrape.py** is a python file of the same code included in the Web Scraping Collab, and we used this to obtain our own dataset for the competition. **ese_ratemyprof.csv** is a sample of what the output of the webscrape looks like.

## Conclusions 
Initially we assumed that there would be a direct correlation between factors like attendance mandatory and class difficulty and an inverse correlation between GPA and class score. However, what we found is that these factors don't always have a strong impact on students' scoring of a class and instead students' scoring is sometimes more nuanced, with difficult classes often receiving positive scores despite lower GPA distributions. Ultimately the data is incomplete, since students can omit certain fields on a review and neither are students required to submit a review after completing a class. To improve our dataset we would likely have to employ data from Stony Brook's Classie Evaluation system to impute missing data in our RateMyProfessor Dataset and compare them with each other to see if student sentiment is drastically different between the two platforms.  
