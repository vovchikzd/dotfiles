require "options"
require "keymaps"

local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not (vim.uv or vim.loop).fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", -- latest stable release
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

vim.filetype.add({
  extension = {
    c3 = "c3",
    c3i = "c3",
    c3t = "c3",
  },
  filename = {
    [".bash_env"] = "bash",
    [".bash_functions"] = "bash"
  }
})

vim.api.nvim_create_autocmd('TextYankPost', {
  desc = 'Highlight when yanking (copying) text',
  group = vim.api.nvim_create_augroup('kickstart-highlight-yank', { clear = true }),
  callback = function()
    vim.highlight.on_yank({ timeout = 250 })
  end,
})

vim.api.nvim_create_autocmd("FileType", {
  pattern = {"typst"},  -- для каких файлов включить
  callback = function()
    vim.bo.textwidth = 80       -- максимальная длина строки
    vim.bo.wrapmargin = 0       -- отключаем wrapmargin (устаревший аналог)
    vim.bo.formatoptions = vim.bo.formatoptions .. "t"  -- перенос по textwidth
    vim.bo.formatoptions = vim.bo.formatoptions:gsub("c", "")  -- отключаем автоформат комментариев
  end,
})

vim.api.nvim_create_autocmd('LspAttach', {
  callback = function(ev)
    local client = vim.lsp.get_client_by_id(ev.data.client_id)
    if client:supports_method('textDocument/completion') then
      vim.lsp.completion.enable(true, client.id, ev.buf, { autotrigger = true })
    end
  end
})

vim.diagnostic.config({ virtual_lines = { current_line = true }})

local opts = {
  change_detection = {
    -- automatically check for config file changes and reload the ui
    enabled = true,
    notify = false, -- get a notification when changes are found
  },
}

require("lazy").setup("plugins", opts)
