local align = {
  "Vonr/align.nvim",
  lazy = true,
  init = function()
    local opts = function(description)
      return { noremap = true, silent = true, desc = description}
    end
    local keymap = vim.keymap.set
    keymap("x", "aa", function() require("align").align_to_char({length = 1}) end, opts("Align to 1 character"))
    keymap("x", "ad", function() require("align").align_to_char({length = 2, preview = true}) end, opts("Align to 2 characters"))
    keymap("x", "aw", function() require("align").align_to_string({regex = false, preview = true}) end, opts("Align to strign"))
  end,
}

return align
