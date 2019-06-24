for i in $(find */* -name '*.png')
do
	echo $(file $i)
done
