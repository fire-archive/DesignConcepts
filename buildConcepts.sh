cd src
../versiontag.sh
../multimarkdown/Utilities/mmd_merge.pl GameDesignConcepts.txt > DesignConcepts.wip.txt
../multimarkdown/bin/mmd2PDF.pl DesignConcepts.wip.txt
rm version.txt
