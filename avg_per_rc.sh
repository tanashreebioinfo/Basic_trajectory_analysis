list=($(seq -180.0 5.0 185.0))
f=$1
for i in "${!list[@]}"; do
        thiselement="${list[i]}"
            nextelement="${list[i+1]}"
                python extract_avg2.py $f $thiselement $nextelement
                #awk '{if($1>=thiselement && $1<=nextelement) print $2}' solv_tg.dat
            done
