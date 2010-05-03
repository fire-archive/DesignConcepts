 if [ "$2" = "-n" ]
  then 
   dryrun="-n"
  else
   dryrun=""
fi

a2x --fop -f $1 $dryrun -d book ./src/GameDesignConcepts.txt
mv ./src/GameDesignConcepts.$1 .

# -n for dry run
# --xsltproc-opts "./style.xsl"
