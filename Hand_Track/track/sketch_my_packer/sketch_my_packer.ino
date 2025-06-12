#define LED 11

byte parseMode = 0;
String msg = ""; 

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Распаковка
  if(Serial.available()){
    char in = Serial.read();
    if(!(in=='\n' || in=='|r')){
      if(in == '#'){
        parseMode = 1;
      }
      else if(in == ';'){
        parseMode = 2;
      }
      else if(parseMode == 1){
        msg += in;
      }
      
    }
  }

  // Использование распакованого значения
  if(parseMode == 2){
    int message = msg.toInt();
    analogWrite(LED, message);
    parseMode = 0;
    msg = "";
  }

}
