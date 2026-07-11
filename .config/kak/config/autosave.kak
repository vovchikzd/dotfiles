hook global BufCreate /.* %{
  hook buffer NormalIdle .* %{
    try %{
      eval %sh{ [ "$kak_modified" = false ] && printf 'fail' }
      write
    }
  }
  hook buffer InsertIdle .* %{
    try %{
      eval %sh{ [ "$kak_modified" = false ] && printf 'fail' }
      write
    }
  }
}
