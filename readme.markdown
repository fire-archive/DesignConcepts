# Compiling Pdf

Open Ubuntu.

Install git.

    $ sudo apt-get install git-core

Get repository.

    $ git clone http://github.com/fire/DesignConcepts.git

Install texlive.

    $ sudo apt-get install texlive-latex-extra

Change into git directory.

    $ cd DesignConcepts

Run.

    $ ./buildConcepts.sh

Open pdf.

    $ evince src/DesignConcepts.wip.pdf
