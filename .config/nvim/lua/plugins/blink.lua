return {
  "saghen/blink.cmp"
  , build = { "cargo build --release" }
  , dependencies = {
    "xzbdmw/colorful-menu.nvim"
    , "nvim-mini/mini.icons"
  }
  , lazy = false
  , init = function()
    vim.o.winborder = "rounded"
  end
  , opts = {
    keymap = {
      preset = "super-tab"
      -- , ['<CR>'] = {
      --   function(cmp)
      --     if cmp.snippet_active() then return cmp.accept()
      --     else return cmp.select_and_accept() end
      --   end,
      --   'snippet_forward',
      --   'fallback'
      -- }
      , ['<C-CR>'] = { 'show', 'show_documentation', 'hide_documentation' }
    } -- :h blink-cmp-config-keymap
    , appearance = { nerd_font_variant = "normal" }
    , completion = {
      documentation = { auto_show = true }
      , menu = {
        draw = {
          components = {
            kind_icon = {
              text = function(ctx)
                local kind_icon, _, _ = require("mini.icons").get("lsp", ctx.kind)
                return kind_icon
              end
              , highlight = function(ctx)
                local _, hl, _ = require("mini.icons").get("lsp", ctx.kind)
                return hl
              end
            }
            , kind = {
              highlight = function(ctx)
                local _, hl, _ = require("mini.icons").get("lsp", ctx.kind)
                return hl
              end
            }
            , label = {
              width = { fill = true, max = 60 }
              , text = function(ctx)
                local highlight_info = require("colorful-menu").blink_highlights(ctx)
                if highlight_info ~= nil then
                  return highlight_info.label
                else
                  return ctx.label
                end
              end
              , highlight = function(ctx)
                local highlights = {}
                local highlight_info = require("colorful-menu").blink_highlights(ctx)
                if highlight_info ~= nil then
                  highlights = highlight_info.highlights
                end
                for _, idx in ipairs(ctx.label_matched_indices) do
                  table.insert(highlights, { idx, idx + 1, group = "BlinkCmpLabelMatch" })
                end
                return highlights
              end
            }
          }
          , columns = { {"kind_icon"}, { "label", gap = 1 } }
        }
      }
      , ghost_text = { enabled = true }
      , list = { selection = { auto_insert = false } }
    }
    , sources = {
      default = { "lsp", "path", "buffer" }
      , providers = {
        buffer = {
          opts = {
            get_bufnrs = function()
              return vim.tbl_filter(
                function(bufnr) return vim.bo[bufnr].buftype == '' end
                , vim.api.nvim_list_bufs()
              )
            end
          }
        }
        , path = {
          opts = {
            -- warn: check in work
            get_cwd = function(_)
              return vim.fn.getcwd()
            end
          }
        }
      }
    }
    , fuzzy = {
      implementation = "prefer_rust_with_warning"
      , sorts = { "exact", "score", "sort_text" }
    }
    , signature = {
      enabled = true
      , trigger = { enabled = false, show_on_trigger_character = false }
    }
    , cmdline = { completion = { menu = { auto_show = true } } }
  }
  , opts_extend = { "sources.default" } -- warn: what that is?
}
