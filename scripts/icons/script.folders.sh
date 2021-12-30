for f in *.svg;
do
echo "Changing color of $f ..."
sed -i -- 's/#9eb78c/#ebdbb2/g' "$f";
sed -i -- 's/#75955e/#d5c4a1/g' "$f";
sed -i -- 's/#8ec07c/#ebdbb2/g' "$f";
sed -i -- 's/#689d6a/#d5c4a1/g' "$f";
sed -i -- 's/#000/#1d2021/g' "$f";
sed -i -- 's/#fff/#fbf1c7/g' "$f";
sed -i -- 's/#491706/#282828/g' "$f";
sed -i -- 's/#af3a03/#282828/g' "$f";
sed -i -- 's/#404859/#3c3836/g' "$f";
sed -i -- 's/#8997af/#a89984/g' "$f";

done
