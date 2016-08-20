# PunjabiLexicon-
To scrap Punjabi data from Digital dictionaries of South Asia 

1)Install Beautiful Soup by reading the following 
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

2)Run the python prograwm punjabi.py 

3)You will get the scrapped data of the website :) 

***********************************************
A more detailed step-by-step process 
Install beautiful soup for your Distro .
Make sure you have python in your system 


1 : Run the punjabipython.py program 

2: We will get a file wordlist.txt 

3.Removing dulpicates : 

Help from http://stackoverflow.com/questions/38802396/deleting-a-row-which-is-substring-of-the-subsequent-row

3.1) In find and replace use tick the match using regular expressions
In the find tab       ^(.+)[\r\n]+\1
In the replace tab    \1

3.2)Replace all occurence of 
Next page


Back to the Search Page 
  |  
Back to the DDSA Page

with none so that they get removed

4)Merge all the contents for a word  to a single line 
Thanks to :http://stackoverflow.com/questions/38803431/merging-lines-with-a-given-condition/



In the find tab        \r?\n(?!\r?\n)
In the Replace tab     " "    <<Remember .. there is a space>>

5)To remove any blank spaces in the beginning of the line , use 
^\s*

(OR)

5)To remove blank space and replace it by ~ , use 
^\s*
~

6)Now we have all the words . Just in case we need to add a place holder 
In the find tab ^(\S+)\s
In the Replace tab \1~




7)Delete all blank lines if present 

Thanks to :http://stackoverflow.com/questions/38804320/inserting-a-special-character-in-place-of-first-white-space

Using :

In the find tab ^[\n\r]+
In the Replace tab <<Blank>>

