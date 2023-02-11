$(document).ready(function () {
    handlers.server_chat = function(message) {
        // message should just be a string
        handlers.chat_message({ type: "server", message: message });
    }

    handlers.server_chat(loc("!LOC:HyPA"));
    handlers.server_chat(loc("!LOC:!!! WARNING !!!"));
    handlers.server_chat(loc("!LOC:2.0x Build Speed (and Metal Income)!"));
    handlers.server_chat(loc("!LOC:1.5x Attack and Move Speed!"));
    handlers.server_chat(loc("!LOC:2x Commander HP."));
    handlers.server_chat(loc("!LOC:Be prepared!"));
});