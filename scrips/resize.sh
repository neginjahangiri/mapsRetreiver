for i in $(find ../pix2pix-tensorflow/photos_combined/* -type f -name "*.png")
do
	echo resizing $i
	convert $i -resize 50% $i
done
