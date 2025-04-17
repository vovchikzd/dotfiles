local colorHighlight = {
  "brenoprata10/nvim-highlight-colors"
  , lazy = true
  , init = function()
    require("nvim-highlight-colors").setup({
      render = "foregroung"
      , enable_hex = true
      , enable_short_hex = true
      , enable_rgb = true
      , enable_hsl = true
      , enable_ansi = true
      , enable_hsl_without_function = true
      , enable_var_usage = true
      , enable_named_colors = true
      , enable_tailwind = true
      , custom_colors = {
        --- Label must be properly escaped with '%' to adhere to `string.gmatch`
        --- :help string.gmatch
        { label = '%-%-theme%-primary%-color', color = '#0f1219' }
        , { label = '%-%-theme%-secondary%-color', color = '#5a5d64' }
      }
    })
  end
}

return colorHighlight
