-- TODO: Toggle virtual text on warnings and errors, make autocomplete

local vim = vim -- because of lsw warnings
local keymap = vim.keymap.set

local key_opts = function(description)
  return {noremap = true, silent = true, buffer = 0, desc = description}
end

local on_attach_default = function()
  keymap("n", "K", vim.lsp.buf.hover, key_opts("Open information about thing under cursor"))
  keymap("n", "<leader>r", vim.lsp.buf.rename, key_opts("Remane all uses of the name under cursor"))
  keymap("n", "gd", vim.lsp.buf.definition, key_opts("Go to definition of thing under cursor"))
end

local toggle_text = function()
  vim.lsp.handlers["textDocument/publishDiagnostics"] = vim.lsp.with(
    vim.lsp.diagnostic.on_publish_diagnostics, {
      -- disable virtual text
      virtual_text = false,
      -- show signs
      signs = true,
      -- delay update diagnostics
      update_in_insert = false,
    }
  )
end

local clangd_setup = {
  filetypes = {"c", "h", "cc", "cpp", "hh", "hpp", "cxx", "H", "C", "cppm",
               "cp", "CPP", "c++", "hp", "hxx", "HPP", "h++"},
  on_attach = function()
    toggle_text()
    on_attach_default()
    keymap("n", "<leader>gd", vim.lsp.buf.declaration , key_opts("Go to declaration of thing under cursor"))
  end,
}

local lua_ls_setup = {
  on_attach = function()
    on_attach_default()
  end
}

local rust_analyzer_setup = {
  on_attach = function()
    on_attach_default()
  end
}

local pyright_setup = {
  on_attach = function()
    on_attach_default()
  end
}

local lsp = {
  "neovim/nvim-lspconfig",
  dependencies = {},
  config = function()
    require("lspconfig").pyright.setup(pyright_setup)
    require("lspconfig").lua_ls.setup(lua_ls_setup)
    require("lspconfig").rust_analyzer.setup(rust_analyzer_setup)
    require("lspconfig").clangd.setup(clangd_setup)
  end
}

return lsp
