local opts = { noremap = true, silent = true}

-- local term_opts = { silent = true }

-- short function name
local keymap = vim.api.nvim_set_keymap

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

-- open file explorer in left side on "Space-e"
keymap("n", "<leader>e", ":NvimTreeToggle<cr>", opts)
keymap("n", "<leader>o", ":NvimTreeFocus<cr>", opts)

-- resize with arrows
keymap("n", "<C-Up>", ":resize +2<CR>", opts)
keymap("n", "<C-Down>", ":resize -2<CR>", opts)
keymap("n", "<C-Left>", ":vertical resize -2<CR>", opts)
keymap("n", "<C-Right>", ":vertical resize +2<CR>", opts)

-- navigate buffers on "Shift-<vim key>"
keymap("n", "<S-l>", ":bnext<CR>", opts)
keymap("n", "<S-h>", ":bprevious<CR>", opts)

-- hide highlight aflet search
keymap("n", "<A-l>", ":nohlsearch<CR>", opts)

-- stay in indent mode
keymap("v", "<", "<gv", opts)
keymap("v", ">", ">gv", opts)

-- move text line up and down A = Alt
keymap("v", "<A-j>", ":m .+1<CR>==", opts)
keymap("v", "<A-k>", ":m .-2<CR>==", opts)
keymap("v", "p", '"_dP', opts) -- one of the most important

-- move visual block up and down
keymap("x", "J", ":move '>+1<CR>gv-gv", opts)
keymap("x", "K", ":move '<-2<CR>gv-gv", opts)
keymap("x", "<A-j>", ":move '>+1<CR>gv-gv", opts)
keymap("x", "<A-k>", ":move '<-2<CR>gv-gv", opts)

-- telescope keymaps
keymap("n", "<leader>f", "<cmd>Telescope find_files hidden=true<cr>", opts)
keymap("n", "<leader>g", "<cmd>Telescope live_grep<cr>", opts)

-- git keymaps
keymap("n", "<leader>j", ":Gitsigns next_hunk<cr>", opts)
keymap("n", "<leader>k", ":Gitsigns prev_hunk<cr>", opts)
keymap("n", "<leader>h", ":Gitsigns preview_hunk<cr>", opts)
keymap("n", "<leader>b", ":Gitsigns blame_line<cr>", opts)

-- for tabs (buffers)
keymap("n", "<leader>d", "<cmd>bdelete<CR>", opts)
