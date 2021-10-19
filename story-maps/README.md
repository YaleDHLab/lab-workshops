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
4. Type "yalemaps" into the address as indicated and press "Continue":<br><img src="https://github.com/YaleDHLab/lab-workshops/raw/master/story-maps/images/yalemapslogin.png" width="461">
5. Sign in with your NetID
6. Click past the new user setup screen.
7. Click on "Map" at the top of the screen to go to the [Web Map Viewer](https://yalemaps.maps.arcgis.com/home/webmap/viewer.html) _Make sure you're using the "Classic Map Viewer", if offered the choice._ <br><img src="https://github.com/YaleDHLab/lab-workshops/raw/master/story-maps/images/newmap_no.png" width="627">
8. Download this [spreadsheet of Pizza restuarants in New Haven](https://raw.githubusercontent.com/YaleDHLab/lab-workshops/master/story-maps/data/geocoded_pizza_locations.csv) to your computer. (Hint: **Choose File** -> **Save As...** to save the `geocoded_pizza_locations.csv` file somewhere you can easily find it, such as your Desktop or Downloads folder.)
9. Take a look at how the text is formatted in the [`geocoded_pizza_locations.csv`](https://raw.githubusercontent.com/YaleDHLab/lab-workshops/master/story-maps/data/geocoded_pizza_locations.csv) file. What do you think the first line of the file is doing?<br><img src="https://github.com/YaleDHLab/lab-workshops/blob/master/story-maps/images/csv_raw.png?raw=true" width="489">
10. If you have Microsoft Excel, Numbers, or another spreadsheet on your computer, try opening the `geocoded_pizza_locations.csv` file by double-clicking it.<br>  <img src="https://github.com/YaleDHLab/lab-workshops/blob/master/story-maps/images/csv_excel.png?raw=true" width="800">
11.  Close the file in Excel, if you opened it.
12.  Make sure your **ArcGIS Map Viewer** web browser is visible from step 2, and find the `geocoded_pizza_locations.csv` file on your Desktop, in your Downloads folder, or wherever you saved it.  
13.  Drag the `geocoded_pizza_locations.csv` file into the map section of your ArcGIS Map Viewer web browser window.
14.  Voila! We have a map. You can experiment with the drawing style to see what makes sense for your data. For a spreadsheet of pizza locations around New Haven, a heat map could be good for highlighting clusters of pizza locations in the city. This could help someone looking for pizza zero in on a popular spot. Since for this particular Story Map we want to call attention to individual restaurants, we'll go with "Location (Single Symbol)"
15. Customize the map by clicking on "Options." Let's change our dots to pizzas! Click on "Symbols," then choose "People Places" from the dropdown menu.<br><img src="https://github.com/YaleDHLab/lab-workshops/blob/master/story-maps/images/symbol_pizza.png?raw=true" width="264"><br>Select the pizza icon and increase symbol size to 15. Click "Ok" twice and then "Done".
16. Our pop-ups still have a lot of unnecessary information. Let's change that by clicking on the ellipses and selecting "Configure Pop-Up."<br><img src="https://github.com/YaleDHLab/lab-workshops/blob/master/story-maps/images/configure_popup.png?raw=true" width="342">
17. Next select "Configure Attributes" on the screen that appears. <br><img src="https://github.com/YaleDHLab/lab-workshops/blob/master/story-maps/images/configure_attributes.png?raw=true" width="243"><br>Unselect the **Display** box for everything except for `{Company_Name}` and `{"Neighborhood}`. Click "OK" twice.
18. Save the map by clicking on the (small) floppy disk icon on the toolbar.<br><img src="https://github.com/YaleDHLab/lab-workshops/blob/master/story-maps/images/savemap.png?raw=true" width="570"><br>Add a "Title" of "New Haven Pizza Locations" so you can find this map later.

# Include this map of spreadsheet data points in a StoryMap

1. Go to http://storymaps.arcgis.com/
2. Click on "New Story" and "Start from Scratch" to create a blank StoryMap.
3. Fill in a basic title if you wish.
4. Click the plus symbol in a green circle and add a Map: <br><img src="https://github.com/YaleDHLab/lab-workshops/blob/master/story-maps/images/create_newmap.png?raw=true" width="787">
5. Select the New Haven Pizza Locations map you created moments ago from the spreadsheet.<br>
<img src="https://github.com/YaleDHLab/lab-workshops/blob/master/story-maps/images/add_map_arcgis.png?raw=true" width="653">


## Next steps and additional tips

* [Getting Started Documentation](https://storymaps.arcgis.com/stories/cea22a609a1d4cccb8d54c650b595bc4)
 * [Sidecar Feature (most common interactive tool)](https://storymaps.arcgis.com/stories/82509aafc8ba435f8c1264122d299763)


* Find latitude and longitude:

1. Enter the name of your pizza place in [Google Maps](https://www.google.com/maps)
2. Right click on the location and select "What's Here?"![](https://github.com/YaleDHLab/lab-workshops/raw/master/story-maps/images/latlong_googlemaps.png) The box that appears will contain the latitude and longitude. 

2.5 Alternatively, if you look at the URL, you will find that the latitude and longitude have been there all along! ![](https://github.com/YaleDHLab/lab-workshops/raw/master/story-maps/images/url_googlemaps.png)
3. Add the latitude and longitude to corresponding columns in a spreadsheet 


