ls ./configs/$1 > /dev/null
if [ $? -gt 0 ]
then
	echo $1 system config does not exist
	exit 1
fi

mkdir -p ./configs/$1/root
mkdir -p ./configs/$1/home

for i in $(cat ./configs/$1/dirs.txt)
do
	mkdir -p $(dirname ./configs/$1/root/$i)
	sudo cp -r /$i ./configs/$1/root/$i

	if [ $? -gt 0 ]
	then
		echo failed to get /$i
		exit 2
	fi
done

for i in $(cat ./configs/$1/rel_dirs.txt)
do
	mkdir -p $(dirname ./configs/$1/home/$i)
	cp -r ~/$i ./configs/$1/home/$i

	if [ $? -gt 0 ]
	then
		echo failed to get ~/$i
		exit 2
	fi
done
