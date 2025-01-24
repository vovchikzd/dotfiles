local opts = function(description)
  return { noremap = true, silent = true, desc = description}
end

local keymap = vim.keymap.set

keymap("", "<Space>", "<Nop>", opts("Space as leader key"))
vim.g.mapleader = " "
vim.g.maplocalleader = " "

keymap("n", "<leader>|", "<C-w>v", opts("Vertical split"))
keymap("n", "<leader>\\", "<C-w>s", opts("Horizontal split"))
keymap("n", "<leader>c", "<C-w>c", opts("Close split"))

keymap("n", "<C-h>", "<C-w>h", opts("Go to left window"))
keymap("n", "<C-j>", "<C-w>j", opts("Go to below window"))
keymap("n", "<C-k>", "<C-w>k", opts("Go to above window"))
keymap("n", "<C-l>", "<C-w>l", opts("Go to right window"))

keymap("n", "<esc>", "<cmd>nohlsearch<CR>", opts("Disable highlight after search"))

keymap("v", "<", "<gv", opts("Remove indent and stay in visual mode"))
keymap("v", ">", ">gv", opts("Add indent and stay in visual mode"))

keymap("v", "J", ":m '>+1<CR>gv=gv", opts("Move visual blok(line) down"))
keymap("v", "K", ":m '<-2<CR>gv=gv", opts("Move visual blok(line) up"))

keymap("v", "$", "g_", opts("Select to end of line without newline character"))
keymap("n", "U", "<C-r>", opts("Redo"))

-- insert new line above/below without insert mode
keymap("n", "<leader>o", 'o<Esc>0"_D', opts("Insert newline below and stay in normal mode")) -- conflict with tree
keymap("n", "<leader>O", 'O<Esc>0"_D', opts("Insert newline above and stay in normal mode"))

keymap("t", "<Esc>", "<C-\\><C-n>", opts("Go to normal mode from terminal mode"))
keymap("n", "tt", "<cmd>terminal<CR>", opts("Go to terminal mode"))
keymap("n", "<leader>e", "<cmd>bd!<CR>", opts("\"Kill\" current buffer"))

keymap("n", "<C-M-l>", ":w | !clang-format -i --style=file:/home/vovchik/dotfiles/clang-format %<CR><CR>", opts("Save file and format it with clang-format (c and c++ only)"))

keymap("n", "zz", "ZZ", opts("Bind lower case alternative for ZZ (same as ':x')"))
keymap("n", "zq", "ZQ", opts("Bind lower case alternative for ZQ (same as ':q!')"))
keymap("n", "zs", ":w<CR>", opts("Save current buffer"))
keymap("n", "za", ":qa<CR>", opts("Close all windows"))
