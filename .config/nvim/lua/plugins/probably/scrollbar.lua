return {
  "petertriho/nvim-scrollbar"
  , config = function ()
    require("scrollbar").setup({
      marks = {
        Cursor = { text = "━", priority = 1000 }
        , Search = { text = { "━" } }
        , Error = { text = { "━" } }
        , Warn = { text = { "━" } }
        , Info = { text = { "━" } }
        , Hint = { text = { "━" } }
        , Misc = { text = { "━" } }
        , GitAdd = { text = "┃" }
        , GitChange = { text = "┃" }
      }
    })
    require("scrollbar.handlers.gitsigns").setup()
  end
}
