for i in $(find -name '*.png')
do
	convert $i -crop 1200x1200+0+0 $i
	echo cropingm $i
done
