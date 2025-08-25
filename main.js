var workspace = Blockly.inject('blocklyDiv', {
  toolbox: document.getElementById('toolbox'),
  scrollbars: true,
  trashcan: true,
  zoom: {
    controls: true,
    wheel: true,
    startScale: 1.0,
    maxScale: 3,
    minScale: 0.3,
    scaleSpeed: 1.2
  }
});

let socket = null;

document.getElementById('connectBtn').addEventListener('click', () => {
  const ip = prompt('Введіть IP ESP32 (наприклад, 192.168.1.100):');
  if (!ip) return;

  socket = new WebSocket(`ws://${ip}:81`);

  socket.onopen = () => {
    logOutput('Підключено до ' + ip);
  };

  socket.onclose = () => {
    logOutput('Відключено від ESP32');
    socket = null;
  };

  socket.onerror = (error) => {
    logOutput('Помилка WebSocket: ' + error.message);
  };

  socket.onmessage = (event) => {
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
  logOutput('Код надіслано на ESP32');
});

function logOutput(text) {
  const out = document.getElementById('output');
  out.textContent += text + '\n';
  out.scrollTop = out.scrollHeight;
}
