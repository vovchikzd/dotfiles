require('nvim-treesitter.configs').setup {
  -- A list of parser names, or "all" (the five listed parsers should always be installed)
  ensure_installed = {},
  -- Install parsers synchronously (only applied to `ensure_installed`)
  sync_install = true,

  -- Automatically instakkll missing parsers when entering buffer
  auto_install = true,

  -- List of parsers to ignore installing (for "all")
  ignore_install = {"javascript"},

  highlight = {
    enable = true,
    -- Instead of true it can also be a list of languages
    additional_vim_regex_highlighting = false,
  },

rainbow = {
    enable = true,
    -- disable = { "jsx", "cpp" }, list of languages you want to disable the plugin for
    extended_mode = true, -- Also highlight non-bracket delimiters like html tags, boolean or table: lang -> boolean
    max_file_lines = nil, -- Do not enable for files with more than n lines, int
    -- colors = {}, -- table of hex strings
    -- termcolors = {} -- table of colour name strings
  },

  context_commentstring = {
    enable = true,
    enable_autocmd = false,
  },
}


