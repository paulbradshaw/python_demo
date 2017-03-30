# A brief introduction to Execute Python Online

The [Execute Python Online website](https://www.tutorialspoint.com/execute_python_online.php) allows you to use Python without creating an account or logging in. Start there (for now)

The website screen is split into 3 sections:

* The upper left corner shows the file directory. Ignore this: you won't need it.
* The upper right corner is where you write your code. Above it are buttons to 'execute' that code, etc.
* The bottom half of the screen shows you what *output* is generated when you execute the code above.

The code window already has two lines of code:

```python
# Hello World program in Python
print "Hello World!\n"
```

The first line is a *comment*. Comments start with a hash symbol (`#`) and do not do anything, apart from describe what comes after. They are useful for explaining what the code is doing, both for others and for yourself when you return to it later.

The second line is a **print** command. The word `print` tells Python to *display* anything that comes after it. In this case, a **string** of text: `"Hello World!\n"`

If you click execute, those two lines of code will run, and that string of text displayed in the output window below.

## Adding our own code

We're going to adapt some code that we can use to pull in some data from a URL. 

You can [find the code in full here](https://github.com/paulbradshaw/python_demo/blob/master/main.py). I'm going to explain it line by line below.

Most coding is done by finding some useful code and adapting it, and this example is no exception. 

I've googled "python read json files from url" and come to [this page on StackOverflow](https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script). I'm going to adapt the first few lines of that and explain them along the way:

```python
import urllib, json
```

This first line uses the `import` command to bring two **libraries** into our code. Libraries are often used in programming as a way to use pieces of code that other people have written and helpfully shared with others. 

The library `urllib` has a whole bunch of **functions** that can be used to handle URLs. And the `json` library has lots of functions that make dealing with JSON (a data format) easier.

The next line looks like this at StackOverflow: `url = "http://maps.googleapis.com/maps/api/geocode/json?address=google"`

Try copying that URL (without the quotation marks) and putting it into a browser like Chrome or Firefox. You will see that it returns a small amount of JSON code that includes `"status" : "ZERO_RESULTS"`

We're going to *adapt* that line and change the URL to one that we know does contain some JSON data:

```python
url = "https://data.police.uk/api/forces"
```

The next line opens the URL and puts the contents of that webpage (the JSON) into a **variable** called `response`:

```python
response = urllib.urlopen(url)
```

Then the next line takes that `response` variable, uses something called `.read()` on it (reading the webpage), and then uses the results of *that* as the ingredient for `json.loads`, loading it (as JSON) into the new variable `data`. 

```python
data = json.loads(response.read())
```

Now to print what we have put into that new variable `data`:

```python
print data
```

This just shows us all the JSON. Now I'm going to add some more lines to go through that.

The JSON data is a **list**. The following two lines **loop** through that list and display each item in turn:

```python
for i in data:
    print i
```

Note that the first line ends in a **colon** and the second line is indented. That indentation indicates that the second line is related to the one above it. This is important for any loop. It means for each item in that list (which we've called `i`, but could call almost anything), print the item (`i`). 

Each line looks like this: `{"id":"warwickshire","name":"Warwickshire Police"}`

Notice that `"id"` and `"name"` always stay the same (these are the **keys**), but the *value* of those changes.

We can print more specifically by using square brackets to identify the key in each item like so:

```python
print i['name']
```

And we can test things by using **operators** like so:

```python
if i['id'] == 'wiltshire':
        print 'THIS IS WILTSHIRE2'
```

Note that the **if** line also ends with a colon, and the line underneath (which only executes *if* the condition is met, or TRUE) is indented again. Because the if line itself is already indented, that next line is indented twice.

The operator in this case is `==`. Others include `>` (greater than, for numbers), `<` (less than) and `!=` (does not equal). 

You can also look for text inside a string by using `in` like so:

```python
    if 'wilt' in i['id']:
        print 'IT CONTAINS WILT'
```

[The next step - storing data using Morph.io - can be found here](https://github.com/paulbradshaw/python_demo/blob/master/morphio.md)
