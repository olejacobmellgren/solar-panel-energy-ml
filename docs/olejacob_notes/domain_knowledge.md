
# EDA

Preparation is a crucial part of solving tasks and challenges using machine learning. To be able to make the best possible machine learning model we need to understand the field we are working in. As we are no experts in the area of energy production from solar panel, we must do some research in this field. By doing this, we will be able to better understand the data and therefore make a better model for the prediction task. 

The main part of the preparation is the exploratory data analysis (EDA). This analysis consists of research about the domain, checking data intuitivity, understanding the data and exploring individual or groups of features. By doing such an analysis we will be able to generate hypothesizes about the data and discover important insights. For example, we might be able to figure out which features in the dataset that could be ignored, and which ones should be emphasized. This will also prepare us for the feature engineering we must do at a later occasion.

## Solar panels and energy production

There are many factors that affect solar panels and their energy production. In our research about the field we are going to focus at the major factors that can make an impact. Later we are going to focus on more specific features in our dataset. Both reflecting around what we know about the subject, and researching for new information, will be valuable in the early stages of the process. 

#### Temperature

If we imagine the best possible weather for solar panels, we probably think of a day with clear sky, shining sun and high temperatures. However, research show that the best temperatures for solar panels is 77 degrees fahrenheit (25°C) (Akshay, 2022). This article also states that temperature is one of the most important factors that affect energy production by solar panels, which could be useful to remember. 

Another article refers to statistics when stating that temperatures above 77 fahrenheit actually can decrease the performance of the solar panels. In general, a solar panel will become one percent less efficient for each degree in fahrenheit above 77 °F (Wolf, n.d.). So depending on where in the world the solar panels are going to be utilized, it might vary whether they are more effective in the winter or summer.

#### Clouds and fog

The affect clouds have on the energy production of the solar panels are pretty stragihtforward. Anything the comes inbetween the sun and the solar panels, reduces the production of energy. But the solar panels can still produce energy when there are clouds, depending on the cloud coverage (Wolf, n.d.). Fog will also have the same effect, and anything that can cast a shadow over the panels like trees, buildings or other obstacles will reduce production. In our case, such details will be ignored as they are not relevant to our task.

#### Precipitation

Precipitation is any type of water vapor that falls from the clouds. In our research we have focused on the two major ones, rain and snow. The rain in itself will actually not have any impact on the production of the panels. Rain can actually help the production of energy by cleaning the solar panels for dust and dirt. (Wolf, n.d.) However, when there is rain, there are often clouds, and therefore we might be able to see a correlation between energy production and rain as well. 

Snow can have a very different affect than rain. Snow will cover the solar panels and in this way totally prevent production of energy. Solar panels are however often tilted so that snow could slide off easier. The solar panels might also be cleared for snow by people when there has been accumulated a lot of snow, but this is not something we can assume will happen. Just like with the rain, there will be clouds when we have snow, and we can assume that snow will have an impact on the production. As mentioned, they will also have an impact when it is not snowing and there are no clouds, by covering the panels.


##### Sources: 
Akshay, VR. (2022) *What's the optimal temperature for solar panels*, From URL: https://www.arka360.com/ros/optimal-temperature-solar-panels/

Wolf, S. (n.d.) *How does weather affect solar panels*, From URL: https://www.paradisesolarenergy.com/blog/how-does-weather-affect-solar-panels


