
let socket;
document.getElementById('connectBtn').addEventListener('click', () => {
    const ip = prompt('Введіть IP ESP32');
    if (!ip) return;
    socket = new WebSocket(`ws://${ip}:81`);
    socket.onopen = () => {
        logOutput('Підключено до ' + ip);
    };
    socket.onclose = () => {
        logOutput('Відключено');
    };
    socket.onerror = e => {
        logOutput('Помилка WebSocket: ' + e);
    };
    socket.onmessage = event => {
        logOutput('ESP32: ' + event.data);
    };
});
document.getElementById('sendCodeBtn').addEventListener('click', () => {
    if (!socket || socket.readyState !== WebSocket.OPEN) {
        alert('Спершу підключіться до ESP32');
        return;
    }
    const code = Blockly.Cpp.workspaceToCode(workspace);
    socket.send(code);
    logOutput('Код відправлено');
});
function logOutput(text) {
    const out = document.getElementById('output');
    out.textContent += text + '
';
    out.scrollTop = out.scrollHeight;
}
