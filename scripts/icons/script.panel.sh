for f in *.svg;
do
echo "Changing color of $f ..."
sed -i --follow-symlinks 's/#d3dae3/#ebdbb2/gI' "$f";
sed -i --follow-symlinks 's/#5294e2/#458588/gI' "$f";
sed -i --follow-symlinks 's/#FF2A00/#fb4934/gI' "$f";
sed -i --follow-symlinks 's/#ffffff/#ebdbb2/gI' "$f";
sed -i --follow-symlinks 's/#1ad6ab/#458588/gI' "$f";
sed -i --follow-symlinks 's/#bfc1c1/#d5c4a1/gI' "$f";
sed -i --follow-symlinks 's/#f1f2f3/#ebdbb2/gI' "$f";
sed -i --follow-symlinks 's/#ff0056/#fb4934/gI' "$f";

done
