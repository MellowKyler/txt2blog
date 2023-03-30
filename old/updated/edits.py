if ' !newline ' in line:
			lineSplit = line.split(' !newline ')
			print('Found newline')
			lineSplitCount = -2
			splitLineOutput = ''
			for j in lineSplit:
				print('[New line split]')
				lineSplitCount = lineSplitCount + 2
				lineSplit1 = lineSplit[lineSplitCount] + '</p>\n'
				print('\nLine Split 1: ' + lineSplit1)
				lineSplit2 = '<p>' + lineSplit[lineSplitCount + 1]
				print('\nLine Split 2: ' + lineSplit2)
				splitLineOutput = splitLineOutput + lineSplit1 + lineSplit2
			line = splitLineOutput