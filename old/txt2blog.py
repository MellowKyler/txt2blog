import re

userInput = input("File name: ")
inputFile = open(userInput)

outputFile = open('output.html', "w")

line_no = 0
for line in inputFile:
	if line.startswith("\n"):
		continue
	line_no = line_no + 1
	if line_no == 1:
		title = line.strip()
		line = '<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>' + title + '</title>\n<link rel="icon" type="image/x-icon" href="/images/favicon.png">\n<link href="/styles.css" rel="stylesheet" type="text/css" media="all">\n<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n<link rel="alternate" type="application/rss+xml" href="/feed.xml" title="RSS">\n</head>\n<body>\n<nav class="nav-bar">\n<div class="nav-menu">\n<input type="checkbox" id="check">\n<label for="check" class="checkbtn"><i class="fa fa-bars"></i></label>\n<ul>\n<li><a href="/">Home</a></li>\n<li><a href="/profile/">Profile</a></li>\n<li><a href="/politics/">Politics</a></li>\n<li><a href="/school/">School</a></li>\n<li><a href="/gaming/">Gaming</a></li>\n<li><a href="/blog/">Blog</a></li>\n</ul>\n</div>\n</nav>\n\n<main>\n\n<br>\n\n<h2 class="blog-title">' + title + '</h2>\n\n<div class="blog-header">\n'
		outputFile.write(line)
	elif line_no == 2:
		date = line.strip()
	elif line_no == 3:
		start_time = line.strip()
		line = '<p class="blog-dates">Started ' + date + ' ' + start_time + '</p>\n'
		outputFile.write(line)
	elif line_no == 4:
		end_time = line.strip()
		line = '<p class="blog-dates">Finished ' + date + ' ' + end_time + '</p>\n<p class="blog-dates">Posted 01/01/2023 00:00</p>\n</div>\n\n<hr>\n\n'
		outputFile.write(line)
	elif line.startswith('!quote '):
		line = line.rstrip('\n')
		fn_str = str(re.findall('\[[\0-9*]\]', line))
		if fn_str is True:
			fn_search = (re.findall('[0-9*]', fn_str))
			fn_no = fn_search[0]
			line = '<div class="blog-quote" id="fnl-' + fn_no + '">\n<p>' + line + '</p>' + '\n' + '</div>' + '\n\n'
			for i in fn_search:
				fn_no = fn_search[i]
				fn_flag = '[' + fn_no + ']'
				line = line.replace(fn_flag, '<a href=#fn-' + fn_no + '">' + fn_flag + '</a>')
		else:
			line = '<div class="blog-quote">\n<p>' + line + '</p>' + '\n'  + '</div>' + '\n\n'
		line = line.replace(' !newline ', '\n')
		line = line.replace('!quote ', '')
		outputFile.write(line)
	elif line.startswith('!twitter '):
		line = line.rstrip('\n')
		fn_str = str(re.findall('\[[\0-9*]\]', line))
		if fn_str is True:
			fn_search = (re.findall('[0-9*]', fn_str))
			fn_no = fn_search[0]
			line = '<div class="blog-twitter" id="fnl-' + fn_no + '">\n<p>' + line + '</p>' + '\n' + '</div>' + '\n\n'
			for i in fn_search:
				fn_no = fn_search[i]
				fn_flag = '[' + fn_no + ']'
				line = line.replace(fn_flag, '<a href=#fn-' + fn_no + '">' + fn_flag + '</a>')
		else:
			line = '<div class="blog-twitter">\n<p>' + line + '</p>' + '\n'  + '</div>' + '\n\n'
		line = line.replace(' !newline ', '\n')
		line = line.replace('!twitter ', '')
		outputFile.write(line)
	elif line.startswith("["):
		#footnotes
		fn_no_str = (re.findall('^\[[\0-9*]\]', line))
		fn_str = str(re.findall('^\[[\0-9*]\]', line))
		fn_search = (re.findall('[0-9*]', fn_str))
		fn_no = fn_search[0]
		if fn_no == '1':
			line = line.replace('[1] ', '')
			line = '<br>\n\n<div class="blog-footnotes">\n<h3 class="h-hr">Footnotes</h3>\n<p id="fn-1"><a href="#fnl-1">[1]</a> ' + line + '</p>' + '\n'
		else:
			#line = line.replace('[' + str(line_no) + ']', '')
			line = line.replace(fn_no_str[0], '')
			line = '<p id="fn-' + fn_no + '"><a href="#fnl-' + fn_no + '">[' + fn_no + ']</a>' + line + '</p>\n'
		outputFile.write(line)
	else:
		line = line.rstrip('\n')
		line = '<p class="p-indent">' + line + '</p>' + '\n\n'
		fn_str = str(re.findall('\[[\0-9*]\]', line))
		if fn_str is True:
			fn_search = (re.findall('[0-9*]', fn_str))
			for i in fn_search:
				fn_no = fn_search[i]
				fn_flag = '[' + fn_no + ']'
				line = line.replace(fn_flag, '<a id="fnl-' + fn_no + '" href=#fn-' + fn_no + '">' + fn_flag + '</a>')
		outputFile.write(line)
							 
outputFile.write('</div>\n\n<div class="top-button">\n<a href="https://kyler.neocities.org/blog" class="blog-home">Blog Homepage</a>\n</div>\n\n</main>\n</body>\n</html>')
outputFile.close()
			
		
		
		
