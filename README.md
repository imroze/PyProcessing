# PyProcessing
PyProcessing is a PyGame wrapper for easily creating graphical and interactive programs in Python in a simple format that's very similar to Processing. 

The PyProcessing class implements the program flow and event handling similar to Processing programs through PyGame code and provides implementations of many common Processing functions for things like creating different shapes and displaying images and text.

Python programs similar to Processing can be developed by creating a subclass of PyProcessing class and overriding these methods: setup(), draw(), mousePressed() and keyPressed().

The example.py code demonstrates an example of creating programs using PyProcessing. In the example program, circles are created upon clicking at any location on window and all the circles chase the mouse pointer. Different Processing function implementations are being used in it. It can also be used as boilerplate for creating the programs.

A Python implementation of the common PVector class in Processing is also included in the code. That is based on small modifications to following code by Alexandre B A Villares: https://gist.github.com/villares/5c476cbc44c1153fed159eae36fc016b

### Usage
1. Install pygame using "pip install pygame"
2. Clone this repository. 
3. Run example.py script in repo, using "python example.py"