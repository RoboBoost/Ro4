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

// Генератор для кнопки
Blockly.Cpp['cyobot_button'] = function(block) {
  var button = block.getFieldValue('BUTTON');
  return ['digitalRead(' + button + ')', Blockly.Cpp.ORDER_ATOMIC];
};

// Генератор для потенціометра
Blockly.Cpp['cyobot_potentiometer'] = function(block) {
  return ['analogRead(A0)', Blockly.Cpp.ORDER_ATOMIC];
};

// Генератор для світлодіодів
Blockly.Cpp['cyobot_led'] = function(block) {
  var led = block.getFieldValue('LED');
  return 'digitalWrite(' + led + ', HIGH);\n';
};

// Генератор для моторів
Blockly.Cpp['cyobot_motor'] = function(block) {
  var motor = block.getFieldValue('MOTOR');
  var dir = block.getFieldValue('DIR');
  var speed = Blockly.Cpp.valueToCode(block, 'SPEED', Blockly.Cpp.ORDER_NONE) || '0';

  var pinA = (motor === 'MOTOR_A') ? '5' : '6';
  var pinB = (motor === 'MOTOR_A') ? '7' : '8';
  var forward = (dir === 'FORWARD') ? 'HIGH' : 'LOW';

  var code = 'digitalWrite(' + pinA + ', ' + forward + ');\n';
  code += 'digitalWrite(' + pinB + ', ' + ((dir === 'FORWARD') ? 'LOW' : 'HIGH') + ');\n';
  code += 'analogWrite(9, ' + speed + ');\n';
  return code;
};

// Генератор для RGB матриці
Blockly.Cpp['cyobot_rgb_matrix'] = function(block) {
  var color = block.getFieldValue('COLOR').replace('#', '0x');
  var x = Blockly.Cpp.valueToCode(block, 'X', Blockly.Cpp.ORDER_NONE) || '0';
  var y = Blockly.Cpp.valueToCode(block, 'Y', Blockly.Cpp.ORDER_NONE) || '0';
  var code = 'setRGBMatrixColor(' + x + ', ' + y + ', ' + color + ');\n';
  return code;
};
