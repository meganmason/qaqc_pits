#!/bin/bash

files="/Users/mamason6/Downloads/testy/*.pdf"
#files="/Users/mamason6/Downloads/ER_pdfs/*.pdf"
suffix=".jpg"

for file in $files
 do
	convert -density 150 $file -quality 90 $file
	#basename -s .pdf $file
	#mv "basename -s .pdf $file" "{$file}$suffix"
done
