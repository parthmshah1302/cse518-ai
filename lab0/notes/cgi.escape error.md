### Error
![](media/cgiEscapeError.png)  
### Solution 
* add `import html` below `import cgi` and replace `cgi.escape()` by `html.escape()`