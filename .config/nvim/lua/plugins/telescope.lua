local create_keymaps = function()
  local keymap = vim.keymap.set
  local key_opts = function(description)
    return { noremap = true, silent = true, desc = description }
  end
  keymap("n", "<leader>ff", require("telescope.builtin").find_files, key_opts("Find files in directory"))
  keymap("n", "<C-_>",      "<cmd>Telescope current_buffer_fuzzy_find sorting_strategy=ascending prompt_position=top<CR>", key_opts("Grep current file"))
  keymap("n", "<leader>fe", "<cmd>Telescope diagnostics sorting_strategy=ascending prompt_position=top<CR>", key_opts("See errors/warnings in current file"))
  keymap("n", "<leader>fb", require("telescope.builtin").buffers, key_opts("Find open buffers"))
  keymap("n", "<leader>gf", require("telescope.builtin").git_files, key_opts("Find git files"))
  keymap("n", "<leader>fk", require("telescope.builtin").keymaps, key_opts("Find keymaps"))

  function local_live_grep()
    local git_dir = vim.fn.system(string.format("git -C %s rev-parse --show-toplevel", vim.fn.expand("%:p:h")))
    git_dir = string.gsub(git_dir, "\n", "") -- remove newline character from git_dir
    local opts = {
      cwd = git_dir,
      file_ignore_patterns = { ".git" },
      additional_args = { "--hidden" }
    }
    require('telescope.builtin').live_grep(opts)
  end
  keymap("n", "<leader>gg", "<cmd>lua local_live_grep()<CR>", key_opts("Grep files from git root"))
end

local telescope = {
  "nvim-telescope/telescope.nvim",
  dependencies = {
    "nvim-lua/plenary.nvim",
    {"nvim-telescope/telescope-fzf-native.nvim",
     build = "make"},
  },
  config = function()
    require("telescope").setup({
      extensions = {
        fzf = {
          fuzzy = true,                    -- false will only do exact matching
          override_generic_sorter = true,  -- override the generic sorter
          override_file_sorter = true,     -- override the file sorter
          case_mode = "smart_case",        -- or "ignore_case" or "respect_case"
                                           -- the default case_mode is "smart_case"
        },
      },
    })
    require("telescope").load_extension("fzf")
    create_keymaps()
  end
}

return telescope
