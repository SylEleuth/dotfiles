for f in *.svg;
do
echo "Changing color of $f ..."
# sed -i --follow-symlinks 's/#f55/#fb4934/g' "$f";
# # sed -i --follow-symlinks 's/#fff/#ebdbb2/g' "$f";
# # sed -i --follow-symlinks 's/#555/#ebdbb2/g' "$f";
# sed -i --follow-symlinks 's/#555555/#ebdbb2/g' "$f";
sed -i --follow-symlinks 's/#000000/#282828/g' "$f";
# # sed -i --follow-symlinks 's/#666/#665c54/g' "$f";
# sed -i --follow-symlinks 's/#0ff/#8fc17d/g' "$f";
# sed -i --follow-symlinks 's/#000/#282828/g' "$f";
# sed -i --follow-symlinks 's/#333/#3c3836/g' "$f";
# sed -i --follow-symlinks 's/#687583/#ebdbb2/g' "$f";
# sed -i --follow-symlinks 's/#9bd916/#b8bb26/g' "$f";
# sed -i --follow-symlinks 's/#fc963a/#fe8019/g' "$f";
# sed -i --follow-symlinks 's/#cf000f/#fb4934/g' "$f";
# sed -i --follow-symlinks 's/#f9d24c/#fabd2f/g' "$f";
# sed -i --follow-symlinks 's/#ffa555/#fe8019/g' "$f";
# sed -i --follow-symlinks 's/#cf74e0/#b16286/g' "$f";
# sed -i --follow-symlinks 's/#3c56a0/#458588/g' "$f";
# sed -i --follow-symlinks 's/#0b0b64/#076678/g' "$f";
# sed -i --follow-symlinks 's/#4040bf/#458588/g' "$f";
# sed -i --follow-symlinks 's/#6c7a89/#ebdbb2/g' "$f";
# sed -i --follow-symlinks 's/#51db51/#8ec07c/g' "$f";
# sed -i --follow-symlinks 's/#f62459/#fb4934/g' "$f";
# sed -i --follow-symlinks 's/#209ae7/#83a598/g' "$f";
# sed -i --follow-symlinks 's/#209ae7/#ebdbb2/g' "$f";
# sed -i --follow-symlinks 's/#ec2411/#cc241d/g' "$f";
# sed -i --follow-symlinks 's/#25bb70/#8ec07c/g' "$f";
# sed -i --follow-symlinks 's/#8542c2/#8f3f71/g' "$f";
# sed -i --follow-symlinks 's/#fa752a/#fe8019/g' "$f";
# sed -i --follow-symlinks 's/#4bc94b/#8ec07c/g' "$f";
# sed -i --follow-symlinks 's/#22a7f0/#458588/g' "$f";
# sed -i --follow-symlinks 's/#8e44ad/#8f3f71/g' "$f";
# sed -i --follow-symlinks 's/#383838/#ebdbb2/g' "$f";
# sed -i --follow-symlinks 's/#66380e/#af3a03/g' "$f";
# sed -i --follow-symlinks 's/#124c12/#79740e/g' "$f";
# sed -i --follow-symlinks 's/#20598d/#076678/g' "$f";
# sed -i --follow-symlinks 's/#3c559f/#076678/g' "$f";
# sed -i --follow-symlinks 's/#4d4d4d/#282828/g' "$f";
# sed -i --follow-symlinks 's/#898b8d/#ebdbb2/g' "$f";
# sed -i --follow-symlinks 's/#7fcc74/#8ec07c/g' "$f";
# sed -i --follow-symlinks 's/#2e6ad1/#458588/g' "$f";
# sed -i --follow-symlinks 's/#75d8e1/#83a598/g' "$f";
# sed -i --follow-symlinks 's/#897dc5/#d3869b/g' "$f";
# sed -i --follow-symlinks 's/#913d88/#b16286/g' "$f";
# sed -i --follow-symlinks 's/#674172/#8f3f71/g' "$f";
# sed -i --follow-symlinks 's/#c6970c/#d79921/g' "$f";
# sed -i --follow-symlinks 's/#eff0f1/#ebdbb2/g' "$f";
# sed -i --follow-symlinks 's/#f90/#fe8019/g' "$f";
# sed -i --follow-symlinks 's/#ff8b23/#fe8019/g' "$f";
# sed -i --follow-symlinks 's/#f27935/#fe8019/g' "$f";
# sed -i --follow-symlinks 's/#8096a0/#ebdbb2/g' "$f";
# sed -i --follow-symlinks 's/#e3a943/#e3a943/g' "$f";
# sed -i --follow-symlinks 's/#a64d4d/#af3a03/g' "$f";
# sed -i --follow-symlinks 's/#f4a93c/#fabd2f/g' "$f";
# sed -i --follow-symlinks 's/#f64747/#fb4934/g' "$f";
# sed -i --follow-symlinks 's/#8373d7/#b16286/g' "$f";
# sed -i --follow-symlinks 's/#f59e16/#fabd2f/g' "$f";
# sed -i --follow-symlinks 's/#1ed4e5/#83a598/g' "$f";
# sed -i --follow-symlinks 's/#723838/#af3a03/g' "$f";
# sed -i --follow-symlinks 's/#db3333/#cc241d/g' "$f";
# sed -i --follow-symlinks 's/#036b53/#427b58/g' "$f";
# sed -i --follow-symlinks 's/#656f9d/#458588/g' "$f";
# sed -i --follow-symlinks 's/#3a539b/#076678/g' "$f";
# sed -i --follow-symlinks 's/#c4bb1b/#b8bb26/g' "$f";
# sed -i --follow-symlinks 's/#32cab4/#8ec07c/g' "$f";
# sed -i --follow-symlinks 's/#78a7dc/#83a598/g' "$f";
# sed -i --follow-symlinks 's/#5294e2/#458588/g' "$f";
# sed -i --follow-symlinks 's/#dfdfdf/#ebdbb2/g' "$f";
# sed -i --follow-symlinks 's/#0c2d63/#076678/g' "$f";
# sed -i --follow-symlinks 's/#924ab0/#8f3f71/g' "$f";
# sed -i --follow-symlinks 's/#42a603/#98971a/g' "$f";
# sed -i --follow-symlinks 's/#42a603/#b8bb26/g' "$f";
# sed -i --follow-symlinks 's/#20bcfa/#83a598/g' "$f";
# sed -i --follow-symlinks 's/#197cf1/#458588/g' "$f";
# sed -i --follow-symlinks 's/#dc2b41/#fb4934/g' "$f";
# sed -i --follow-symlinks 's/#c61423/#cc241d/g' "$f";
# sed -i --follow-symlinks 's/#04896a/#427b58/g' "$f";
# sed -i --follow-symlinks 's/#13a4f7/#83a598/g' "$f";
# sed -i --follow-symlinks 's/#e00a5e/#fb4934/g' "$f";
# sed -i --follow-symlinks 's/#8542c2/#8f3f71/g' "$f";
# sed -i --follow-symlinks 's/#6fc7e0/#83a598/g' "$f";
# sed -i --follow-symlinks 's/#777/#ebdbb2/g' "$f";
# sed -i --follow-symlinks 's/#16907d/#689d6a/g' "$f";
# sed -i --follow-symlinks 's/#662d0e/#af3a03/g' "$f";
# sed -i --follow-symlinks 's/#94408b/#8f3f71/g' "$f";
# sed -i --follow-symlinks 's/#3f3f3f/#ebdbb2/g' "$f";
# sed -i --follow-symlinks 's/#666666/#282828/g' "$f";
# sed -i --follow-symlinks 's/#ffffff/#ebdbb2/g' "$f";
# sed -i --follow-symlinks 's/#f9b425/#fabd2f/g' "$f";
# sed -i --follow-symlinks 's/#2cbd2c/#8ec07c/g' "$f";
# sed -i --follow-symlinks 's/#52a743/#689d6a/g' "$f";
# sed -i --follow-symlinks 's/#777777/#689d6a/g' "$f";
# sed -i --follow-symlinks 's/#c8e3fe/#83a598/g' "$f";
# sed -i --follow-symlinks 's/#35bedc/#83a598/g' "$f";
# sed -i --follow-symlinks 's/#78da06/#b8bb26/g' "$f";
# sed -i --follow-symlinks 's/#d24d57/#fb4934/g' "$f";

done