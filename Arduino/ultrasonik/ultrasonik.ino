int pTrig = 8;
int pEcho = 6;
int buzz = 4;
long durasi;
char dataString[50] = {0};
int a = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(pTrig, OUTPUT);
  pinMode(pEcho, INPUT);
  pinMode(buzz, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  
  int jarak = trig();
  sprintf(dataString,"%02X",jarak);
  Serial.println(jarak);
  delay(1000);
}

long trig(){
  digitalWrite(pTrig, LOW);
  delayMicroseconds(1000);
  digitalWrite(pTrig, HIGH);
  delayMicroseconds(1000);
  digitalWrite(pTrig, LOW);
  durasi = pulseIn(pEcho, HIGH);
  return durasi / 29 / 2;
}

