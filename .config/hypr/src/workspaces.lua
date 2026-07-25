-- see https://wiki.hypr.land/Configuring/Basics/Workspace-Rules

for w = 1, 10 do
  hl.workspace_rule({ workspace = tostring(w), monitor = "DP-2"})
  hl.workspace_rule({ workspace = tostring(w+10), monitor = "DP-3"})
end
