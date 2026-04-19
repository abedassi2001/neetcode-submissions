class Solution {

    public String encode(List<String> strs) {
        String ret = "" ;
        for(String s : strs){
            ret += s + "~" ; 
        }
        return ret ;
    }

    public List<String> decode(String str) {
        List<String> ret = new ArrayList<>();

        int iter = 0 ; 
        String word = "";
        for (int i = 0 ; i < str.length() ; i++){

            if (str.charAt(i) == '~'){
                iter++ ;
                ret.add(word);
                word = "";
                continue ;
            }

            word += str.charAt(i) ;
            

        }
        return ret ;
    }
}
