var removeDuplicates = function(nums) {
    let uniqueNums = []; //Crete an empty array to store unique numbers
    
    for (let i = 0; i < nums.length; i++) { 
        if (!uniqueNums.includes(nums[i])) {
            uniqueNums.push(nums[i]); // Add the number to uniqueNums if it's not already present
        }
    }
    
    for (let i = 0; i < uniqueNums.length; i++) {
        nums[i] = uniqueNums[i]; // Update the original array with the unique numbers
    }
    
    return uniqueNums.length; // Return the length of uniqueNums
};
