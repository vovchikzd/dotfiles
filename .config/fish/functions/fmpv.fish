function fmpv
    if test (count $argv) -ne 1
        set_color red
        echo "Too many files passed" >&2
        set_color normal
        return 1
    else if test -z $argv[1]
        set_color red
        echo "Where is playlist file?" >&2
        set_color normal
        return 1
    else if not test -f $argv[1]
        set_color red
        echo "File $argv[1] doesn't exist" >&2
        set_color normal
        return 1
    end
    
    mpv --playlist=$argv[1] &>/dev/null &
end
