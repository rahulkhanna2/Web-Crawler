page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=') #finds the starting of the link
start_quote = page.find('"' , start_link)#find's the starting of the " before url but includes " in it
end_quote = page.find('"' , start_quote + 1) #find's the end of the " after url but does not includes " in it
url = page[start_quote+1 : end_quote] #Gives the url of the site found. +1 just skips the " included in the start_quote.

print url
