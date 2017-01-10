# Switching to Morph.io

Once you've [tested out the code in Execute Python Online](https://github.com/paulbradshaw/python_demo/blob/master/README.md) you can try it out in [Morph.io](https://morph.io/)

First, create an account on Morph.io

Then click on the menu in the upper right corner and select **create a new scraper**. (You will need a GitHub account too.)

Choose *Python* as the language. 

Once it's set up your page, you can find a link to the scraper code on the right hand side - it will be called *scraper.py*.

Clicking on that link will take you to your GitHub account (a bit disorientating I know - this is because Morph.io uses GitHub to store your code). 

That .py file will already have some basic Python scraping code in it. You can click on the edit button (the pencil icon) to start editing it.

## Editing your Python code

Leave the first line as it is:

`import scraperwiki`

But the rest can be deleted.

Add this line:

`record = {}`

After `print i['name']` add the following two lines:

`    record['idcode'] = i['id']`

`    record['fullname'] = i['name']`

`    scraperwiki.sqlite.save(['idcode'], record)`

(Don't forget the indents).

## Running your Python code in Morph.io

Now you can switch back to your Morph.io page for this scraper. (Use the back button to find it again if you need to)

Click **Run scraper**.

Depending how busy Morph.io is, this can run quickly or take a while. If it works you should see *Last run completed successfully ... ago.*

You can click *Download table (as CSV)* to get the data

You can click *Use the API* to query the data and generate a subset of it, if it's too large.

