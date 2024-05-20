local opts = { noremap = true, silent = true}

-- short function name
-- local keymap = vim.api.nvim_set_keymap
local keymap = vim.keymap.set

-- space as leader key
keymap("", "<Space>", "<Nop>", opts)
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- split window
keymap("n", "<leader>|", "<C-w>v", opts)
keymap("n", "<leader>\\", "<C-w>s", opts)

-- window navigation on "Ctrl-<vim key>"
keymap("n", "<C-h>", "<C-w>h", opts)
keymap("n", "<C-j>", "<C-w>j", opts)
keymap("n", "<C-k>", "<C-w>k", opts)
keymap("n", "<C-l>", "<C-w>l", opts)

-- resize with arrows
-- keymap("n", "<C-Up>", ":resize +2<CR>", opts)
-- keymap("n", "<C-Down>", ":resize -2<CR>", opts)
-- keymap("n", "<C-Left>", ":vertical resize -2<CR>", opts)
-- keymap("n", "<C-Right>", ":vertical resize +2<CR>", opts)

-- hide highlight aflet search
keymap("n", "<esc>", "<cmd>nohlsearch<CR>", opts)

-- stay in indent mode
keymap("v", "<", "<gv", opts)
keymap("v", ">", ">gv", opts)

-- move visual block up and down
keymap("v", "J", "<cmd>m '>+1<CR>gv=gv", opts)
keymap("v", "K", "<cmd>m '<-2<CR>gv=gv", opts)

-- select to end of line without newline character
keymap("v", "$", "g_", opts)
keymap("n", "U", "<C-r>", opts)

-- insert new line above/below without insert mode
keymap("n", "<leader>o", "o<esc>", opts) -- conflict with tree
keymap("n", "<leader>O", "O<esc>", opts)

-- Telescope keys
keymap("n", "<leader>ff", "<cmd>Telescope find_files<CR>", opts)
keymap("n", "<leader>fg", "<cmd>Telescope live_grep<CR>", opts)
keymap("n", "<C-_>",      "<cmd>Telescope current_buffer_fuzzy_find sorting_strategy=ascending prompt_position=top<CR>", opts)
keymap("n", "<leader>fe", "<cmd>Telescope diagnostics sorting_strategy=ascending prompt_position=top<CR>", opts)
keymap("n", "<leader>fb", "<cmd>Telescope buffers<CR>", opts)
keymap("n", "<leader>gf", "<cmd>Telescope git_files<CR>", opts)
keymap("n", "<leader>fk", "<cmd>Telescope keymaps<CR>", opts)
