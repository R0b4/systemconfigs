ls ./configs/$1 > /dev/null
if [ $? -gt 0 ]
then
	echo $1 system config does not exist
	exit 1
fi

sudo pacman -Syu --noconfirm

yay -V > /dev/null
if [ $? -eq 127 ]
then
    echo hello
    sudo pacman -S --needed --noconfirm git base-devel
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si --noconfirm --needed
    rm -rf yay
fi

yay -S --noconfirm --needed - < ./configs/$1/packages.txt

if [ $? -gt 0 ]
then
	echo failed to install needed packages
	exit 2
fi

sudo cp -r ./configs/$1/root/. /

if [ $? -gt 0 ]
then
	echo failed to copy global files
	exit 3
fi

sudo cp -r ./configs/$1/home/. ~
if [ $? -gt 0 ]
then
	echo failed to copy user files
	exit 4
fi

if [ -e ./configs/$1/setup.sh ]
then
	sh ./configs/$1/setup.sh
fi

sudo reboot
