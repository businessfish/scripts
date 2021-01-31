
for i in $1/*
do
	echo "== [$i] MEDATA =="

	exiftool "$i" | awk '/File Name/ || /MIME Type/ || /Title/ || /Title of Parts/ || /Author/ || /Last Modified By/ || /Last Printed/ || /Producer/ || /Software/ || /Create Date/ || /Modify Date/ || /Company/'
	#exiftool $1 | grep "File Name"
	#exiftool $1 | grep "MIME Type"
	#exiftool $1 | grep -w "Title"
	#exiftool $1 | grep "Title of Parts"
	#exiftool $1 | grep "Author"
	#exiftool $1 | grep "Last Modified By"
	#exiftool $1 | grep "Last Printed"
	#exiftool $1 | grep "Producer"
	#exiftool $1 | grep "Software"
	#exiftool $1 | grep "Create Date"
	#exiftool $1 | grep "Modify Date"
	#exiftool $1 | grep "Company"
done
