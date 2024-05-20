-- :help options

vim.opt.colorcolumn = '81'                    -- Highlighted column on 80 symbols
vim.opt.cursorline = true                     -- Highlight the text line of the cursor
vim.opt.number = true                         -- Print the line number in front of each line
vim.opt.relativenumber = true                 -- changes the displayed number to be relative

vim.opt.expandtab = true                      -- use spaces instead of tabs
vim.opt.shiftwidth = 2                        -- shift 2 spaces when tab
vim.opt.tabstop = 2                           -- 1 tab == 2 spaces
vim.opt.smartindent = true                    -- autoindent new lines

vim.opt.scrolloff = 8                         -- minimal number of screen lines to keep above and below the cursor
vim.opt.sidescrolloff = 8                     -- as above but colums

-- don't sure I need it
vim.opt.backup = false                        -- create a backup file
-- vim.opt.clipboard = "unnamedplus"             -- access the system clipboard
vim.opt.cmdheight = 1                         -- more space in the neovim command line
vim.opt.completeopt = {"menuone", "noselect"} -- list of options for insert
vim.opt.conceallevel = 0                      -- determine how text with the "conceal" syntax attribute
vim.opt.fileencoding = "utf-8"                -- the encoding written to a fiel
vim.opt.hlsearch = true                       -- highlight all matches on previous search pattern
vim.opt.ignorecase = true                     -- ignore case in search
vim.opt.mouse = "a"                           -- allow mouse to be used in neovim
-- vim.opt.pumheight = 10                        -- pop up menu height
-- vim.opt.showmode = false                      -- don't show -- INSERT -- and etc.
vim.opt.showtabline = 2                       -- always show tabs
vim.opt.smartcase = true                      -- override the 'ignorecase' if the search contains upper case
vim.opt.splitbelow = true                     -- all horizontal splits to go below
vim.opt.splitright = true                     -- all vertical splits to go right
vim.opt.swapfile = false                      -- creates a swap file
-- vim.opt.termguicolors = true               -- set term gui colors
vim.opt.timeoutlen = 1000                     -- time in milliseconds to wait for a mapped sequence to complete
vim.opt.undofile = false                      -- enable persistent undo
vim.opt.updatetime = 300                      -- faster completion
vim.opt.writebackup = false                   -- if a file was edited by another program
-- vim.opt.numberwidth = 4                    -- set number column width
vim.opt.signcolumn = "yes"                    -- always show the sign column
vim.opt.wrap = false                          -- display lines as one long line
vim.opt.guifont = "monospace:h17"             --the font used in graphical neovim application

vim.opt.shortmess:append "c"

-- vim.cmd "set whichwrap+=<,>,[,],h,l"
vim.cmd [[set iskeyword+=-]]

-- since vim.cmd [[set formatoptions-=cro]]
-- and vim.opt.formatoptions:remove {"c", "r", "o"}
-- don't work
vim.cmd([[autocmd BufEnter * set formatoptions-=cro]])
