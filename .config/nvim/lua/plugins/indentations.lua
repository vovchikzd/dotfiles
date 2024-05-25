local scope = {
  show_start = false,
  show_end = true,
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
