return {
  "akinsho/bufferline.nvim"
  , config = function()
    local status_ok, bufferline = pcall(require, "bufferline")
    if not status_ok then return end
    bufferline.setup()
  end
}
