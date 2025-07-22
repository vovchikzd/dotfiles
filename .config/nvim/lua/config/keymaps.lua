local opts = function(description)
  return { noremap = true, silent = true, desc = description }
end

local keymap = vim.keymap.set

keymap('', "<Space>", "<Nop>", opts("Space as leader key"))
vim.g.mapleader = ' '
vim.g.maplocalleader = ' '

keymap('n', "<leader>|", "<C-w>v", opts("Vertical split"))
keymap('n', "<leader>\\", "<C-w>s", opts("Horizontal split"))
keymap('n', "<leader>c", "<C-w>c", opts("Close split"))

keymap('n', "<C-h>", "<C-w>h", opts("Go to left window"))
keymap('n', "<C-j>", "<C-w>j", opts("Go to below window"))
keymap('n', "<C-k>", "<C-w>k", opts("Go to above window"))
keymap('n', "<C-l>", "<C-w>l", opts("Go to right window"))

keymap('n', "<esc>", "<cmd>nohlsearch<CR>", opts("Disable highlight after search"))

keymap('v', '<', "<gv", opts("Remove indent and stay in visual mode"))
keymap('v', '>', ">gv", opts("Add indent and stay in visual mode"))

keymap('v', 'J', ":m '>+1<CR>gv=gv", opts("Move visual blok(line) down"))
keymap('v', 'K', ":m '<-2<CR>gv=gv", opts("Move visual blok(line) up"))

keymap('v', '$', "g_", opts("Select to end of line without newline character"))
keymap('n', 'U', "<C-r>", opts("Redo"))

keymap('n', "<leader>]", "o<Esc>0\"_D", opts("Insert newline below and stay in normal mode")) -- conflict with tree
keymap('n', "<leader>[", "O<Esc>0\"_D", opts("Insert newline above and stay in normal mode"))


keymap('n', "<S-l>", "<cmd>bnext<CR>", opts("Go to next buffer"))
keymap('n', "<S-h>", "<cmd>bprevious<CR>", opts("Go to previous buffer"))
keymap('n', "<leader>bd", "<cmd>bd<CR>", opts("Close current buffer (tab)"))

keymap('n', "gl", '$', opts("Goto end of line"))
keymap('n', "gh", '^', opts("Goto first char in line"))

