/**
 * Reverses a singly linked list.
 *
 * @param {ListNode} head - The head node of the linked list.
 * @return {ListNode} - The new head node of the reversed linked list.
 */
class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head) {
        // Initialize three pointers: prev (previous node), curr (current node), and next (next node)
        let [prev, curr, next] = [null, head, null];
        
        // Iterate through the linked list until the current node is null
        while (curr) {
            // Store the next node
            next = curr.next;
            // Reverse the current node's pointer to point to the previous node
            curr.next = prev;

            // Move the previous node pointer to the current node
            prev = curr;
            // Move the current node pointer to the next node
            curr = next;
        }
        // Return the new head of the reversed linked list (which is the previous node)
        return prev;
    }
}