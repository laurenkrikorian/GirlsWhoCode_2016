int LEDPIN = 4;
int LEDPIN2 = 5;

void setup() {
  // put your setup code here, to run once:
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LEDPIN, HIGH);
  digitalWrite(LEDPIN2, LOW);
  delay(50);
  digitalWrite(LEDPIN, LOW);
  digitalWrite(LEDPIN2, HIGH);
  delay(50);
  
}
