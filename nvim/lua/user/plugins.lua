local fn = vim.fn

-- automatically install packer
local install_path = fn.stdpath("data").."/site/pack/packer/start/packer.nvim"
if fn.empty(fn.glob(install_path)) > 0 then
    PACKER_BOOTSTRAP = fn.system {
        "git",
        "clone",
        "--depth",
        "1",
        "https://github.com/wbthomason/packer.nvim",
        install_path,
    }
    print "Installing packer, close and reopen Neovim..."
    vim.cmd [[packadd packer.nvim]]
end

-- autocommand that reloads noevim whenever you save the plugins.lua file
vim.cmd [[
    augroup packer_user_config
        autocmd!
        autocmd BufWritePost plugins.lua source <afile> | PackerSync
    augroup end
]]

-- use a protected call so we don't error out on first use
local status_ok, packer = pcall(require, "packer")
if not status_ok then
    return
end

-- have packer use a popup window
packer.init {
    display = {
        open_fn = function()
            return require("packer.util").float { border = "rounded" }
        end,
    },
}

-- install your plugins here
return packer.startup(function(use)
    -- don't touch this
    use "wbthomason/packer.nvim" -- packer manage itself
    use "nvim-lua/popup.nvim" -- implementation of the Popup API from vim in Neovim
    use "nvim-lua/plenary.nvim" -- useful lua functions used by lots of plugins

    -- put plugins here
    --[[ use "ellisonleao/gruvbox.nvim" -- gruvbox colorscheme ]]
    use "Mofiqul/dracula.nvim"

    -- highlight syntax
    use "nvim-treesitter/nvim-treesitter"
    use "p00f/nvim-ts-rainbow"

    use "lewis6991/gitsigns.nvim" -- git plugin

    -- lualine
    use 'nvim-lualine/lualine.nvim'
    use 'nvim-tree/nvim-web-devicons'

    --autopairs
    -- use {"windwp/nvim-autopairs",
    --       config = function()
    --       require("nvim-autopairs").setup {} end
    -- }

    -- autocomment plugin
    use "JoosepAlviste/nvim-ts-context-commentstring"
    use 'numToStr/Comment.nvim'

    -- tree
    use "nvim-tree/nvim-tree.lua"

    -- start page
    use "goolord/alpha-nvim"

    --bufferline
    use "akinsho/bufferline.nvim"


    -- automatically set up your congifuration after cloning packer.nvim
    -- this sould be at the end after all plugins
    if PACKER_BOOTSTRAP then
        require("packer").sync()
    end
end)
