local keymap = vim.keymap.set

local key_opts = function(description)
  return {noremap = true, silent = true, buffer = 0, desc = description}
end

local on_attach_default_keymaps = function()
  keymap("n", "K", vim.lsp.buf.hover, key_opts("Open information about thing under cursor"))
  keymap("n", "<leader>r", vim.lsp.buf.rename, key_opts("Remane all uses of the name under cursor"))
  keymap("n", "gd", vim.lsp.buf.definition, key_opts("Go to definition of thing under cursor"))
  keymap("n", "<leader>tt", "<cmd>lua vim.diagnostic.enable(not vim.diagnostic.is_enabled())<CR>", key_opts("Toggle diagnostic visibility"))
end

local clangd_setup = function()
  if vim.fn.executable("clangd") == 1 then
    require("lspconfig").clangd.setup({
      filetypes = {"c", "h", "cc", "cpp", "hh", "hpp", "cxx", "H", "C", "cppm",
                   "cp", "CPP", "c++", "hp", "hxx", "HPP", "h++"},
      on_attach = function()
        vim.diagnostic.enable(false)
        on_attach_default_keymaps()
        keymap("n", "<leader>gd", vim.lsp.buf.declaration , key_opts("Go to declaration of thing under cursor"))
      end,
    })
  end
end

local rust_analyzer_setup = function()
  if vim.fn.executable("rust-analyzer") == 1 then
    require("lspconfig").rust_analyzer.setup({
      on_attach = function()
        on_attach_default_keymaps()
      end
    })
  end
end

local lua_ls_setup = function()
  if vim.fn.executable("lua-language-server") == 1 then
    require("lspconfig").lua_ls.setup({
      on_attach = function()
        on_attach_default_keymaps()
      end
    })
  end
end

local pyright_setup = function()
  if vim.fn.executable("pyright-langserver") == 1 then
    require("lspconfig").pyright.setup({
      on_attach = function()
        on_attach_default_keymaps()
      end
    })
  end
end

local lsp = {
  "neovim/nvim-lspconfig",
  dependencies = {},
  config = function()
    clangd_setup()
    rust_analyzer_setup()
    lua_ls_setup()
    pyright_setup()
  end
}

return lsp
