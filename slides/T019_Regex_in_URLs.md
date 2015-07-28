# Regex in URL's

Regular Expressions (Regex) are a handy way to search for matching patterns in string, In our case search for patterns within url's. Some of the commonly used regex characters; 
* '^' for beginning of the text
* '$' for end of text
* '\d' for a digit
* '+' to indicate that the previous item should be repeated at least once
* () to capture part of the pattern
* / tells django that another / character should follow

Example: Explain each of the below...
```
urlpatterns = [ 
- url(r'^album/([0-9]{4})/$', views.album),
- url(r'^songs/$', views.songs),
- url(r'^album/',include('music.album.urls',namespace="album")),
- Example of URL Reversing
]
```
