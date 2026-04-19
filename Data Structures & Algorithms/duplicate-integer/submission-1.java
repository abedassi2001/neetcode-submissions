class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> cars = new HashSet<>();
        int length = nums.length;

        for (int i = 0 ; i < length ; i++){
            if(!cars.contains(nums[i]))
                cars.add(nums[i]); 
        
            else {
                return true ;
            }
         }
        return false ;
    }
}