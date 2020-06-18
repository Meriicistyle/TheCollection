int state;
void setup() {
pinMode(2, OUTPUT); 
Serial.begin(9600);
}

void loop() {
 if(Serial.available() > 0){     
      state = Serial.read();   
 }
if (state == 'F') {
     
      digitalWrite(2, HIGH);
    }
else if (state == 'B') {
      digitalWrite(2, LOW);
       
    }   
 }
