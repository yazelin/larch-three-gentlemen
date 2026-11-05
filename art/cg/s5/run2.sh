cd ~/larch-three-gentlemen
R="canon/refs/style_anchor.jpg canon/refs/view_desk_C.jpg canon/refs/tea.jpg canon/refs/prop_tea.jpg canon/refs/prop_phone.jpg canon/refs/prop_laptop_tablet.jpg canon/refs/c.jpg canon/refs/m.jpg canon/refs/s.jpg"
V="art/gen/s5/05A.png canon/refs/tea.jpg canon/refs/s.jpg"
mv art/gen/s5/05-0.png art/cg/rejected/05-0_v2.png; mv art/gen/s5/05-3.png art/cg/rejected/05-3_v1.png
python3 tools/gen.py art/gen/s5/05-0.png art/cg/s5/05-0.prompt.txt $R > art/gen/s5/05-0.log 2>&1 &
python3 tools/gen.py art/gen/s5/05-3.png art/cg/s5/05-3.prompt.txt $R > art/gen/s5/05-3.log 2>&1 &
for k in 05A-1 05A-2 05A-3; do python3 tools/gen.py art/gen/s5/$k.png art/cg/s5/$k.prompt.txt $V > art/gen/s5/$k.log 2>&1 & done; wait
for k in 05A-4 05A-5; do python3 tools/gen.py art/gen/s5/$k.png art/cg/s5/$k.prompt.txt $V > art/gen/s5/$k.log 2>&1 & done; wait
cat art/gen/s5/*.log | grep -v "^ok" ; echo done
