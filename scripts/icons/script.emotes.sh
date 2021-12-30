for f in *.svg;
do
echo "Changing color of $f ..."
sed -i --follow-symlinks 's/#000/#282828/gI' "$f";
sed -i --follow-symlinks 's/#fff/#ebdbb2/gI' "$f";
sed -i --follow-symlinks 's/#F7F7F7/#ebdbb2/gI' "$f";
sed -i --follow-symlinks 's/#FFCC4D/#fabd2f/gI' "$f";
sed -i --follow-symlinks 's/#664500/#504945/gI' "$f";
sed -i --follow-symlinks 's/#5DADEC/#83a598/gI' "$f";
sed -i --follow-symlinks 's/#292F33/#282828/gI' "$f";
sed -i --follow-symlinks 's/#FDCB58/#fabd2f/gI' "$f";
sed -i --follow-symlinks 's/#E75A70/#fb4934/gI' "$f";
sed -i --follow-symlinks 's/#f76363/#fb4934/gI' "$f";
sed -i --follow-symlinks 's/#8E142A/#9d0006/gI' "$f";
sed -i --follow-symlinks 's/#FF7892/#d3869b/gI' "$f";
sed -i --follow-symlinks 's/#F5F8FA/#ebdbb2/gI' "$f";
sed -i --follow-symlinks 's/#65471B/#665c54/gI' "$f";
sed -i --follow-symlinks 's/#825D0E/#665c54/gI' "$f";
sed -i --follow-symlinks 's/#DD2E44/#cc241d/gI' "$f";
sed -i --follow-symlinks 's/#D79E84/#d3869b/gI' "$f";
sed -i --follow-symlinks 's/#642116/#af3a03/gI' "$f";
sed -i --follow-symlinks 's/#BF6952/#b16286/gI' "$f";
sed -i --follow-symlinks 's/#9B3C07/#af3a03/gI' "$f";
sed -i --follow-symlinks 's/#77B255/#b8bb26/gI' "$f";
sed -i --follow-symlinks 's/#3E721D/#427b58/gI' "$f";
sed -i --follow-symlinks 's/#FFAC33/#fabd2f/gI' "$f";
sed -i --follow-symlinks 's/#2A6797/#458588/gI' "$f";
sed -i --follow-symlinks 's/#64AADD/#83a598/gI' "$f";
sed -i --follow-symlinks 's/#DA2F47/#cc241d/gI' "$f";
sed -i --follow-symlinks 's/#F76363/#fb4934/gI' "$f";

done
