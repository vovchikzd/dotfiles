return {
  "nvim-treesitter/nvim-treesitter"
  , branch = "master"
  , lazy = false
  , build = ":TSUpdate"
  , config = function()
    require("nvim-treesitter.configs").setup({
      ensure_installed = { 'c', "cpp", "python", "lua", "bash", "rust", "cmake",
        "git_config", "git_rebase", "gitattributes", "gitcommit", "gitignore",
        "llvm", "nasm", "ninja", "tmux", "markdown", "latex", "typst", "zig",
        "fish", "gnuplot", "hyprlang", "make", "markdown_inline", "printf",
        "regex", "sql", "toml", "xml", "yaml" }
      , auto_install = true
      , ignore_install = {}
      , indent = { enable = true }
      , highlight = { enable = true }
    })
  end
}
