return {
  "nvim-lualine/lualine.nvim"
  , dependencies = { "echasnovski/mini.icons" }
  , opts = {
    sections = {
      lualine_a = {}
      , lualine_b = {}
      , lualine_c = { "lsp_status", "filename", "navic" }

      , lualine_x = { "encoding", "fileformat", "filetype" }
      , lualine_y = { "branch", "diff", "diagnostics" }
      , lualine_z = { "mode" }
    }
  }
}
