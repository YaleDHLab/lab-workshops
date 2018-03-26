# Building a Site with GitHub Pages

## Getting Started: Terminology

**Git** 

Git is version control software that's used for tracking changes in files. 

**GitHub** 

GitHub is a website for hosting code and project documentation, among things.  

**Markdown**  

Markdown provides a plaintext way to create styled pages on the web. 

## Create a site with GitHub Pages

**1. Sign up for a GitHub account**

To create an account, visit [GitHub](https://github.com/), click 'Sign up,' and follow the steps. For the type of plan, select the free one. If you find yourself using GitHub a lot in the future for projects, you might want to upgrade to a paid account, which will provide you with the option to have private repositories for projects that you may not be ready to share.

Check your email to finish creating an account - you have to verify the email address you provided when registering.

**2. Create a new repository on GitHub**    

While on GitHub, click on the plus sign in the top right corner, then select "New repository." 

Name this new repository
```
hello-world
```

Provide a description for what will be in this repository (helpful for you and other GitHub users who may want to use your code)
```
Demo for GitHub Pages
```

Click on 'Initialize this repository with a README.'

Click 'Create repository.'

**3. Create index.md file**

From within your new repository, click on 'Create new file' on the right. 

For the file name at the top, type
```
index.md
```

Add some content. For example:  
```
# Add a title for your site  
Include a sentence that describes what will be on your site.
## Indicate another section
*Emphasize something important about the site*  
**Really mean it**
```

Scroll down to the bottom and for 'Commit new file,' add a message
```
Create index.md
```

Click the green 'Commit new file' button. (You should have 'Commit directly to the master branch' selected.)

**4. Ask GitHub Pages to look for the Master Branch**

From within your repository, click on 'Settings' on the right.

Scroll down to 'GitHub Pages' toward the bottom.

Click the dropdown that says 'None' and select 'Master branch.'

Click 'Save.' 

**5. Visit your new site!**

Wait a few seconds after the step above, and then click on the link under 'GitHub Pages.' (If you see a 404 page, wait a few more seconds, and then click 'refresh' on your browser.) 

The URL for your website should look like
```
https://YOUR-USERNAME.github.io/REPOSITORY-NAME/
```

## Recommended Resources
* [Sample GitHub Pages Setup](https://github.com/cdworkshops/GitHub-pages)

* ["Building a Static Website with Jeykll and GitHub Pages"](https://programminghistorian.org/lessons/building-static-sites-with-jekyll-github-pages) *Programming Historian* tutorial by Amanda Visconti

* [Git Intro](https://data-lessons.github.io/library-git/) Library Carpentry tutorial

* [Introduction to Git for Data Science](https://www.datacamp.com/courses/introduction-to-git-for-data-science) by DataCamp

* [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) by GitHub

* [Markdown Quick Reference](https://en.support.wordpress.com/markdown-quick-reference/) by WordPress

* [Markdown Live Preview](http://markdownlivepreview.com/)