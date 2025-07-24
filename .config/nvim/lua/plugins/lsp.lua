local clangd = "clangd"
local servers = {
  [1] = clangd
  , [2] = "zls"
  , [3] = "rust_analyzer"
  , [4] = "lua_ls"
  , [5] = "pyright"
}

local configs = {
  [clangd] = {
    filetypes = {"c", "h", "cc", "cpp", "hh", "hpp", "cxx", "H", "C", "cppm",
                  "cp", "CPP", "c++", "hp", "hxx", "HPP", "h++"}
  }
}

return {
  "neovim/nvim-lspconfig"
  , ft = { "cpp", "c", "lua", "python", "rust", "zig" }
  , init = function()
    vim.diagnostic.config({ virtual_text = { current_line = true }})
  end
  , config = function()
    for _, server in ipairs(servers) do
      vim.lsp.enable(server)
      local config = configs[server]
      if config then
        vim.lsp.config(server, config)
      end
    end
  end
}
