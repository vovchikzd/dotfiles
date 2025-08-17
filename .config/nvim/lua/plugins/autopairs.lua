return {
  "windwp/nvim-autopairs"
  , event = "InsertEnter"
  , config = function()
    local Rule = require("nvim-autopairs.rule")
    local cond = require("nvim-autopairs.conds")
    local npairs = require("nvim-autopairs")
    npairs.setup({})

    npairs.add_rules({
      Rule('|', '|', "zig")
        :with_pair(cond.before_text(" catch "))
        :with_move(cond.done())
        :with_del(cond.done())
        :with_cr(cond.none())
      , Rule('|', '|', "zig")
        :with_pair(cond.before_text(") "))
        :with_move(cond.done())
        :with_del(cond.done())
        :with_cr(cond.none())
    })

  end
}
