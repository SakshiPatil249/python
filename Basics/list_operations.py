  """
Problem: List Operations
Platform: HackerRank

Description:
Perform a series of operations on a list based on given commands.

Commands:
- insert i e: Insert integer e at position i
- print: Print the list
- remove e: Delete first occurrence of e
- append e: Add e at end
- sort: Sort the list
- pop: Remove last element
- reverse: Reverse the list

Approach:
- Read number of commands
- Parse each command using split()
- Execute corresponding list operation
- Use conditional handling for commands

Time Complexity: O(N) (depends on operations)
Space Complexity: O(N)
""" 

if __name__ == '__main__':
    N = int(input())
    lst = []
    
    for _ in range(N):
        cmd = input().split()
        
        if cmd[0] == "insert":
            lst.insert(int(cmd[1]), int(cmd[2]))
        
        elif cmd[0] == "print":
            print(lst)
        
        elif cmd[0] == "remove":
            lst.remove(int(cmd[1]))
        
        elif cmd[0] == "append":
            lst.append(int(cmd[1]))
        
        elif cmd[0] == "sort":
            lst.sort()
        
        elif cmd[0] == "pop":
            lst.pop()
        
        elif cmd[0] == "reverse":
            lst.reverse()
