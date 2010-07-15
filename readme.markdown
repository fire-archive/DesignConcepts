# Compiling Pdf

Open Ubuntu.

Install git.

    $ sudo apt-get install git-core

Get repository.

    $  git clone git@github.com:fire/DesignConcepts.git

Install texlive.

    $ sudo apt-get install texlive-latex-extra

Run.

    $ cd DesignConcepts
    $ buildConcepts.sh

Open pdf.

    $ evince src/DesignConcepts.wip.pdf
