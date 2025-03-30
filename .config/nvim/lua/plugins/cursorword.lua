return {
  'echasnovski/mini.cursorword'
  , version = false
  , lazy = true
  , init = function()
    require("mini.cursorword").setup({
      -- Delay (in ms) between when cursor moved and when highlighting appeared
      delay = 100,
    })
  end
}
