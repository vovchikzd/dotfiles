return {
  "neovim-treesitter/nvim-treesitter"
  , branch = "main"
  , lazy = false
  , build = ":TSUpdate"
  , init = function()
    vim.api.nvim_create_autocmd('FileType', {
      pattern = { 'c', "cpp", "python", "lua", "bash", "rush", "cmake",
        "gitconfig", "gitrebase", "gitignore", "gitattributes", "gitcommit",
        "llvm", "nasm", "ninja", "tmux", "markdown", "typst", "zig", "fish",
        "gnuplot", "hyprlang", "make", "sql", "toml", "xml", "yaml"
      }
      , callback = function()
        vim.treesitter.start()
        -- vim.wo.foldexpr = "v:lua.vim.treesitter.foldexpr()"
        -- vim.wo.foldmethod = 'expr'
        vim.bo.indentexpr = "v:lua.require'nvim-treesitter'.indentexpr()"
      end
    })
  end
  , config = function()
    local ts = require("nvim-treesitter")
    ts.install({ 'c', "cpp", "python", "lua", "bash", "rust", "cmake",
      "git_config", "git_rebase", "gitattributes", "gitcommit", "gitignore",
      "llvm", "nasm", "ninja", "tmux", "markdown", "typst", "zig",
      "fish", "gnuplot", "hyprlang", "make", "markdown_inline", "printf",
      "regex", "sql", "toml", "xml", "yaml" })
    ts.setup({
      auto_install = true
      , ignore_install = {}
      , indent = { enable = true }
      , highlight = { enable = true }
    })
  end
}
