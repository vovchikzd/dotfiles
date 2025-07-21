improvedft = {
  "backdround/improved-ft.nvim"
  , opts = {
    -- Maps default f/F/t/T/;/, keys.
    -- default: false
    use_default_mappings = true,

    -- Ignores case of the given characters.
    -- default: false
    ignore_char_case = true,

    -- Takes a last hop direction into account during repetition hops
    -- default: false
    use_relative_repetition = true,

    -- Uses direction-relative offsets during repetition hops.
    -- default: false
    use_relative_repetition_offsets = true,
  }
}

return improvedft
