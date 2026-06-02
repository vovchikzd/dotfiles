return {
  "okuuva/auto-save.nvim"
  , version = '*'
  , cmd = "ASToggle"
  , event = { "InsertLeave", "TextChanged" }
  , opts = {
    trigger_events = {
      immediate_save = {
        "BufLeave"
        , "FocusLost"
        , "QuitPre"
        , "VimSuspend"
        , "InsertLeave"
        , "TextChanged"
      }
      , defer_save = {}
    }
  }
}
