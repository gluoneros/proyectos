class armyor{
    public static void mayor(int n1, int n2, int n3, int n4){
      int[] myNum = {n1, n2, n3, n4};
      int ma = 0;
      int nmayor = myNum[0];
      for (int i = 0; i < myNum.length; i++) {
        for (int j = 0; j < myNum.length; j++){
          if (myNum[i] > myNum[j]){            
            ma = myNum[i];         
          }
          j = j + 1;        
        }
        nmayor = ma;
        i = i + 1;        
      }
      
      System.out.println("el mayor numero del array es: " + nmayor );    
  
    }
  
    public static void main(String[] args) {      
      mayor(1, 13, 10, 5);
    }
}
