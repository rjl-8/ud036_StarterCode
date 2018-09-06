# ud036_StarterCode
Source code for a Movie Trailer website.


# Udacity FEND Google Map Project

This code is intended to satisfy the requirements of the Neighborhood Map project in the Advanced Interactive Websites lesson of the Front End Web Developer nanodegree.

## Getting Started

Just copy the files to your local web root and browse to index.html

### Prerequisites

Should be self contained with the provided files

## Built With

* [Knockoutjs](http://knockoutjs.com/) - The web framework used
* [JQuery](http://jquery.com/) - general utility
* [Google Maps API](https://cloud.google.com/maps-platform/) - Used to manage maps and pull place related info for various locations
* [Wikipedia API](https://www.mediawiki.org/wiki/API:Query) - Used to pull wikipedia related info for various locations

## Authors

* **Ron Lewis** - *Initial work* - [rjl-8](https://github.com/rjl-8)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to Udacity for forcing me to learn all this cool stuff







# Project Overview

In this project you are given a web-based application that reads RSS feeds. The original developer of this application clearly saw the value in testing, they've already included [Jasmine](http://jasmine.github.io/) and even started writing their first test suite! Unfortunately, they decided to move on to start their own company and we're now left with an application with an incomplete test suite. That's where you come in.


## Why this Project?

Testing is an important part of the development process and many organizations practice a standard of development known as "test-driven development". This is when developers write tests first, before they ever start developing their application. All the tests initially fail and then they start writing application code to make these tests pass.

Whether you work in an organization that uses test-driven development or in an organization that uses tests to make sure future feature development doesn't break existing features, it's an important skill to have!


## What will I learn?

You will learn how to use Jasmine to write a number of tests against a pre-existing application. These will test the underlying business logic of the application as well as the event handling and DOM manipulation.


## How will this help my career?

* Writing effective tests requires analyzing multiple aspects of an application including the HTML, CSS and JavaScript - an extremely important skill when changing teams or joining a new company.
* Good tests give you the ability to quickly analyze whether new code breaks an existing feature within your codebase, without having to manually test all of the functionality.


# How will I complete this project?

Review the Feed Reader Testing [Project Rubric](https://review.udacity.com/#!/projects/3442558598/rubric)

1. Take the JavaScript Testing [course](https://www.udacity.com/course/ud549)
2. Download the [required project assets](http://github.com/udacity/frontend-nanodegree-feedreader).
3. Review the functionality of the application within your browser.
4. Explore the application's HTML (**./index.html**), CSS (**./css/style.css**) and JavaScript (**./js/app.js**) to gain an understanding of how it works.
5. Explore the Jasmine spec file in **./jasmine/spec/feedreader.js** and review the [Jasmine documentation](http://jasmine.github.io).
6. Edit the `allFeeds` variable in **./js/app.js** to make the provided test fail and see how Jasmine visualizes this failure in your application.
7. Return the `allFeeds` variable to a passing state.
8. Write a test that loops through each feed in the `allFeeds` object and ensures it has a URL defined and that the URL is not empty.
9. Write a test that loops through each feed in the `allFeeds` object and ensures it has a name defined and that the name is not empty.
10. Write a new test suite named `"The menu"`.
11. Write a test that ensures the menu element is hidden by default. You'll have to analyze the HTML and the CSS to determine how we're performing the hiding/showing of the menu element.
12. Write a test that ensures the menu changes visibility when the menu icon is clicked. This test should have two expectations: does the menu display when clicked and does it hide when clicked again.
13. Write a test suite named `"Initial Entries"`.
14. Write a test that ensures when the `loadFeed` function is called and completes its work, there is at least a single `.entry` element within the `.feed` container.
15. Write a test suite named `"New Feed Selection"`.
16. Write a test that ensures when a new feed is loaded by the `loadFeed` function that the content actually changes.
17. No test should be dependent on the results of another.
18. Callbacks should be used to ensure that feeds are loaded before they are tested.
19. Implement error handling for undefined variables and out-of-bound array access.
20. When complete - all of your tests should pass. 
21. Write a README file detailing all steps required to successfully run the application. If you have added additional tests (for Udacious Test Coverage),  provide documentation for what these future features are and what the tests are checking for.

# How to install and run this project

1. navigate to the appropriate repository in github.com and clone the project
2. the site is self contained and works out of the box so all you need to do is copy the files to a dedicated folder within your web server.
3. browse to index.html in a browser.  The site is the content at the top of the page and the test results are at the bottom of the page just past the "Jasmine" logo.

# How I completed this project?

1. all modifications occurred within the feedreader.js file
2. to check that each feed has a url defined, i wrote a simple loop through the allFeeds array, running an expect on the url property's existence and that it had a length greater than 0
3. to check that each feed has a name defined, i basically copied the test from 2 above but this time referencing the name property with the allFeeds objects
4. to check that the menu starts out hidden, after looking over the css, i checked that the body has a className of 'menu-hidden'
5. to check that the menu becomes visible when clicked, i triggered a click event and then checked the className of the body tag again. As an extra validation, i triggered another click event and made sure the className had toggled back.
6. to test that loadFeed loaded at least one entry, i executed loadFeed(0) asynchronously using the beforeEach functionality within Jasmine.  Then i validated that the number of article tags in the document was > 0.
7. to test that the loadFeed function would load a different set of entries for different feeds, i initiated loadFeed(0) as in item 6 above.  However, in the callback function for this call, after capturing the results of the call, I initiated loadFeed(1) and then captured the results for that call.  Then I compared the two result sets, in addition to validating that the result set for loadFeed(1) had some entries.




## Website Performance Optimization portfolio project

Your challenge, if you wish to accept it (and we sure hope you will), is to optimize this online portfolio for speed! In particular, optimize the critical rendering path and make this page render as quickly as possible by applying the techniques you've picked up in the [Critical Rendering Path course](https://www.udacity.com/course/ud884).

To get started, check out the repository and inspect the code.

### Getting started

#### Part 1: Optimize PageSpeed Insights score for index.html

Some useful tips to help you get started:

1. Check out the repository
1. To inspect the site on your phone, you can run a local server

  ```bash
  $> cd /path/to/your-project-folder
  $> python -m SimpleHTTPServer 8080
  ```

1. Open a browser and visit localhost:8080
1. Download and install [ngrok](https://ngrok.com/) to the top-level of your project directory to make your local server accessible remotely.

  ``` bash
  $> cd /path/to/your-project-folder
  $> ./ngrok http 8080
  ```

1. Copy the public URL ngrok gives you and try running it through PageSpeed Insights! Optional: [More on integrating ngrok, Grunt and PageSpeed.](http://www.jamescryer.com/2014/06/12/grunt-pagespeed-and-ngrok-locally-testing/)

Profile, optimize, measure... and then lather, rinse, and repeat. Good luck!

Changes made to improve performance
1. Moved the contents of style.css and print.css files to inline style tags
2. Refactored the 2 of the least efficient images sizewise (img/profilepic.jpg and views/images/pizzeria.jpg) to compress their size.  I created new files (*.min.jpg) so I also changed the references to the image files in the index.html and the pizza.html files respectively.
3. Made the call to google-analytics javascript library asynchronous
4. Minified the performance.js file to performance.min.js and changed the references to point to the new filename

#### Part 2: Optimize Frames per Second in pizza.html

To optimize views/pizza.html, you will need to modify views/js/main.js until your frames per second rate is 60 fps or higher. You will find instructive comments in main.js. 

You might find the FPS Counter/HUD Display useful in Chrome developer tools described here: [Chrome Dev Tools tips-and-tricks](https://developer.chrome.com/devtools/docs/tips-and-tricks).

### Optimization Tips and Tricks
* [Optimizing Performance](https://developers.google.com/web/fundamentals/performance/ "web performance")
* [Analyzing the Critical Rendering Path](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/analyzing-crp.html "analyzing crp")
* [Optimizing the Critical Rendering Path](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/optimizing-critical-rendering-path.html "optimize the crp!")
* [Avoiding Rendering Blocking CSS](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/render-blocking-css.html "render blocking css")
* [Optimizing JavaScript](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/adding-interactivity-with-javascript.html "javascript")
* [Measuring with Navigation Timing](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/measure-crp.html "nav timing api"). We didn't cover the Navigation Timing API in the first two lessons but it's an incredibly useful tool for automated page profiling. I highly recommend reading.
* <a href="https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/eliminate-downloads.html">The fewer the downloads, the better</a>
* <a href="https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/optimize-encoding-and-transfer.html">Reduce the size of text</a>
* <a href="https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/image-optimization.html">Optimize images</a>
* <a href="https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching.html">HTTP caching</a>

Changes made to improve performance
1. Scrolling: in updatePositions function, I moved the scrollTop calculation out of the loop through all the floating pizza images
2. Pizza size toggle: in changePizzaSizes function:
  * cleaned up multiple calls to querySelectorAll in loop through all the pizzas
  * dropped the use of the determineDx function and instead stole the sizeSwitcher function from determineDX to return a fixed percent to avoid all the unnecessary calculation the provided function used.

### Customization with Bootstrap
The portfolio was built on Twitter's <a href="http://getbootstrap.com/">Bootstrap</a> framework. All custom styles are in `dist/css/portfolio.css` in the portfolio repo.

* <a href="http://getbootstrap.com/css/">Bootstrap's CSS Classes</a>
* <a href="http://getbootstrap.com/components/">Bootstrap's Components</a>