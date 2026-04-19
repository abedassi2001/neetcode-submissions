class Solution {
    public int maxArea(int[] heights) {
        int left = 0 ; 
        int right = heights.length - 1 ;
        int maxSize = 0 ; 
        int currSize = 0 ;
        while (left < right ) {
            int width = right - left ;
            int height = Math.min(heights[left] , heights[right]);
            currSize = width * height ;

            maxSize = Math.max(currSize , maxSize);
            if (height == heights[right])right--;
            else{
                left ++ ;
            }
        }
        return maxSize ;

    }
}
