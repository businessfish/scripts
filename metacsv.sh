columns=("File Name" "MIME Type" "Title" "Title of Parts" "Author" "Last Modified By" "Last Printed" "Producer" "Software" "Create Date" "Modify Date" "Company")
row=("N/A" "N/A" "N/A" "N/A" "N/A" "N/A" "N/A" "N/A" "N/A" "N/A" "N/A" "N/A")
lastline=""
# print the columns
for c in "${columns[@]}"
do
	echo -n "$c,"
done
echo ""

# for each line in the exiftool data
while read -r line
do
	# if its a formatting line ignore it
	if [[ $line =~ "MEDATA =="  ]] ; then
		# print out the contents of the row and clear it for the next file
		for text in "${row[@]}"
		do
			echo -n "$text,"
			text="N/A"
		done
		echo ""
		#echo ""
	else
		# get name of metadata tag
		word=`echo $line | cut -d: -f1 | xargs`
		i=0
		# put the data in the corresponding column
		for col in "${columns[@]}"
		do
			# data should be everything after first colon
			if [[ $word == $col ]] ; then
				row[$i]=`echo $line | cut -d: -f 2- | xargs`
			fi
			i=$((i+1))
		done
		#exit 1
	fi
done < $1

# print the last row since we wont see a trailing format line
for text in "${row[@]}"
do
	echo -n "$text,"
	text="N/A"
done
echo ""
