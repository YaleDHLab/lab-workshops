# Introduction to Data Visualization with Tableau Public

## Overview
[Tableau Public](https://public.tableau.com/en-us/s/) is a free visualization suite for creating interactive data visualizations online. The software provides detailed data overviews and enables toggling between different visualizations in a single click, making it easier to see which works better for the data and questions at hand.   

While Tableau runs locally, it saves publicly. For data with privacy restrictions, you should use Tableau Desktop, which runs on and saves to your local machine. [Students](https://www.tableau.com/academic/students?utm_campaign_id=2019176&utm_campaign=Prospecting-PROD-ALL-ALL-ALL-ALL&utm_medium=Paid+Search&utm_source=Google+Search&utm_language=EN&utm_country=USCA&kw=tableau%20for%20students&adgroup=CTX-Brand-Student-E&adused=RSA&matchtype=e&placement=&gclid=EAIaIQobChMI4uyd9faW6gIVkYbACh2MZgwNEAAYASAAEgIG6PD_BwE&gclsrc=aw.ds) and [educators](https://www.tableau.com/academic/teaching?utm_campaign_id=2019176&utm_campaign=Prospecting-CORE-ALL-ALL-ALL-ALL&utm_medium=Paid+Search&utm_source=Google+Search&utm_language=EN&utm_country=USCA&kw=%2Btableau%20for%20%2Bteachers&adgroup=CTX-Brand-Teaching-B&adused=ETA&matchtype=b&placement=&gclid=EAIaIQobChMIp5Spi_eW6gIVycDACh2PAQkjEAAYASAAEgLwKvD_BwE&gclsrc=aw.ds) can sign up for free yearly licenses to Tableau Desktop.

## Example Project: Internet Users By Country Over Time
To practice working in Tableau Public, download this [dataset of internet users per 100 people](https://github.com/YaleDHLab/lab-workshops/blob/master/tableau/data/internet-users-knoema-world-data-atlas.csv) by going to the dataset, clicking "Raw," and then at the top of your browser, select "File" and "Save Page As..." Make sure that the file format saves as a comma separated value (CSV) file. This dataset was published by Tableau Public in 2018, but was originally published on [Knoema](https://knoema.com/WBINU2018/internet-users-per-100-people). The spreadsheet includes three variables or columns ("Country," "Internet users per 100 people," "Year") and 1,764 records or rows.

As a sample research scenario, let's imagine that someone just handed us this data. To get a better feel for its quality and what questions we might ask of it, we can create a few exploratory data visualizations in Tableau Public.

### Set Up
1. [Download, install, and then open Tableau Public](https://public.tableau.com/en-us/s/).
2. Under "Connect," click on "Text file" and select the internet users CSV file. This will load a preview of your dataset. 
3. Review Tableau's guesses as to what data types it's observing. The representations are as follows:  
- Globe = geospatial data, 
- Hashtag = numeric data, 
- Abc = string (text) data,
- T|F = Boolean (true or false) data
- Calendar = temporal data.  
For our dataset, we need to change the "Year" column from a numeric value to a date. To do so, click on the hashtag symbol above "Year" and select "Date." You should notice that all of our years now also have a month and day attached to them; by default, Tableau treats dates as day-month-year.
4. To begin working with our data, click on the orange "Sheet 1" rectangle toward the bottom left-hand corner of the application. This will create our first Tableau sheet, a blank space for generating visualizations.

### Interface Changes
Tableau version 2020.2 underwent major interface and functionality changes. You can read about all of the differences on [Tableau's website](https://help.tableau.com/current/pro/desktop/en-us/datasource_datamodel_whatschanged.htm). Below, I will describe the most notable differences you'll see from the main interface.

#### Pre-2020.2 Tableau Versions
- On the left-hand column, there is the "Data" pane that sorts our data into "Dimensions" (categorical data) and "Measures" (numeric data). Under "Measures," you will see that Tableau has also automatically generated two additional measures: "Number of Records" (number of rows in the dataset) and "Measure Values" (sum of all values). 

#### Tableau Version 2020.2
- On the left-hand column, Tableau now groups data as "Tables." While Tableau no longer explicitly calls out "Dimensions" and "Measures," there is a horizontal line that separates categorical and numeric data.
- Tableau still generates two fields: "Measure Values" (sum of all values) and the previously named "Number of Records," which now takes the name of your file.

#### Interface Interactions 
Double-clicking or dragging any dimension or measure over to the "Columns" and "Rows" sections near the middle-top of the sheet will give you the opportunity to examine the data more closely. You can use the back arrow at the top left to undo actions.  
- "Pages," "Filters," and "Marks" are where you will drag dimensions and measures in order to filter the data.
- The "Show Me" button on the top right can be clicked on and off. When clicked on, it shows you different visualizations you can toggle between, along with what kind of data you need in order to generate them. Toggle "Show Me" off for now, since it takes up screen real estate and will hide our filter settings (once we create a filter).

### Bar Chart: Number of Internet Users
1. Drag "Country" to "Rows."
2. Drag "Internet users" to "Columns."
3. Sort data from most to least by clicking the icon with the three stacked rectangles and downward arrow. 
4. Challenge: if our dataset is internet users per 100 people, then why does Iceland show 708.8 users? Tableau is summing all values that correspond with an "Iceland" row. To see internet users per 100 people, we need to add a year filter.
5. Create year filter by dragging "Year" to the "Filters" card. 
- Select "Years" in the resulting pop-up box.
- Click the "All" box.
- Click "Ok."
- To set the filter, click on the dropdown by "YEAR(Year)," and select "Show Filter." This will show the filtering options in the right-hand column (you may have to click of "Show Me" to see it).
- In the right-hand column, click the dropdown by "YEAR(Year)," and select "Single Value (list)" to filter by year.
6. We can now start asking questions of the data. For example, what 5 countries had the most early adopters of the internet? What 5 countries have the most internet users per 100 people?
7. Filter to countries of interest by dragging "Country" to the "Filters" card. This time, select countries of interest. If we'd like to compare greatest number of users in 1990 to 2015, we might select: the United States, Norway, Switzerland, Australia, Sweden, Iceland, Luxembourg, Andorra, Liechtenstein.
8. Convert our time filter to an automated time slider by dragging "YEAR(Year)" from the "Filters" card to "Pages." In the right-hand column, you can click the right triangle button to activate the time slider and see how the number of users changes over time.
9. Give a title to the chart by double clicking on the current "Sheet 1" title and inserting "Internet Users per 100 People by Country and Year." Leave "<Page Name>" there since it will automatically show what year we're viewing. Click "Apply" to see what the title will look like. Then click "Ok."
10. Change the "Sheet 1" name in the lower left-hand corner by double clicking on it and renaming it "bar chart."
 
### Line Graph: Change over Time
1. Start a new sheet by clicking the icon next to our current sheet.
2. Double click on "Year" (this should add it to the "Columns" section)
3. Double click on "Internet users" (this should add it to the "Rows" section)
4. Drag "Country" to the "Color" mark - note the warning that there would be too many colors to be legible if we don't filter first. To see what happens, click "Add all members." While the resulting line graph shows an overall increase in the number of users, it's hard to track individual changes. Click the back arrow in the top-left corner to undo.
5. Drag "Country" to the "Color" mark again, but this time, click "Filter and then add." Choose countries of interest (you might choose the same countries from the bar chart).
6. Change colors by clicking on the dropdown next to "Country" in the right-hand column. Select a palette from the dropdown, or double click on the color by an individual country's name to change it. When you have colors you like, click "Assign Palette" to see what they look like on the graph. Then click "Ok." 
7. Give the graph the title: "Internet Users over Time by Country"
8. Rename the sheet to "line graph"

### Map: Internet Users by Country
1. Start a new sheet.
2. Drag "Country" to "Columns."
3. Drag "Internet Users" to "Rows."
4. Click to turn on "Show Me" and select the second map, which will generate a choropleth map.
5. Notice that not all countries are being recognized by Tableau. Click on "3 unknown" in the lower right-hand corner of the map to give Tableau a mapping between countries' names in our dataset, and countries' names Tableau knows. 
- Dem. People's Rep. Korea to North Korea
- Dem. Rep. Congo to Democratic Republic of Congo
- Korea to South Korea.
6. Drag "Year" to "Pages" to see change over time.
7. Give the map the title: "Map of Internet Users per 100 People over Time."
8. Rename the sheet to "map."

### Data Dashboard: Combine Visualizations Together
1. Start a data dashboard by clickong in the icon next to the sheet icon.
2. Adjust the size of the dashboard by clicking on the dropdown under "Size" in the left-hand column. To have the dashboard take up the size of the screen you're using, click the size dropdown and then click the dropdown by "Range" and select "Automatic."
3. Double click on sheets to add them to the dashboard. Practice re-arranging them on the dashboard.
4. Add a component to the dashboard that links out to the Wikipedia page for whichever country a user selects.
- Drag a "Web Page" object onto the dashboard and click "Ok" without adding a URL. 
- On the dropdown box for the web page object, click "Add URL Action."
- In the name field, type: "Go to Wikipedia page for" and cilck the triangle button at the end of the line and select "Country."
- For "Run action on," choose "Hover."
- For URL, add: "https://en.wikipedia.org/wiki/" and then click on the triangle button and select "Country."
- Click "Test Link" to see if it's working.
- Click "Ok" and "Ok" again to add the action.
- Hover on any data point in the dashboard, and the Wikipedia page will automatically update to reflect the country that's been selected. ![Dashboard View](https://github.com/YaleDHLab/lab-workshops/blob/master/tableau/image/dashboard.png)
 
### Save Your Workbook
To save your workbook, you have to create a free Tableau account. When you click save, you will be prompted to log in and save your workbook to Tableau's server, where it will be visible on Tableau Public. Users can interact with your workbook on Tableau Public, or they could download, add to, or otherwise edit it.

## Next Steps, Cautions, & Additional Tips
* Watch Tableau's free, online [training videos](https://www.tableau.com/learn/training/20201) to learn more about joining multiple datasets, creating dashboards, and running calculations.
* Tableau frequently has updates availability, but they're not always backwards compatible. For that reason, you might not update to the newest version while you're in the middle of a project.
* For additional practice and open datasets, check out [#MakeoverMonday](https://www.makeovermonday.co.uk/). Every week, Tableau shares a dataset and start visualization, and you're challenged to remake it. You can see how others take up the challenge on [Twitter](https://twitter.com/hashtag/makeovermonday?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Ehashtag). See a makeover visualization you like? Download their workbook to see how they made it!
