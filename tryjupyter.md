# Try Jupyter

[Jupyter](http://jupyter.org/) is a tool for running Python scripts and creating Python notebooks, which combine working code with commentary and notes (click on any of the `ipynb` files to see one).

The [Try Jupyter!](https://try.jupyter.org/) option at try.jupyter.org is another online environment that creates a temporary way "to try out a recent development version of the IPython/Jupyter notebook."

There is a big warning, however: 

> "**Don't rely on this server for anything you want to last - your server will be *deleted after 10 minutes of inactivity*.**"

One nice feature of Try Jupyter is that it allows you to work in a Terminal too. To launch one, click on **New** in the right corner, and select **Terminal**. This will open up a big black box where you can type commands just like on a computer's Terminal. The first command to try is: 

`ls`

This will list the files and folders in the current directory - and you should see the same list that you saw on the main try.jupyter.org page. [For more on command line see my GitHub repo](https://github.com/paulbradshaw/commandline)

You can create Python files in Try Python in the same way by clicking on **New** and selecting the type of Python file you want to create (2 and 3 are different versions of the language).

You can then run that file in Terminal by typing `Python` followed by the name of the file including `.py`.

Note that some libraries won't import properly in your Python file, including common scraping libraries like `lxml.html` and `scraperwiki`. [To add those](http://support.datascientistworkbench.com/knowledgebase/articles/600735-how-do-i-install-additional-libraries-in-my-notebo) you need to go into Terminal and run `pip install` followed by the name of the library.
