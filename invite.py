#! /usr/bin/env python 

from pyh import *

page = PyH("invite page for group leader")
page << h1("invite your friends!") 
form = form(action="begin.py", method="push")
form << input(type="text", name="nickname")
form << input(type="submit", value="submit")
page << form
page.printOut()

