cd ~/larch-three-gentlemen
R="canon/refs/style_anchor.jpg canon/refs/view_desk_C.jpg canon/refs/tea.jpg canon/refs/prop_tea.jpg canon/refs/prop_phone.jpg canon/refs/prop_laptop_tablet.jpg canon/refs/c.jpg canon/refs/m.jpg canon/refs/s.jpg"
run(){ python3 tools/gen.py art/gen/s5/$1.png art/cg/s5/$1.prompt.txt $R > art/gen/s5/$1.log 2>&1; }
for k in 05A 05-2 05-6 01-6 05-0; do run $k & done; wait
for k in 05-1 05-3 05-4; do run $k & done; wait
cat art/gen/s5/*.log
