/**
 * Represents a stack that supports push, pop, top, and getMin operations.
 */
class MinStack { //Class was created to hold all of the operations
    constructor() {
        this.stack = [];
        this.minStack = [];
    }

    /**
     * Pushes the element val onto the stack.
     * @param {number} val - The value to be pushed onto the stack.
     * @return {void}
     */
    push(val) { //
        this.stack.push(val);
        if (this.minStack.length === 0 || val <= this.minStack[this.minStack.length - 1]) {
            this.minStack.push(val);
        }
    }

    /**
     * Removes the element on the top of the stack.
     * @return {void}
     */
    pop() {
        const popped = this.stack.pop();
        if (popped === this.minStack[this.minStack.length - 1]) {
            this.minStack.pop();
        }
    }

    /**
     * Gets the top element of the stack.
     * @return {number} - The top element of the stack.
     */
    top() {
        return this.stack[this.stack.length - 1];
    }

    /**
     * Retrieves the minimum element in the stack.
     * @return {number} - The minimum element in the stack.
     */
    getMin() {
        return this.minStack[this.minStack.length - 1];
    }
}