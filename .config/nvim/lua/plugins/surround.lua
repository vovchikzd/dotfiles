local surround = {
  "kylechui/nvim-surround",
  version = "*",
  event = "VeryLazy",
  config = function()
      require("nvim-surround").setup({
      })
  end
}

--[[
    Old text                    Command         New text
--------------------------------------------------------------------------------
    surr*ound_words             ysiw)           (surround_words)
    *make strings               ys$"            "make strings"
    [delete ar*ound me!]        ds]             delete around me!
    remove <b>HTML t*ags</b>    dst             remove HTML tags
    'change quot*es'            cs'"            "change quotes"
    <b>or tag* types</b>        csth1<CR>       <h1>or tag types</h1>
    delete(functi*on calls)     dsf             function calls
]]


local miniSurround = {
  'echasnovski/mini.surround'
  , version = false
  , lazy = true
  , init = function()
    require('mini.surround').setup({
      -- Add custom surroundings to be used on top of builtin ones. For more
      -- information with examples, see `:h MiniSurround.config`.
      custom_surroundings = {
        ['('] = { output = { left = '(', right = ')' } },
        ['['] = { output = { left = '[', right = ']' } },
        ['{'] = { output = { left = '{', right = '}' } },
        ['<'] = { output = { left = '<', right = '>' } },
      },

      -- Duration (in ms) of highlight when calling `MiniSurround.highlight()`
      highlight_duration = 100,

      -- Module mappings. Use `''` (empty string) to disable one.
      mappings = {
        add = 'ma', -- Add surrounding in Normal and Visual modes
        delete = 'md', -- Delete surrounding
        find = 'mf', -- Find surrounding (to the right)
        find_left = 'mF', -- Find surrounding (to the left)
        highlight = 'mh', -- Highlight surrounding
        replace = 'mr', -- Replace surrounding
        update_n_lines = 'mn', -- Update `n_lines`

        suffix_last = 'l', -- Suffix to search with "prev" method
        suffix_next = 'n', -- Suffix to search with "next" method
      },

      -- Number of lines within which surrounding is searched
      n_lines = 20,

      -- Whether to respect selection type:
      -- - Place surroundings on separate lines in linewise mode.
      -- - Place surroundings on each line in blockwise mode.
      respect_selection_type = false,

      -- How to search for surrounding (first inside current line, then inside
      -- neighborhood). One of 'cover', 'cover_or_next', 'cover_or_prev',
      -- 'cover_or_nearest', 'next', 'prev', 'nearest'. For more details,
      -- see `:h MiniSurround.config`.
      search_method = 'cover',

      -- Whether to disable showing non-error feedback
      -- This also affects (purely informational) helper messages shown after
      -- idle time if user input is required.
      silent = false,
    })
  end
}

-- return surround
return miniSurround
