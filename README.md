# Linux_Path_Traversal-Virtual_Linux_Terminal

Implemented various Linux commands, as follows:\
`cd <path>`\
`mkdir <path>`\
`rm <path>`\
`pwd`\
There would be an additional command, for application purpose, which is\
`session_clear`\
It will clear all the previous operations and put back the application to starting point, as if application started just now.

Problem will have a command line environment, where testing input would be as command line input. 

At start, application would be at **ROOT directory ‘/’**, Overtime application would be provided with various commands. 

Examples:\
	Following is in ordered way. \
  `  $ <Starting your application...>`\
`    $ pwd`\
`    PATH: /`\
`    $ cd /some/random/path/which/doesn’t/exist`\
`    ERR: INVALID PATH`\
`    $ mkdir dir1`\
`    SUCC: CREATED`\
`    $ mkdir dir1`\
`    ERR: DIRECTORY ALREADY EXISTS`\
`    $ mkdir dir2`\
`    SUCC: CREATED`\
`     $ ls`\
`    DIRS: dir1	dir2`\
`    $ cd dir1`\
`    SUCC: REACHED`\
`    $ pwd`\
`    PATH: /dir1`\
`    $ cd /`\
`    SUCC: REACHED`\
`    $ rm /dir1`\
`    SUCC: DELETED`\
`    $ cd /dir1`\
`    ERR: INVALID PATH`\
`    $ mkdir /dir3`\
`    SUCC: CREATED`\
`    $ cd /dir2`\
`    SUCC: REACHED`\
`    $ pwd`\
`    PATH: /dir2`\
`    $ session_clear`\
`    SUCC: CLEARED: RESET TO ROOT`\
`    $ pwd`\
`    PATH: /`\
`    $ asdf asdf`\
`    ERR: CANNOT RECOGNIZE INPUT.`\
