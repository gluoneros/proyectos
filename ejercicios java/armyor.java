class armyor{
    public static void mayor(int n1, int n2, int n3, int n4){
        int[] myNum = {n1, n2, n3, n4};
        int nmayor = myNum[0];
        for (int i = 0; i < 4; i++) {
            if (myNum[i] > nmayor){            
                nmayor = myNum[i];         
            } 
                    
        }
      
      System.out.println("el mayor numero del array es: " + nmayor );  
    }    

        public static void main(String[] args) {      
        mayor(21, 13, 10, 15);
    }
}