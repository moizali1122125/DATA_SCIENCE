#Print a name
a <- 'moiz'
print(a)

{
# To read data
install.pakages('readxl') # to read excel file
install.pakages('readr')  # to read csv or other files
install.pakages('datapasta') # copy clipboard
# To handle data or explore it
install.pakages('dplyr')
install.pakages('tidyr')
# writing data and export into files
install.pakages('writeXLS')
# Visualization
install.pakages('ggplot2')
install.pakages('plotly')
install.pakages('ggpubr')
install.pakages('ggthemes')
install.pakages('viridis')
# set of most pakages
install.pakages('tidyverse')
}



# FOR IMPORTING LIBRARIES
# To read data
library('readxl') # to read excel file
library('readr')  # to read csv or other files
library('datapasta') # copy clipboard
# To handle data or explore it
library('dplyr')
library('tidyr')
# writing data and export into files
library('writeXLS')
# Visualization
library('ggplot2')
library('plotly')
library('ggpubr')
library('ggthemes')
library('viridis')
# set of most pakages
library('tidyverse')


# let's use these packages and turn them into data driven decision making
data()

data('diamonds')    # for impording buildin data
remove('diamonds')  # for removing data

?diamonds     # for knowing data (meta-data)
summary(diamonds)   # describe function in PYTHON
glimpse(diamonds)

head(diamonds)
tail(diamonds, 2)

str(diamonds)   # Structure of data

## Visualization and explore the Categorical DATA

qplot(diamonds$cut) # also write like     qplot(cut, data=diamonds)
