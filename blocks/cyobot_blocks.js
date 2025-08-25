Blockly.defineBlocksWithJsonArray([
  {
    "type": "cyobot_button",
    "message0": "кнопка %1 натиснута",
    "args0": [
      {
        "type": "field_dropdown",
        "name": "BUTTON",
        "options": [
          ["Кнопка 1", "BTN1"],
          ["Кнопка 2", "BTN2"]
        ]
      }
    ],
    "output": "Boolean",
    "colour": 230,
    "tooltip": "Перевірити чи кнопка натиснута",
    "helpUrl": ""
  },
  {
    "type": "cyobot_potentiometer",
    "message0": "значення потенціометра",
    "output": "Number",
    "colour": 230,
    "tooltip": "Отримати аналогове значення потенціометра",
    "helpUrl": ""
  },
  {
    "type": "cyobot_led",
    "message0": "увімкнути світлодіод %1",
    "args0": [
      {
        "type": "field_dropdown",
        "name": "LED",
        "options": [
          ["LED1", "LED1"],
          ["LED2", "LED2"]
        ]
      }
    ],
    "previousStatement": null,
    "nextStatement": null,
    "colour": 120,
    "tooltip": "Увімкнути світлодіод",
    "helpUrl": ""
  },
  {
    "type": "cyobot_motor",
    "message0": "задати мотору %1 напрямок %2 швидкість %3",
    "args0": [
      {
        "type": "field_dropdown",
        "name": "MOTOR",
        "options": [
          ["Мотор A", "MOTOR_A"],
          ["Мотор B", "MOTOR_B"]
        ]
      },
      {
        "type": "field_dropdown",
        "name": "DIR",
        "options": [
          ["вперед", "FORWARD"],
          ["назад", "BACKWARD"]
        ]
      },
      {
        "type": "input_value",
        "name": "SPEED",
        "check": "Number"
      }
    ],
    "previousStatement": null,
    "nextStatement": null,
    "colour": 160,
    "tooltip": "Задати напрямок і швидкість мотора",
    "helpUrl": ""
  },
  {
    "type": "cyobot_rgb_matrix",
    "message0": "вивести колір %1 на RGB матрицю x:%2 y:%3",
    "args0": [
      {
        "type": "field_colour",
        "name": "COLOR"
      },
      {
        "type": "input_value",
        "name": "X",
        "check": "Number"
      },
      {
        "type": "input_value",
        "name": "Y",
        "check": "Number"
      }
    ],
    "previousStatement": null,
    "nextStatement": null,
    "colour": 20,
    "tooltip": "Задати точковий колір на RGB матриці",
    "helpUrl": ""
  }
]);
