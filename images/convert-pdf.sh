for pdf in *{pdf,PDF} ; do
    convert "$pdf" "${pdf%%.*}.png"
done
