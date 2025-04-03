local initialized = false

function show_speed()
    local speed = mp.get_property_number("speed", 1.0)
    mp.osd_message(string.format("Speed: %.2fx", speed), 2)
end

mp.add_key_binding("S", "show_speed", show_speed)

mp.observe_property("speed", "number", function(_, _)
    if not initialized then
        initialized = true
        return
    end
    show_speed()
end)
