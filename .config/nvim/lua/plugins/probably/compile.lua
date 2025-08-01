return {
  "ej-shafran/compile-mode.nvim"
  , dependencies = {
    "nvim-lua/plenary.nvim"
    , { "m00qek/baleia.nvim", tag = "v1.3.0" }
  }
  , init = function ()
    vim.g.compile_mode = {
      baleia_setup = true
    }
  end
}
