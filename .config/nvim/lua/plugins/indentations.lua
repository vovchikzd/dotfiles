local scope = {
  show_start = false,
  show_end = false,
}

local indentations = {
  "lukas-reineke/indent-blankline.nvim",
  main = "ibl",
  config = function()
    require("ibl").setup({
      scope = scope,
    })
  end,
}

return indentations
