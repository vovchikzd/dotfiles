local opts = { noremap = true, silent = true}
local keymap = vim.api.nvim_set_keymap

keymap("n", "<S-l>", ":bnext<CR>", opts) -- go to next buffer
keymap("n", "<S-h>", ":bprevious<CR>", opts) -- go to prev buffer
keymap("n", "<leader>d", "<cmd>bdelete<CR>", opts) -- close current tab

return {
  "akinsho/bufferline.nvim",
  config = function()
    local status_ok, bufferline = pcall(require, "bufferline")
    if not status_ok then
      return
    end
    bufferline.setup()
  end,
}
