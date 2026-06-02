return {
  "folke/todo-comments.nvim"
  , dependencies = { "nvim-lua/plenary.nvim" }
  , opts = {
    keywords = {
      FIX = { alt = { "fix", "FIXME", "fixme", "BUG", "bug", "FIXIT", "fixit",
        "ISSUE", "issue", "ERROR", "error", "UB", "ub"
      }}
      , TODO = { alt = { "todo", "LATER", "later" } }
      , HACK = { alt = { "hack", "CRUTCH", "crutch" } }
      , WARN = { alt = { "warn", "WARNING", "warning" } }
      , PERF = { alt = { "perf", "OPTIM", "optim", "PERFOMANCE", "perfomance",
        "OPTIMIZE", "optimize"
      }}
      , NOTE = { alt = { "note", "INFO", "info" } }
      , TEST = { alt = { "test", "TESTING", "testing", "PASSED", "passed",
        "FAILED", "failed"
      }}
    }
    , colors = {
      error = { "DiagnosticError", "ErrorMsg", "#DC2626" },
      warning = { "DiagnosticWarn", "WarningMsg", "#FBBF24" },
      info = { "DiagnosticInfo", "#2563EB" },
      hint = { "DiagnosticHint", "#10B981" },
      default = { "Identifier", "#7C3AED" },
      test = { "Identifier", "#FF00FF" }
    }
  }
}
