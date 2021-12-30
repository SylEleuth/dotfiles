for f in *.svg;
do
echo "Changing color of $f ..."
sed -i --follow-symlinks 's/#af7f4c/#fe8019/gI' "$f";
sed -i --follow-symlinks 's/#4c76af/#458588/gI' "$f";
sed -i --follow-symlinks 's/#ffffff/#ebdbb2/gI' "$f";
sed -i --follow-symlinks 's/#252a35/#282828/gI' "$f";
sed -i --follow-symlinks 's/#f44336/#fb4934/gI' "$f";
sed -i --follow-symlinks 's/#4caf99/#689d6a/gI' "$f";
sed -i --follow-symlinks 's/#af4c5f/#8f3f71/gI' "$f";
sed -i --follow-symlinks 's/#4caf50/#b8bb26/gI' "$f";
sed -i --follow-symlinks 's/#c579be/#d3869b/gI' "$f";
sed -i --follow-symlinks 's/#5c616c/#ebdbb2/gI' "$f";
sed -i --follow-symlinks 's/#5294e2/#458588/gI' "$f";
sed -i --follow-symlinks 's/#5294e2/#458588/gI' "$f";

done
