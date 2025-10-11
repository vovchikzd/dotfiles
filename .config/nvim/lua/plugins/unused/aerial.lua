return {
  "stevearc/aerial.nvim"
  , lazy = true
  , dependencies = {
    "nvim-treesitter/nvim-treesitter"
      , "nvim-mini/mini.icons"
  }
  , opts = {
    backends = { "lsp", "treesitter" }
    , layout = {
      min_width = 30
      , default_direction = "prefer_left"
    }
    , filter_kind = false
    , show_guides = true
  }
  , keys = {
    { "<leader>s", "<cmd>AerialToggle<CR>" }
  }
}
