hook global InsertCompletionShow .* %{
  try %{
    # this command temporarily removes cursors preceded by whitespace;
    # if there are no cursors left, it raises an error, does not
    # continue to execute the mapping commands, and the error is eaten
    # by the `try` command so no warning appears.
    execute-keys -draft 'h<a-K>\h<ret>'
    map window insert <tab> <c-n>
    map window insert <s-tab> <c-p>
    hook -once -always window InsertCompletionHide .* %{
      unmap window insert <tab> <c-n>
      unmap window insert <s-tab> <c-p>
    }
  }
}

