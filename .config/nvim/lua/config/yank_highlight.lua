vim.api.nvim_create_autocmd({ "TextYankPost", "TextPutPost" }, {
  desc = "Highlight when yanking (copying) or pasting text"
  , group = vim.api.nvim_create_augroup("kickstart-highlight-yank_paste", { clear = true }) 
  , callback = function()
    vim.hl.hl_op({ timeout = 250 })
  end
})
