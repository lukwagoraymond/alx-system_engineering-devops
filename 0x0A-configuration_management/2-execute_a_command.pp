# Kill a process call "killmenow"
exec { 'killmenow':
    command  => 'pkill -9 killmenow',
    provider => shell,
}
