local opts = {
      -- A list of parser names, or "all" (the five listed parsers should always be installed)
      ensure_installed = {"c", "cpp", "python", "lua", "bash",
        "rust", "cmake", "git_config", "git_rebase", "gitattributes",
        "gitcommit", "gitignore", "llvm", "nasm", "ninja", "tmux"},
      -- Install parsers synchronously (only applied to `ensure_installed`)
      sync_install = true,

      -- Automatically instakkll missing parsers when entering buffer
      auto_install = false,

      -- List of parsers to ignore installing (for "all")
      ignore_install = {},

      highlight = {
        enable = true,
        -- Instead of true it can also be a list of languages
        additional_vim_regex_highlighting = false,
      },

      indent = {
        enable = true
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

return {
  "nvim-treesitter/nvim-treesitter",
  config = function()
    local parser_config = require "nvim-treesitter.parsers".get_parser_configs()
    parser_config.c3 = {
      install_info = {
        url = "https://github.com/c3lang/tree-sitter-c3",
        files = {"src/parser.c", "src/scanner.c"},
        branch = "main",
      },
    }
    require('nvim-treesitter.configs').setup(opts)
  end
}
