vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1

vim.opt.termguicolors = true

local function my_on_attach(bufnr)
  local api = require "nvim-tree.api"

  local function opts(desc)
    return { desc = "nvim-tree: " .. desc, buffer = bufnr, noremap = true, silent = true, nowait = true }
  end

  -- default mappings
  api.config.mappings.default_on_attach(bufnr)

  -- custom mappings
  vim.keymap.set('n', '<C-t>', api.tree.change_root_to_parent,        opts('Up'))
  vim.keymap.set('n', '?',     api.tree.toggle_help,                  opts('Help'))
end

local opts = { noremap = true, silent = true}
local keymap = vim.api.nvim_set_keymap

-- open file explorer in left side on "Space-e"
keymap("n", "<leader>e", ":NvimTreeToggle<cr>", opts)
keymap("n", "<leader>o", ":NvimTreeFocus<cr>", opts)

return {
  -- neotree ???
  "nvim-tree/nvim-tree.lua",
  config = function()
    require("nvim-tree").setup({
      sort_by = "case_sensitive",
      view = {
        width = 26,
      },
      renderer = {
        group_empty = true,
      },
      filters = {
        dotfiles = false,
      },
      on_attach = my_on_attach,
    })
  end
}

