return {
  "nvim-telescope/telescope.nvim"
  , lazy = false
  , version = '*'
  , dependencies = {
    { "nvim-telescope/telescope-fzf-native.nvim", build = "make" }
  }
  , config = function()
    local tls = require("telescope")

    tls.setup({
      defaults = {
        mappings = {} -- ignore all defaults keymaps
        , sorting_strategy = "ascending"
        , layout_strategy = "vertical"
        , layout_config = {
          mirror = true
          , prompt_position = "top"
        }
      }

      , pickers = {
        live_grep = {
          additional_args = { "--hidden", "--no-ignore" }
          , glob_pattern = { "!**/.git/*", "!**/zig-pkg/*", "!**/zig-out/*", "!**/.zig-cache/*" }
        }
      }

      , extensions = {
        fzf = {
          fuzzy = true -- exact matching or not
          , override_generic_sorter = true
          , override_file_sorter = true
          , case_mode = "smart_case" -- "ignore_case", "respect_case"
        }
      }
    })

    tls.load_extension("fzf")

    local key_opts = function(description)
      return { noremap = true, silent = true, desc = description }
    end
    local keymap = vim.keymap.set
    local pck = require("telescope.builtin")

    local grep_current_buffer = function()
      pck.live_grep({ prompt_title = "Grep Current Buffer", search_dirs = { vim.fn.expand("%:p") } })
    end
    keymap({ 'n', 'v' }, '<C-/>', grep_current_buffer, key_opts("Grep current buffer"))

    local get_git_root = function()
      local root, _ = string.gsub(
        vim.system({ "git", "-C", vim.fn.expand("%:p:h"), "rev-parse", "--show-toplevel" }):wait().stdout
        , "\n", ""
      )
      return root
    end

    local grep_git_root_cwd_fallback = function()
      local git_root = get_git_root()
      local opts = {}
      if git_root and git_root ~= '' then
        opts = { cwd = git_root, prompt_title = "Grep Project Files" }
      else
        opts = { prompt_title = "Grep Files" }
      end
      pck.live_grep(opts)
    end
    keymap({ 'n', 'v' }, "<leader><Space>", grep_git_root_cwd_fallback, key_opts("Grep files"))


    local find_files_git_root_cwd_fallback = function()
      local git_root = get_git_root()
      local opts = { prompt_title = "Find Files" }
      if git_root and git_root ~= '' then
        opts.show_untracked = true
        pck.git_files(opts)
      else
        opts.hidden = true
        pck.find_files(opts)
      end
    end
    keymap({ 'n', 'v' }, "<leader>.", find_files_git_root_cwd_fallback, key_opts("Find files"))
  end
}
