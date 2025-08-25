import zipfile
import os

project_name = "cyobot_blockly_project"
os.makedirs(project_name, exist_ok=True)

# index.html
index_html = """
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Cyobot Blockly ESP32</title>
    <script src=\"https://unpkg.com/blockly/blockly.min.js\"></script>
    <link rel=\"stylesheet\" href=\"style.css\">
</head>
<body>
    <h1>Cyobot Blockly ESP32 Online</h1>
    <div id=\"blocklyDiv\" style=\"height: 480px; width: 100%;\"></div>
    <xml id=\"toolbox\" style=\"display: none\">
        <category name=\"Керування\" colour=\"210\">
            <block type=\"cyobot_button\"></block>
            <block type=\"cyobot_potentiometer\"></block>
            <block type=\"cyobot_led\"></block>
            <block type=\"cyobot_motor\"></block>
            <block type=\"cyobot_rgb_matrix\"></block>
        </category>
        <category name=\"Логіка\" colour=\"120\">
            <block type=\"controls_if\"></block>
            <block type=\"logic_compare\"></block>
        </category>
    </xml>
    <button id=\"connectBtn\">Підключити</button>
    <button id=\"sendCodeBtn\">Відправити код на ESP32</button>
    <pre id=\"output\"></pre>
    <script src=\"websocket.js\"></script>
    <script src=\"blocks/cyobot_blocks.js\"></script>
    <script src=\"generators/cpp_generator.js\"></script>
    <script src=\"main.js\"></script>
</body>
</html>
"""

with open(os.path.join(project_name, "index.html"), "w") as f:
    f.write(index_html)

# style.css
style_css = """
body { font-family: Arial, sans-serif; margin: 10px; }
h1 { color: #333; }
button { margin: 5px; padding: 8px 12px; font-size: 16px; }
#output { background: #f0f0f0; border: 1px solid #ccc; height: 120px; overflow: auto; padding: 5px; }
"""
with open(os.path.join(project_name, "style.css"), "w") as f:
    f.write(style_css)

# websocket.js
websocket_js = """
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
    out.textContent += text + '\n';
    out.scrollTop = out.scrollHeight;
}
"""
with open(os.path.join(project_name, "websocket.js"), "w") as f:
    f.write(websocket_js)

# main.js
main_js = """
const workspace = Blockly.inject('blocklyDiv', {
    toolbox: document.getElementById('toolbox'),
    scrollbars: true,
});
"""
with open(os.path.join(project_name, "main.js"), "w") as f:
    f.write(main_js)

# cyobot_blocks.js
cyobot_blocks_js = """
Blockly.defineBlocksWithJsonArray([
  {
    \"type\": \"cyobot_button\",
    \"message0\": \"кнопка %1 натиснута\",
    \"args0\": [
      {
        \"type\": \"field_dropdown\",
        \"name\": \"BUTTON\",
        \"options\": [
          [\"Кнопка 1\", \"BTN1\"],
          [\"Кнопка 2\", \"BTN2\"]
        ]
      }
    ],
    \"output\": \"Boolean\",
    \"colour\": 230,
    \"tooltip\": \"Перевірити чи кнопка натиснута\",
    \"helpUrl\": \"\"
  },
  {
    \"type\": \"cyobot_potentiometer\",
    \"message0\": \"значення потенціометра\",
    \"output\": \"Number\",
    \"colour\": 230,
    \"tooltip\": \"Отримати аналогове значення потенціометра\",
    \"helpUrl\": \"\"
  },
  {
    \"type\": \"cyobot_led\",
    \"message0\": \"увімкнути світлодіод %1\",
    \"args0\": [
      {
        \"type\": \"field_dropdown\",
        \"name\": \"LED\",
        \"options\": [
          [\"LED1\", \"LED1\"],
          [\"LED2\", \"LED2\"]
        ]
      }
    ],
    \"previousStatement\": null,
    \"nextStatement\": null,
    \"colour\": 120,
    \"tooltip\": \"Увімкнути світлодіод\",
    \"helpUrl\": \"\"
  },
  {
    \"type\": \"cyobot_motor\",
    \"message0\": \"задати мотору %1 напрямок %2 швидкість %3\",
    \"args0\": [
      {
        \"type\": \"field_dropdown\",
        \"name\": \"MOTOR\",
        \"options\": [
          [\"Мотор A\", \"MOTOR_A\"],
          [\"Мотор B\", \"MOTOR_B\"]
        ]
      },
      {
        \"type\": \"field_dropdown\",
        \"name\": \"DIR\",
        \"options\": [
          [\"вперед\", \"FORWARD\"],
          [\"назад\", \"BACKWARD\"]
        ]
      },
      {
        \"type\": \"input_value\",
        \"name\": \"SPEED\",
        \"check\": \"Number\"
      }
    ],
    \"previousStatement\": null,
    \"nextStatement\": null,
    \"colour\": 160,
    \"tooltip\": \"Задати напрямок і швидкість мотора\",
    \"helpUrl\": \"\"
  },
  {
    \"type\": \"cyobot_rgb_matrix\",
    \"message0\": \"вивести колір %1 на RGB матрицю x:%2 y:%3\",
    \"args0\": [
      {
        \"type\": \"field_colour\",
        \"name\": \"COLOR\"
      },
      {
        \"type\": \"input_value\",
        \"name\": \"X\",
        \"check\": \"Number\"
      },
      {
        \"type\": \"input_value\",
        \"name\": \"Y\",
        \"check\": \"Number\"
      }
    ],
    \"previousStatement\": null,
    \"nextStatement\": null,
    \"colour\": 20,
    \"tooltip\": \"Задати точковий колір на RGB матриці\",
    \"helpUrl\": \"\"
  }
]);
"""
with open(os.path.join(project_name, "blocks/cyobot_blocks.js"), "w") as f:
    f.write(cyobot_blocks_js)

# cpp_generator.js
cpp_generator_js = """
Blockly.Cpp = new Blockly.Generator('Cpp');

Blockly.Cpp.addReservedWords('auto,break,case,char,const,continue,default,do,double,else,float,for,goto,if,int,long,return,short,signed,sizeof,static,struct,switch,unsigned,void,volatile,while');

Blockly.Cpp.init = function(workspace) {
  Blockly.Cpp.definitions_ = Object.create(null);
  Blockly.Cpp.functionNames_ = Object.create(null);
};

Blockly.Cpp.finish = function(code) {
  var definitions = [];
  for (var name in Blockly.Cpp.definitions_) {
    definitions.push(Blockly.Cpp.definitions_[name]);
  }
  return definitions.join('\n') + '\n' + code;
};

Blockly.Cpp.scrub_ = function(block, code) {
  var commentCode = '';
  var nextBlock = block.nextConnection && block.nextConnection.targetBlock();
  var nextCode = Blockly.Cpp.blockToCode(nextBlock);
  return commentCode + code + nextCode;
};

Blockly.Cpp['cyobot_button'] = function(block) {
  var button = block.getFieldValue('BUTTON');
  return ['digitalRead(' + button + ')', Blockly.Cpp.ORDER_ATOMIC];
};

Blockly.Cpp['cyobot_potentiometer'] = function(block) {
  return ['analogRead(A0)', Blockly.Cpp.ORDER_ATOMIC];
};

Blockly.Cpp['cyobot_led'] = function(block) {
  var led = block.getFieldValue('LED');
  return 'digitalWrite(' + led + ', HIGH);\n';
};

Blockly.Cpp['cyobot_motor'] = function(block) {
  var motor = block.getFieldValue('MOTOR');
  var dir = block.getFieldValue('DIR');
  var speed = Blockly.Cpp.valueToCode(block, 'SPEED', Blockly.Cpp.ORDER_NONE) || '0';
  var pinA = motor === 'MOTOR_A' ? '5' : '6';
  var pinB = motor === 'MOTOR_A' ? '7' : '8';
  var forward = dir === 'FORWARD' ? 'HIGH' : 'LOW';

  var code = 'digitalWrite(' + pinA + ', ' + forward + ');\n';
  code += 'digitalWrite(' + pinB + ', ' + (dir === 'FORWARD' ? 'LOW' : 'HIGH') + ');\n';
  code += 'analogWrite(9, ' + speed + ');\n';
  return code;
};

Blockly.Cpp['cyobot_rgb_matrix'] = function(block) {
  var color = block.getFieldValue('COLOR');
  var x = Blockly.Cpp.valueToCode(block, 'X', Blockly.Cpp.ORDER_NONE) || '0';
  var y = Blockly.Cpp.valueToCode(block, 'Y', Blockly.Cpp.ORDER_NONE) || '0';
  var code = `setRGBMatrixColor(${x}, ${y}, ${color});\n`;
  return code;
};
"""
with open(os.path.join(project_name, "generators/cpp_generator.js"), "w") as f:
    f.write(cpp_generator_js)

# esp32/ws_firmware.ino
ws_firmware_ino = """
#include <WiFi.h>
#include <WebSocketsServer.h>

const char* ssid = \"your_SSID\";
const char* password = \"your_PASSWORD\";

WebSocketsServer webSocket = WebSocketsServer(81);

void handleWebSocketMessage(void *arg, uint8_t *data, size_t len) {
  WebSocketsServer *server = (WebSocketsServer *)arg;
  // Тут можна додати виконання отриманого коду
  Serial.print(F("Received code:\n"));
  Serial.write(data, len);
  Serial.println();
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.print("\nConnected to WiFi. IP: ");
  Serial.println(WiFi.localIP());

  webSocket.begin();
  webSocket.onEvent([](uint8_t num, WStype_t type, uint8_t * payload, size_t length) {
    if (type == WStype_TEXT) {
      handleWebSocketMessage(&webSocket, payload, length);
    }
  });
}

void loop() {
  webSocket.loop();
}
"""
with open(os.path.join(project_name, "esp32/ws_firmware.ino"), "w") as f:
    f.write(ws_firmware_ino)

# esp32/config/wifi_config.h
wifi_config_h = """
#ifndef WIFI_CONFIG_H
#define WIFI_CONFIG_H

#define WIFI_SSID \"your_SSID\"
#define WIFI_PASSWORD \"your_PASSWORD\"
#define STATIC_IP IPAddress(192, 168, 1, 100)
#define GATEWAY IPAddress(192, 168, 1, 1)
#define SUBNET IPAddress(255, 255, 255, 0)

#endif
"""
with open(os.path.join(project_name, "esp32/config/wifi_config.h"), "w") as f:
    f.write(wifi_config_h)

# README.md
readme_md = """
# Cyobot Blockly ESP32 Project

Цей проект дозволяє програмувати ESP32 онлайн через Blockly з підтримкою кастомних блоків для кнопок, потенціометра, світлодіодів, моторів та RGB матриці.

## Як запустити

1. Розгорніть веб-інтерфейс:
   - Відкрийте `index.html` у сучасному браузері або налаштуйте локальний сервер.
2. Підключіть ESP32 до WiFi з налаштуваннями у `esp32/config/wifi_config.h`.
3. Зашийте прошивку `esp32/ws_firmware.ino` через Arduino IDE.
4. У веб-інтерфейсі натисніть "Підключити" та введіть IP ESP32.
5. Створіть блок-схему та натисніть "Відправити код на ESP32".

## Структура проекту

- `index.html` — веб-інтерфейс Blockly
- `style.css` — стилі
- `websocket.js` — логіка WebSocket
- `src/blocks/cyobot_blocks.js` — визначення кастомних блоків
- `src/generators/cpp_generator.js` — генератор C++
- `esp32/ws_firmware.ino` — прошивка ESP32
- `esp32/config/wifi_config.h` — WiFi налаштування

## Ліцензія

MIT
"""
with open(os.path.join(project_name, "README.md"), "w") as f:
    f.write(readme_md)

# Создание архива
archive_name = project_name + ".zip"
with zipfile.ZipFile(archive_name, 'w') as zipf:
    for foldername, subfolders, filenames in os.walk(project_name):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            zipf.write(file_path, os.path.relpath(file_path, project_name))

archive_name
