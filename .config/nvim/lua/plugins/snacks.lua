local getGitRoot = function()
  local root, _ = string.gsub(
    vim.system({ "git", "-C", vim.fn.expand("%:p:h"), "rev-parse", "--show-toplevel" }):wait().stdout
    , "\n", ""
  )
  return root
end

local files = function()
  local git_root = getGitRoot()
  if git_root and git_root ~= '' then
    Snacks.picker.git_files()
  else
    Snacks.picker.files({ hidden = true })
  end
end

local grep = function()
  local git_root = getGitRoot()
  if git_root and git_root ~= '' then
    Snacks.picker.grep({ dirs = { git_root }, hidden = true, ignored = true })
  else
    Snacks.picker.grep({ hidden = true, ignored = true })
  end
end

local explorer = function()
  local current_file = vim.fn.expand("%:p")
  local res, ind = string.find(current_file, "/.", 1, true)
  if res then
    Snacks.explorer.open({ hidden = true })
  else
    Snacks.explorer.open()
  end
end


return {
  "folke/snacks.nvim"
  , priority = 1000
  , lazy = false
  , opts = {
    indent = { animate = { enabled = false } }
    , scope = { enabled = true }
    , scroll = { enabled = false }
    , explorer = {}

    , image = { convert = { notify = false } }
    , picker = {
      matcher = { sort_empty = true, frecency = true }
      , formatters = { file = { filename_first = true } }
      , previewers = { man_pager = "nvim -c Man!" }
    }
  }
  , keys = {
    { "<leader><space>", function() files() end, desc = "Find Files" }
    , {"<C-/>", function() Snacks.picker.grep({ dirs = { vim.fn.expand("%:p") }}) end, desc = "Grep Current File (Buffer)"}
    , {"<leader>f", function() grep() end, desc = "Grep Files"}

    , {"<leader>e", function() explorer() end, desc = "File Explorer"}
  }
}
