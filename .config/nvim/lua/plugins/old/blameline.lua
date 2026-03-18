return {
  "Yu-Leo/blame-column.nvim"
  , opts = {}
  , keys = {
    { "<C-g>", function() require("blame-column").toggle() end, desc = "Toggle blame"}
  }
}
