RAW MATERIALS SPICES PRICE PREDICTION
•	Business Problem: Unpredictable fluctuations in raw spice prices negatively impact cost structure and inventory management.
•	Business Objectives: Maximize cost savings through effective inventory management.
•	Business Success Criteria: Optimize procurement strategies and reduce production cost by 10%.
•	Economic Success Criteria: Achieve cost savings in raw material procurement and inventory management by at least 20%.
Data Overview
•	Dataset: Raw spice price data from April 2021 to April 2023.
•	Variables: Month&Year, Spices, Location, Grade, Price.
•	Data Structure: Rectangular with 715 rows and 5 columns.
•	Columns:
1.	Month&Year: The month and year of the recorded data.
2.	Spices: The type of spice.
3.	Location: The location of procurement.
4.	Grade: The grade of the spice.
5.	Price: The price of the spice.  
Data Cleaning and Preprocessing
•	Missing Values: None identified.
•	Outliers: Examined using boxplots and IQR, addressed if necessary.
•	Formatting: Ensured consistency in date/time formats, units, etc.

Descriptive Statistics
•	count     690.000000
•	mean     4768.268188
•	std     33290.511477
•	min        32.500000
•	25%       118.075000
•	50%       258.355000
•	75%       693.355000
•	max    675000.000000

Univariate Analysis
•	Spices:
o	Distribution of prices for each spice across time.
o	Identify spices with the most significant price fluctuations.
o	Consider potential factors influencing price variations (seasonality, supply/demand, quality, etc.).
•	Locations:
o	Price comparisons across different locations for the same spice and grade.
o	Investigate reasons for location-based price differences (transportation costs, local market factors, etc.).
•	Grades:
o	Analyze price variations based on spice grade.
o	Determine if cost savings can be achieved by strategically procuring different grades.
•	Price:
o	Overall price distribution.
o	Identify periods of significant price increases or decreases.
o	Explore potential patterns or trends.

Bivariate and Multivariate Analysis
•	Correlations:
o	Assess relationships between spices, locations, grades, and price.
o	Identify potentially influential factors for price variations.
•	Regression Analysis:
o	Build models to predict price based on other variables (if appropriate).
o	Evaluate model performance and interpret results.
•	Time Series Analysis:
o	Analyze price trends over time.
o	Forecast future prices to inform procurement decisions.

Data Visualization
•	Charts and graphs: Use clear and informative visualizations to present findings.
•	Examples:
o	Line charts to show price trends over time.
o	Boxplots to compare price distributions across spices, locations, and grades.
o	Scatter plots to explore correlations between price and other variables.
o	This is done using POWER BI TOOL.

Insights and Recommendations
•	Procurement Strategies:
o	Based on price volatility and correlations, suggest strategies for buying spices at optimal times and locations.
o	Consider grade substitutions when feasible to reduce costs.
•	Inventory Management:
o	Recommend inventory levels based on predicted price trends and anticipated demand.
o	Implement just-in-time (JIT) inventory management if applicable.
•	Further Analysis:
o	If relevant, suggest additional data to be collected or analyses to be conducted for more insights.

Time Series Forecasting:
Model Selection:
Autoregressive Integrated Moving Average (ARIMA):
Evaluate the suitability of ARIMA models for each spice type.
Seasonal-Trend decomposition using LOESS (STL):
Explore STL for capturing non-linear trends and seasonality.
Model Performance:
Train-Test Split:
Split the dataset into training and testing sets to evaluate model performance.
Forecast Accuracy Metrics:
Utilize metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) for model evaluation.

Key Insights:
1.	Seasonal decomposition reveals clear patterns in spice prices, allowing for effective time series modeling.
2.	ARIMA and STL models demonstrate promising forecasting capabilities.
3.	Evaluate forecast accuracy metrics to ensure the reliability of predictions.






