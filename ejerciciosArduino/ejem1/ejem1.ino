int amarillo = 13;
int milisegundos  = 100;
int rojo = 7;


void setup()
{
  pinMode(amarillo, OUTPUT); 
  pinMode(rojo, OUTPUT); 
}

void loop()
{
  digitalWrite(amarillo, HIGH);
  digitalWrite(rojo, LOW);
  delay(milisegundos);

  digitalWrite(amarillo, LOW);
  digitalWrite(rojo, HIGH);
  delay(milisegundos*2);


}
