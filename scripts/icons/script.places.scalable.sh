for f in *.svg;
do
echo "Changing color of $f ..."
sed -i --follow-symlinks 's/#fcefe8/#ebdbb2/gI' "$f";
sed -i --follow-symlinks 's/#ffffff/#ebdbb2/gI' "$f";
sed -i --follow-symlinks 's/#ebebeb/#ebdbb2/gI' "$f";
sed -i --follow-symlinks 's/#4f1748/#1d2021/gI' "$f";
sed -i --follow-symlinks 's/#a0649a/#1d2021/gI' "$f";
sed -i --follow-symlinks 's/#ddc8db/#1d2021/gI' "$f";

done
