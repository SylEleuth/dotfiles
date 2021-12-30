for f in *.svg;
do
echo "Changing color of $f ..."
# sed -i --follow-symlinks 's/#000000/#282828/gI' "$f";
# sed -i --follow-symlinks 's/#ffffff/#ebdbb2/gI' "$f";
# sed -i --follow-symlinks 's/#5e5e5e/#665c54/gI' "$f";
# sed -i --follow-symlinks 's/#ff6600/#fe8019/gI' "$f";
# sed -i --follow-symlinks 's/#262626/#282828/gI' "$f";
# sed -i --follow-symlinks 's/#424242/#3c3836/gI' "$f";
# sed -i --follow-symlinks 's/#9a06ff/#8f3f71/gI' "$f";
# sed -i --follow-symlinks 's/#ffca28/#fabd2f/gI' "$f";
# sed -i --follow-symlinks 's/#ef5350/#fb4934/gI' "$f";
# sed -i --follow-symlinks 's/#ff9605/#fe8019/gI' "$f";
# sed -i --follow-symlinks 's/#4caf50/#689d6a/gI' "$f";
# sed -i --follow-symlinks 's/#ec407a/#fb4934/gI' "$f";
# sed -i --follow-symlinks 's/#4e9a06/#689d6a/gI' "$f";
# sed -i --follow-symlinks 's/#bfbfbf/#bdae93/gI' "$f";
# sed -i --follow-symlinks 's/#8b8b8b/#928374/gI' "$f";
# sed -i --follow-symlinks 's/#008000/#427b58/gI' "$f";
# sed -i --follow-symlinks 's/#dcdcdc/#ebdbb2/gI' "$f";
# sed -i --follow-symlinks 's/#ff00ff/#b16286/gI' "$f";
sed -i --follow-symlinks 's/#ff00ff/#b16286/gI' "$f";

done
