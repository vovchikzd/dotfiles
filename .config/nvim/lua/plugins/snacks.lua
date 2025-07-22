return {
  "folke/snacks.nvim"
  , priority = 1000
  , opts = {
    indent = { animate = { enabled = false } }
    , scope = { enabled = true }
    , scroll = { enabled = true }
    , explorer = { replace_netrw = true }

    , image = { convert = { notify = false } }
    , picker = {
      matcher = { sort_empty = true, frecency = true }
      , formatters = { file = { filename_first = true } }
      , previewers = { man_pager = "nvim -c Man!" }
    }
  }
}
