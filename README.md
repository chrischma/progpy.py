# progpy.py
progpy is an easy to use progress bar for the macOS terminal. 

<h2> Setup </h2>
No setup requiered, a simple copy paste will do. 

<h2> Basic Usage </h2>

<p> The <code> progress_bar() </code> function requires two parameters: <code> split</code> and <code> total</code>. 
for example, if 2 of 10 tasks are done, <code> progress_bar(2,10)</code> will create a progressbar where 20% blocks are black. </p>

<h2> Resizing </h2>
<p> The size of the progress set in the <code>length</code>variable. it can be set to short, medium, maximum or to a custom number. progpy.py auto-sizes the progressbar by reading out the windows size of the currently opened terminal window. </p>

<h2> Auto-Print </h2>
By default, progpy.py automatically prints out the progress bar to the macOS terminal. if you set <code>auto_print</code> to <code>false</code>, progpy will instead just return the final string for further use.

<h2> Enjoy! </h2>
