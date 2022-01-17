for i in $(ls ./configs)
do
	echo $i
	if [ -e ./configs/$i/description.txt ]
	then
		cat ./configs/$i/description.txt
	fi
	echo
done
