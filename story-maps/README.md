# Story Maps

Story Maps is a free, open-source platform for combining texts, images, and videos alongside maps (though technically, maps aren't required!). In this workshop, we'll discuss the pros and cons of the various templates, offering tips along the way for how you might collect, analyze, and visualize the data that will serve as the basis for your Story Map.

## Story Maps templates

Story Maps offers a number of templates that you can choose from. Some will be better if you have a lot of textual data, whereas others work especially well if you have geographic data or high-quality visual content. Each template also provides a different user experience. Is chronology important to your argument? If yes, you might choose a template that requires visitors to scroll through your Story Map instead of one that gives visitors the flexibility to jump around to different sections. 

### Spy Glass template

[The World in 1812 and 2013](https://story.maps.arcgis.com/apps/StorytellingSwipe/index.html?appid=b8ece5952db443858442f122984602ba&webmap=8ea34ba9a4f843e08a468595d8d91188#) - comparison of modern and historic maps

### Map Journal template

[Aeneid](http://www.arcgis.com/apps/MapJournal/index.html?appid=33be151cbe1942d99a300da085884729) - great example for how you can move through a timeline that's linked to a map - you could easily replace any of the photos in the left-hand column with videos, if desired

### Cascade template

[The Uprooted](http://storymaps.esri.com/stories/2016/the-uprooted/index.html) - demonstrates the range of media your site might include

[Restoring Old Havana](http://storymaps.esri.com/stories/2017/havana-restoration/index.html?language=english) - shows that you could have a Story Map set up in different languages   

### Crowdsourcing template

[Tropical Storm Harvey](https://napsg.maps.arcgis.com/apps/StoryMapCrowdsource/index.html?appid=b6ef838e4d26489e8f62102639dc3d91) - example of how you can crowdsource photographs in real time and for crisis relief efforts

[1Frame4Nature](https://conservationphotographers.org/1f4n/) - example of how you can embed a Story Map within your own site

## Gathering content for Story Map 

For this workshop, we'll create a Story Map using the Map Journal template to showcase New Haven pizza rivalries. Gathering content is the hardest part of creating a Story Map. For the purposes of this tutorial, we'll provide sample data and content. For after the workshop, here are a few sites you might try for content. 

### To find photos 

1. Go to [Google images](https://images.google.com/)
2. Search for a related photo of your choosing
3. Under "Tools," click "Labeled for Reuse" (more on this later in the workshop) ![](https://github.com/YaleDHLab/lab-workshops/raw/master/story-maps/images/google_images_reuse.png)
4. Right-click on an image in the results and click "Copy Image Location" or "Save Image As," depending on if you want to link out to or upload the image

### To collect data

There are a lot of open data repositories online. Here are a couple places you might check out:

[Connecticut Open Data](https://data.ct.gov/) - many states have complementary sites

[Reference USA](http://search.library.yale.edu/databases/12540702) - good for finding business data

### To map geographic data

1. Log in to [ArcGIS.com](http://www.arcgis.com/home/index.html) (see instructions in "Sign in to Story Maps" section below)
2. Go to "Map" 
3. Drag a .csv spreadsheet that has a "latitude" and "longitude" column over the map. Voila! We have a map. You can experiment with the drawing style to see what makes sense for your data. For a spreadsheet of pizza locations around New Haven, a heat map could be good for highlighting clusters of pizza locations in the city. This could help someone looking for pizza zero in on a popular spot. Since for this particular Story Map we want to call attention to individual restaurants, we'll go with "Location (Single Symbol)"
4. Customize the map by clicking on "Options." Let's change our dots to pizzas! Click on "Symbols," then choose "People Places" from the dropdown menu. Select the pizza icon and increase symbol size to 15. Click "Ok" twice and then "Done" 
5. Our pop-ups still have a lot of unnecessary information. Let's change that by clicking on the ellipses and selecting "Configure Pop-Up." Next select "Configure Attributes" on the screen that appears. Unselect the display box for everything except for "Company_Name" and "Neighborhood." Click "Ok" twice
6. Save the map. Add a "Title," "Tags," and "Summary"


## Sign in to Story Maps

Anyone can sign up for a free account with Esri. For this workshop, we encourage you to sign in with your Yale NetID, which will give you access to additional content that's been created and shared by members of the Yale community. To sign in, follow the steps below.

1. Go to http://storymaps.arcgis.com/en/
2. Click "Sign In" in the upper right-hand corner
3. Click "Sign in with Enterprise Account"
4. Type "yalemaps" into the address as indicated ![screenshot](https://github.com/YaleDHLab/lab-workshops/raw/master/story-maps/images/yale_login.png) and press "Continue"
5. Sign in with your NetID
6. Click on "My Stories" to create your first story!

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

## Experiment with your own Story Map

With the remaining time in the workshop, expand on New Haven Pizza Rivalries or create a new Story Map from scratch. 


## Next steps and additional tips

* Want to customize your Story Map beyond what's immediately available? Google "Story Map \[insert template name here] GitHub," and you'll be taken to the underlying code.

* Experiment with embedding Story Maps within one another. For example, you could embed an existing Map Tour inside a Map Journal. Follow this [Esri guide](https://blogs.esri.com/esri/arcgis/2016/07/15/embed-story-map-in-story-map/) to try it out.

* Find latitude and longitude:

1. Enter the name of your pizza place in [Google Maps](https://www.google.com/maps)
2. Right click on the location and select "What's Here?"![](https://github.com/YaleDHLab/lab-workshops/raw/master/story-maps/images/latlong_googlemaps.png) The box that appears will contain the latitude and longitude. 

2.5 Alternatively, if you look at the URL, you will find that the latitude and longitude have been there all along! ![](https://github.com/YaleDHLab/lab-workshops/raw/master/story-maps/images/url_googlemaps.png)
3. Add the latitude and longitude to corresponding columns in a spreadsheet 

