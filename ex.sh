
for i in $1/*
do
	echo "== [$i] MEDATA =="
	exiftool "$i" | awk '/File Name/ || /MIME Type/ || /Title/ || /Title of Parts/ || /Author/ || /Last Modified By/ || /Last Printed/ || /Producer/ || /Software/ || /Create Date/ || /Modify Date/ || /Company/'
done
