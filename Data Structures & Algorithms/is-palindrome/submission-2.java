class Solution {
    public boolean isPalindrome(String s) {
        int  left = 0  ;
        s = s.replaceAll("[^a-zA-Z0-9]", "");
        int right = 0 ;
        int mid = s.length() / 2 ; 
        s = s.toLowerCase().replace(" ","");
        System.out.println(s);
        if (s.length() % 2 == 0 ){
            right = mid ; 
            left = mid - 1 ;
        }
        else{
            right = mid + 1 ;
            left = mid - 1 ; 
        }
        
        while(left >= 0){
            System.out.println(left);
            System.out.println(right);
            if(s.charAt(left) != s.charAt(right)){
                return false ; 
            }
            right++;
            left--;
        }
        
        return true; 
    }
}
