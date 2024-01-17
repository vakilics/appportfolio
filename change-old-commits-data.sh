git filter-branch --commit-filter '
      if [ "$GIT_AUTHOR_EMAIL" = "vakili@univention.de" ];
      then
              GIT_AUTHOR_NAME="Abdul Rahman, Vakili";
              GIT_AUTHOR_EMAIL="vakili.hu.it@gmal.com";
              git commit-tree "$@";
      else
              git commit-tree "$@";
      fi' HEAD
