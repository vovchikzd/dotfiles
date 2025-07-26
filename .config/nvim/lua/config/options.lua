-- :help options

vim.opt.fileencoding = "utf-8"
vim.opt.colorcolumn = "81"
vim.opt.cursorline = true
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.expandtab = true
vim.opt.shiftwidth = 2
vim.opt.tabstop = 2
vim.opt.smartindent = true
vim.opt.scrolloff = 15
vim.opt.sidescrolloff = 8
vim.opt.mouse = ''
vim.opt.backup = false
vim.opt.cmdheight = 1
vim.opt.conceallevel = 0
vim.opt.hlsearch = true
vim.opt.ignorecase = true
vim.opt.smartcase = true
vim.opt.splitbelow = true
vim.opt.splitright = true
vim.opt.swapfile = false
vim.opt.undodir = (os.getenv("XDG_DATA_HOME") or (os.getenv("HOME") .. "/.local/share")) .. "/nvim_undo"
vim.opt.undofile = true
vim.opt.showtabline = 2
vim.opt.signcolumn = "yes"
vim.opt.wrap = false
vim.opt.showmode = false
vim.opt.shortmess:append 'c'
vim.opt.iskeyword:append { '-', '_' }
-- vim.opt.iskeyword:remove {'-', '_'}


vim.o.background = "dark"

vim.cmd [[cnoreabbrev q1 q!]]

-- don't add comment when insert new line from comment line
-- (sometimes this is unset while working, don't know why)
-- since vim.cmd [[set formatoptions-=cro]]
-- and vim.opt.formatoptions:remove {"c", "r", "o"}
-- don't work
vim.cmd([[autocmd BufEnter * set formatoptions-=cro]])
