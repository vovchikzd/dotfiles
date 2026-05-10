return {
  "ej-shafran/compile-mode.nvim"
  , dependencies = {
    "nvim-lua/plenary.nvim"
    , { "m00qek/baleia.nvim", tag = "v1.3.0" }
  }
  , config = function ()
    vim.g.compile_mode = {
      input_word_completion = true
      , baleia_setup = true
      , error_threshhold = require("compile-mode").level.ERROR
      , auto_jump_to_first_error = true
      , time_format = "%d.%m.%Y %H:%M:%S"
      , focus_compilation_buffer = true
      , bang_expansion = true
    }
  end
}
