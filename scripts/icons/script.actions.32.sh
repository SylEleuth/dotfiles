for f in *.svg;
do
echo "Changing color of $f ..."
# sed -i --follow-symlinks 's/#ffb900/#fabd2f/gI' "$f";
# sed -i --follow-symlinks 's/#ffffff/#ebdbb2/gI' "$f";
# sed -i --follow-symlinks 's/#fff"/#ebdbb2"/gI' "$f";
# sed -i --follow-symlinks 's/#ff0000/#fb4934/gI' "$f";
sed -i --follow-symlinks 's/#ffdc40/#fabd2f/gI' "$f";
sed -i --follow-symlinks 's/#124b85/#076678/gI' "$f";
sed -i --follow-symlinks 's/#e4e4e4/#ebdbb2/gI' "$f";
sed -i --follow-symlinks 's/#16a085/#076678/gI' "$f";
sed -i --follow-symlinks 's/#165ba0/#689d6a/gI' "$f";
sed -i --follow-symlinks 's/#12806a/#689d6a/gI' "$f";
sed -i --follow-symlinks 's/#16a085/#689d6a/gI' "$f";
sed -i --follow-symlinks 's/#5164d7/#076678/gI' "$f";
sed -i --follow-symlinks 's/#ffcc19/#fabd2f/gI' "$f";
sed -i --follow-symlinks 's/#c43f0d/#af3a03/gI' "$f";
sed -i --follow-symlinks 's/#956a42/#7c6f64/gI' "$f";
sed -i --follow-symlinks 's/#c2eeff/#bdae93/gI' "$f";
sed -i --follow-symlinks 's/#e33e00/#fb4934/gI' "$f";
sed -i --follow-symlinks 's/#4f4f4f/#504945/gI' "$f";
sed -i --follow-symlinks 's/#d4d4d4/#d5c4a1/gI' "$f";
sed -i --follow-symlinks 's/#34a046/#979617/gI' "$f";
sed -i --follow-symlinks 's/#ff9e29/#fe8019/gI' "$f";
sed -i --follow-symlinks 's/#fabd7f/#fabd2f/gI' "$f";
sed -i --follow-symlinks 's/#6650d2/#8f3f71/gI' "$f";
sed -i --follow-symlinks 's/#ad3f36/#af3a03/gI' "$f";
sed -i --follow-symlinks 's/#3b8ae0/#458588/gI' "$f";
sed -i --follow-symlinks 's/#7dc564/#8ec07c/gI' "$f";
sed -i --follow-symlinks 's/#ffda46/#fabd2f/gI' "$f";
sed -i --follow-symlinks 's/#b38d32/#b57614/gI' "$f";

done
