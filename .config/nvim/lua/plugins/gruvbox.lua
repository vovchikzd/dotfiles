return {
  "sainnhe/gruvbox-material"
  , priority = 1000
  , config = function()
    vim.g.gruvbox_material_background = "medium" -- "sort", "medium", "hard"
    vim.g.gruvbox_material_foreground = "material" -- "material", "mix", "original"
    vim.g.gruvbox_material_enable_italic = true
    vim.g.gruvbox_material_transparent_background = 0
    vim.g.gruvbox_material_dim_inactive_windows = 0
    -- "grey background", "green background", "blue background", "red background", "reverse"
    vim.g.gruvbox_material_visual = "reverse"
    -- "grey", "red", "orange", "yellow", "green", "aqua", "blue", "purple"
    vim.g.gruvbox_material_menu_selection_background = "grey"
    -- "none", "gray"
    vim.g.gruvbox_material_sign_column_background = "none"
    vim.g.gruvbox_material_ui_contrast = "high" -- "low", "high"
    vim.g.gruvbox_material_show_eob = 0
    vim.g.gruvbox_material_diagnostic_virtual_text = "colored" -- "grey", "colored", "highlighted"
    -- "grey background", "high contrast background", "bold", "underline", "italic"
    vim.g.gruvbox_material_current_word = "underline"
    vim.cmd.colorscheme("gruvbox-material")
  end
}
