local servers = {
  clangd = {
    filetypes = {"c", "h", "cc", "cpp", "hh", "hpp", "cxx", "H", "C", "cppm",
                  "cp", "CPP", "c++", "hp", "hxx", "HPP", "h++"}
    , cmd = { "clangd",  "--background-index", "--clang-tidy", "--experimental-modules-support"
              , "--background-index-priority=normal", "--fallback-style=Google"
              , "--header-insertion=never", "--pch-storage=memory" }
  }
  , zls = {}
  , rust_analyzer = {}
  , lua_ls = {}
  , pyright = {}
  , neocmake = {}
  , tinymist = {}
  , fish_lsp = {}
  , bashls = {}
}

return {
  "neovim/nvim-lspconfig"
  , ft = { "cpp", "c", "lua", "python", "rust", "zig", "cmake", "typst", "fish", "bash", "sh" }
  , cmd = { "LspInfo" }
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
}
