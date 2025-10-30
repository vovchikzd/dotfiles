local servers = {
  clangd = {
    filetypes = {"c", "h", "cc", "cpp", "hh", "hpp", "cxx", "H", "C", "cppm",
                  "cp", "CPP", "c++", "hp", "hxx", "HPP", "h++"}
    , cmd = { "clangd",  "--background-index", "--fallback-style=Google"
              , "--background-index-priority=normal", "--pch-storage=memory"
              , "--header-insertion=never", "--function-arg-placeholders=0" }
  }
  , zls = {
    settings = {
      enable_build_on_save = true
      , enable_argument_placeholders = false
      , highlight_global_var_declarations = true
    }
  }
  , rust_analyzer = {}
  , lua_ls = {}
  , pyright = {}
  , neocmake = {}
  , tinymist = {}
  , bashls = {}
}

return {
  "neovim/nvim-lspconfig"
  , ft = { "cpp", "c", "lua", "python", "rust", "zig", "cmake", "typst", "fish", "bash", "sh" }
  , cmd = { "LspInfo", "LspStart" }
  , init = function()
    vim.diagnostic.config({ virtual_text = { current_line = true }})
  end
  , config = function()
    for server, config in pairs(servers) do
      vim.lsp.enable(server)
      if config and next(config) ~= nil then
        vim.lsp.config(server, config)
      end
    end
  end
  , keys = {
    { "<leader>lr", vim.lsp.buf.rename, desc = "Rename symbol" }
    , { "<leader>lf", vim.diagnostic.open_float, desc = "Open diagnostic message in new window" }
  }
}
