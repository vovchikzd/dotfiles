return {
  "SmiteshP/nvim-navic"
  , dependensies = { "neovim/nvim-lspconfig" }
  -- , init = function ()
  --   vim.o.winbar = "%{%v:lua.require'nvim-navic'.get_location()%}"
  -- end
  , opts = {
    highlight = true
    , lsp = { auto_attach = true }
  }
}
