# ArcGIS StoryMaps

[StoryMaps](https://storymaps.arcgis.com/) is a free, open-source platform for combining texts, images, and videos alongside maps (though technically, maps aren't required!). In this workshop, we'll discuss the pros and cons of the various templates, offering tips along the way for how you might collect, analyze, and visualize the data that will serve as the basis for your StoryMap.

## Introduction: Explore some example StoryMaps
* [Preserving Significant Places of Black History](https://storymaps.arcgis.com/stories/2e2f8343e7254e948f5a0d3699ba91fd)
* [The lines that shape our cities: Connecting present-day environmental inequalities to redlining policies of the 1930s](https://storymaps.arcgis.com/stories/0f58d49c566b486482b3e64e9e5f7ac9?adumkts=product)

## Hands-on: Creating a StoryMap about Bubble Tea in New Haven

_In-class exercise_

## Advanced: Creating a map from a spreadsheet of data

1. Log in to [ArcGIS.com](http://arcgis.com)
2. Click "Sign In" in the upper right-hand corner
3. Click "Sign in with Enterprise Account"
4. Type "yalemaps" into the address as indicated and press "Continue"
 ![screenshot](https://github.com/YaleDHLab/lab-workshops/raw/master/story-maps/images/yalemapslogin.png) 
6. Sign in with your NetID
7. Click past the new user setup screen.
8. Click on "Map" at the top of the screen to go to the [Web Map Viewer](https://yalemaps.maps.arcgis.com/home/webmap/viewer.html?useExisting=1)
_(Make sure you're using the "Classic Map Viewer", if offered the choice.)_

 ![screenshot](https://github.com/YaleDHLab/lab-workshops/raw/master/story-maps/images/newmap_no.png) 

3. Download this [spreadsheet of Pizza restuarants in New Haven](https://raw.githubusercontent.com/YaleDHLab/lab-workshops/master/story-maps/data/geocoded_pizza_locations.csv) to your computer. (Hint: **Choose File** -> **Save As...** to save the `geocoded_pizza_locations.csv` file somewhere you can easily find it, such as your Desktop or Downloads folder.)
4. Take a look at how the text is formatted in the [`geocoded_pizza_locations.csv`](https://raw.githubusercontent.com/YaleDHLab/lab-workshops/master/story-maps/data/geocoded_pizza_locations.csv) file. Is it easy or difficult to read? What do you think the first line of the file is doing?

![screenshot](https://github.com/YaleDHLab/lab-workshops/blob/master/story-maps/images/csv_raw.png?raw=true)

5. If you have Microsoft Excel, Numbers, or another spreadsheet on your computer, try opening the `geocoded_pizza_locations.csv` file by double-clicking it.  Is the file easier or more dificult to read?

![screenshot](https://github.com/YaleDHLab/lab-workshops/blob/master/story-maps/images/csv_excel.png?raw=true)

6.  Close the file in Excel, if you opened it.
7.  Make sure your **ArcGIS Map Viewer** web browser is visible from step 2, and find the `geocoded_pizza_locations.csv` file on your Desktop, in your Downloads folder, or wherever you saved it.  
8.  Drag the `geocoded_pizza_locations.csv` file into the map section of your ArcGIS Map Viewer web browser window.
9.  Voila! We have a map. You can experiment with the drawing style to see what makes sense for your data. For a spreadsheet of pizza locations around New Haven, a heat map could be good for highlighting clusters of pizza locations in the city. This could help someone looking for pizza zero in on a popular spot. Since for this particular Story Map we want to call attention to individual restaurants, we'll go with "Location (Single Symbol)"
10. Customize the map by clicking on "Options." Let's change our dots to pizzas! Click on "Symbols," then choose "People Places" from the dropdown menu. 

![screenshot](https://github.com/YaleDHLab/lab-workshops/blob/master/story-maps/images/symbol_pizza.png?raw=true)

Select the pizza icon and increase symbol size to 15. Click "Ok" twice and then "Done".

8. Our pop-ups still have a lot of unnecessary information. Let's change that by clicking on the ellipses and selecting "Configure Pop-Up."

![screenshot](https://github.com/YaleDHLab/lab-workshops/blob/master/story-maps/images/configure_popup.png?raw=true)

9. Next select "Configure Attributes" on the screen that appears. 

![screenshot](https://github.com/YaleDHLab/lab-workshops/blob/master/story-maps/images/configure_attributes.png?raw=true)

Unselect the **Display** box for everything except for `{Company_Name}` and `{"Neighborhood}`. Click "OK" twice

10. Save the map by clicking on the (small) floppy disk icon on the toolbar. 

![screenshot](https://github.com/YaleDHLab/lab-workshops/blob/master/story-maps/images/savemap.png?raw=true)

Add a "Title" of "New Haven Pizza Locations" so you can find this map later.

# Include this map of spreadsheet data points in a StoryMap

1. Go to http://storymaps.arcgis.com/
2. Click on "New Story" and "Start from Scratch" to create a blank StoryMap.
3. Fill in a basic title if you wish.
4. Click the plus symbol in a green circle and add a Map:

![screenshot](https://github.com/YaleDHLab/lab-workshops/blob/master/story-maps/images/create_newmap.png?raw=true)

5. Select the New Haven Pizza Locations map you created moments ago from the spreadsheet.


![screenshot](https://github.com/YaleDHLab/lab-workshops/blob/master/story-maps/images/add_map_arcgis.png?raw=true)

## Create Map Journal: New Haven Pizza Rivalries

1. Click on "Create Story"
2. Click "Map Journal" and select either "Side Panel" or "Floating Panel"
3. Give the Story Map a title and click on the right arrow
```
New Haven Pizza
```
4. For our main page, we'll go with a map. We can use the one we just created by searching for it in "My Organization." After selecting the map, click on "Custom configuration" to set the map extent. This is the region of the map that will appear when visitors first load the page
5. Click "Next" to add a description to introduce visitors to the site
```
Looking for pizza in New Haven? Here are some places to try! 
Click on a "pizza" for the name and neighborhood of the restaurant. 
This data was gathered from Reference USA. http://resource.referenceusa.com/
```
Congratulations! We have made our first page. Now let's add a second page.

6. Click "Add Section" and give it a title
```
Famous Pizza Wars
```
7. Select "Video" and "YouTube." Search for the link below and select the video that will provide additional context for New Haven pizza rivalries. Click "Fit" and "Next"
```
Link to video: https://youtu.be/aTRKEOdONhI
```
8. Add content on New Haven pizza wars
```
New Haven is famous for its long-standing pizza wars. Watch this video for a quick history of one 
of the oldest rivalries: Pepe's Pizzeria versus Sally's Apizza. Located in Wooster Square, the two 
restaurants are only one block away from each other. It's a New Haven tradition for people to line up 
outside the restaurants, waiting for their chance to get in.  
```
Two pages down! Let's add a third.

9. Let's dive deeper in the rivalries and create pages for Pepe's Pizzeria and Sally's Apizza, starting with Pepe's. Click "Add Section" and give it a title
```
Frank Pepe Pizzeria Napoletana
```
10. This time, select "Image" and "Link" to add a photo from the web
```
Link to image: https://upload.wikimedia.org/wikipedia/commons/a/aa/Frank_pepe_clam_pie.jpg
```
11. Add content on Pepe's
```
Known locally as "Pepe's," this pizzeria first opened in 1925. According to Wikipedia, 
"Pepe's originated the New Haven-style thin-crust apizza(closely related to Neapolitan-style 
Italian pizza) which he baked in a coal-fired brick oven. Originally, Frank Pepe only made two 
varieties of pizza: the "tomato pie" (tomatoes with grated pecorino romano cheese, garlic, oregano, 
and olive oil) and the other with the addition of anchovy.

The piece of land which Pepe's restaurant sat on was owned by the Boccamiello family. They later 
made Frank Pepe leave so that they could start their own pizzeria at the establishment, which they 
renamed The Spot. Pepe moved his restaurant to its current location next door to The Spot in 1936. 
The Pepe family later bought back The Spot from the Boccamiello family in 1981 and it now serves the 
same menu as the newer restaurant." Link: https://en.wikipedia.org/wiki/Frank_Pepe_Pizzeria_Napoletana
```
Now that we have a page on Pepe's, let's add Sally's.

12. Click "Add Section" and give it a title
```
Sally's Apizza
```
13. Select "Image," but this time, choose "Upload" to add a file from the computer. You can download the file [here](https://github.com/YaleDHLab/lab-workshops/blob/master/story-maps/images/sallys_apizza.jpg)

14. Add content on Sally's
```
Sally's Apizza first opened in 1938. According to Wikipedia: "The restaurant was purchased for 
$500 in 1938 by Filomena Pepe Consiglio, sister of Frank Pepe, who was the owner of Frank Pepe 
Pizzeria Napoletana, another Wooster Street pizza restaurant. Sal Consiglio, a son of Filomena, 
ran it until his death in May 1989. His wife Flo died in September 2012. Their children Richard 
and Robert still operate the restaurant.

Sally's serves New Haven-style thin-crust apizza, which is baked in coal-fired brick ovens. By 
default, a New Haven pizza is a "plain" pizza topped with only tomato sauce, garlic, and mozzarella
and Parmesan. Sally's is a small restaurant, and often, patrons must wait in line, sometimes for 
hours." Link: https://en.wikipedia.org/wiki/Sally%27s_Apizza
```
We now have a Story Map that celebrates one famous pizza rivalry in New Haven. 


## Next steps and additional tips

* [Getting Started Documentation](https://storymaps.arcgis.com/stories/cea22a609a1d4cccb8d54c650b595bc4)
 * [Sidecar Feature (most common interactive tool)](https://storymaps.arcgis.com/stories/82509aafc8ba435f8c1264122d299763)


* Find latitude and longitude:

1. Enter the name of your pizza place in [Google Maps](https://www.google.com/maps)
2. Right click on the location and select "What's Here?"![](https://github.com/YaleDHLab/lab-workshops/raw/master/story-maps/images/latlong_googlemaps.png) The box that appears will contain the latitude and longitude. 

2.5 Alternatively, if you look at the URL, you will find that the latitude and longitude have been there all along! ![](https://github.com/YaleDHLab/lab-workshops/raw/master/story-maps/images/url_googlemaps.png)
3. Add the latitude and longitude to corresponding columns in a spreadsheet 


