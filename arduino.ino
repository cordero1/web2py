
int valor= analogRead(0);
char recibido;
String estado_led=",0";
String  enviar;

void setup()
{
  Serial.begin(9600);
  pinMode(7, INPUT);
  pinMode(2, OUTPUT);
  pinMode(8, OUTPUT);
  digitalWrite(2,0);
}

void loop() 
{
  if (Serial.available()>0)
    {
      recibido= Serial.read();
      if (recibido=='a')
     {
       digitalWrite(8,1);
       estado_led=",1";
     }
    
    if (recibido=='b')
    {
      digitalWrite(8,0);
      estado_led=",0";
      }
    } 
    
   else{
    valor=map(analogRead(0),0,1023,0,86);
    enviar= enviar + String(valor);
    
    if (digitalRead(2)==1){
        enviar= enviar + ",1";
      }
      
     if (digitalRead(2)==0){
        enviar= enviar + ",0";
      }
    enviar= enviar + estado_led;
    Serial.println(enviar);
    enviar="";
    
    
    
  }
  
}
    


