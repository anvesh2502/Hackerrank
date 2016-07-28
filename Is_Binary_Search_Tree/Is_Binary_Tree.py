/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.

The Node class is defined as follows:
    class Node {
        int data;
        Node left;
        Node right;
     }
*/

ArrayList<Integer> arr=new ArrayList<Integer>();

   void getList(Node root)
   {
       if(root!=null)
       {
       getList(root.left);
       arr.add(root.data);
       getList(root.right);
       }
   }

    boolean checkBST(Node root)
    {
        getList(root);
        for(int i=1;i<arr.size();i++)
        {
        if(arr.get(i-1)>=arr.get(i))
            return false;
        }
        return true;

    }
