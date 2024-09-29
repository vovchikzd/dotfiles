local keymap = vim.keymap.set

-- Capabilities for lspconfig from autocomplete
local capabilities = require("cmp_nvim_lsp").default_capabilities()

local key_opts = function(description)
  return {noremap = true, silent = true, buffer = 0, desc = description}
end

local on_attach_default = function()
  vim.lsp.handlers["textDocument/hover"] = vim.lsp.with(vim.lsp.handlers.hover, {
  border = "rounded",
  })
  keymap("n", "K", vim.lsp.buf.hover, key_opts("Open information about thing under cursor"))
  keymap("n", "<leader>r", vim.lsp.buf.rename, key_opts("Remane all uses of the name under cursor"))
  keymap("n", "gd", vim.lsp.buf.definition, key_opts("Go to definition of thing under cursor"))
  keymap("n", "<leader>tt", "<cmd>lua vim.diagnostic.enable(not vim.diagnostic.is_enabled())<CR>", key_opts("Toggle diagnostic visibility"))
  keymap("n", "<leader>en", "<cmd>lua vim.diagnostic.goto_next({ float = { border = 'rounded' }})<CR>", key_opts("Goto next error/warning"))
  keymap("n", "<leader>ep", "<cmd>lua vim.diagnostic.goto_prev({ float = { border = 'rounded' }})<CR>", key_opts("Goto previous error/warning"))
end

local clangd_setup = function()
  if vim.fn.executable("clangd") == 1 then
    require("lspconfig").clangd.setup({
      autostart = true,
      filetypes = {"c", "h", "cc", "cpp", "hh", "hpp", "cxx", "H", "C", "cppm",
                   "cp", "CPP", "c++", "hp", "hxx", "HPP", "h++"},
      capabilities = capabilities,
      on_attach = function()
        vim.diagnostic.enable(false)
        on_attach_default()
        keymap("n", "<leader>gd", vim.lsp.buf.declaration , key_opts("Go to declaration of thing under cursor"))
      end,
    })
  end
end

local rust_analyzer_setup = function()
  if vim.fn.executable("rust-analyzer") == 1 then
    require("lspconfig").rust_analyzer.setup({
      capabilities = capabilities,
      on_attach = function()
        on_attach_default()
      end
    })
  end
end

local lua_ls_setup = function()
  if vim.fn.executable("lua-language-server") == 1 then
    require("lspconfig").lua_ls.setup({
      capabilities = capabilities,
      on_attach = function()
        on_attach_default()
      end
    })
  end
end

local pyright_setup = function()
  if vim.fn.executable("pyright-langserver") == 1 then
    require("lspconfig").pyright.setup({
      capabilities = capabilities,
      on_attach = function()
        on_attach_default()
      end
    })
  end
end

local neocmakelsp_setup = function()
  if vim.fn.executable("neocmakelsp") == 1 then
    local lspconfig = require("lspconfig")
    lspconfig.neocmake.setup({
      capabilities = capabilities,
      on_attach = function()
        on_attach_default()
      end,
      cmd = {"neocmakelsp", "--stdio"},
      filetypes = {"cmake"},
      root_dir = function(fname)
        return lspconfig.util.find_git_ancestor(fname)
      end,
      single_file_support = true,
      init_options = {
        format = {enable = true},
        lint = {enable = true},
        scan_cmake_in_package = true,
      }
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
    neocmakelsp_setup()
  end
}

return lsp
