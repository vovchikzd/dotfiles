---------------------
---- KEYBINDINGS ----
---------------------

-- see https://wiki.hypr.land/Configuring/Basics/Binds/
local bind = hl.bind
local exec = hl.dsp.exec_cmd

local mainMod = "SUPER"

bind(mainMod .. " + Return", exec(Ghostty))
bind(mainMod .. " + C", hl.dsp.window.close())
bind(mainMod .. " + SHIFT + M", hl.dsp.exit())
bind(mainMod .. " + F", hl.dsp.window.float({ action = "toggle" }))
bind("ALT + Space", exec(Menu))
bind(mainMod .. " + P", hl.dsp.window.pin({ action = "toggle" }))
bind(mainMod .. " + B", exec("firefox"))
bind(mainMod .. " + V", exec("ghostty --class=clipse -e clipse", { float = true, size = { 622, 652 }, stay_focused = true, move = { 1286, 417 } }))
bind("Print", exec("flameshot gui"))
bind(mainMod .. " + comma", hl.dsp.focus({ monitor = "+1"}))
bind(mainMod .. " + SHIFT + c", hl.dsp.window.center())
bind(mainMod .. " + SHIFT + f", hl.dsp.window.fullscreen())

bind(mainMod .. " + h", hl.dsp.focus({ direction = "l" }))
bind(mainMod .. " + l", hl.dsp.focus({ direction = "r" }))
bind(mainMod .. " + k", hl.dsp.focus({ direction = "u" }))
bind(mainMod .. " + j", hl.dsp.focus({ direction = "d" }))

bind(mainMod .. " + n", hl.dsp.window.cycle_next({ next = true }))
bind(mainMod .. " + p", hl.dsp.window.cycle_next({ next = false }))

for i = 1, 10 do
  local key = i % 10
  bind(mainMod .. " + " .. key, hl.dsp.focus({ workspace = i }))
  bind("ALT + " .. key, hl.dsp.focus({ workspace = i + 10 }))

  bind(mainMod .. " + SHIFT + " .. key, hl.dsp.window.move({ workspace = i, follow = true }))
  bind(mainMod .. " + CTRL + " .. key, hl.dsp.window.move({ workspace = i + 10, follow = true }))
end

bind(mainMod .. " + left", hl.dsp.window.swap({ direction = "l" }))
bind(mainMod .. " + right", hl.dsp.window.swap({ direction = "r" }))
bind(mainMod .. " + up", hl.dsp.window.swap({ direction = "u" }))
bind(mainMod .. " + down", hl.dsp.window.swap({ direction = "d" }))

hl.bind(mainMod .. " + mouse:272", hl.dsp.window.drag(), { mouse = true })
hl.bind(mainMod .. " + mouse:273", hl.dsp.window.resize(), { mouse = true })
