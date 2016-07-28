/*

    class Node
       int data;
       Node left;
       Node right;
   */



  HashMap<Integer,ArrayList<Integer>> levelMap=new HashMap<Integer,ArrayList<Integer>>();


   void createList(Node root,int level)
   {
       if(root==null)
           return;


      if(levelMap.containsKey(level))
      {
      ArrayList<Integer> vals=levelMap.get(level);
      vals.add(root.data);
      levelMap.put(level,vals);
      }
      else
      {
      ArrayList<Integer> vals=new ArrayList<Integer>();
      vals.add(root.data);
      levelMap.put(level,vals);
      }

      createList(root.left,level+1);
      createList(root.right,level+1);

   }


   void printList()
   {
    int i=0;
    while(levelMap.containsKey(i))
    {
     List<Integer> l=levelMap.get(i);
     for(Integer v : l)
         System.out.print(v+" ");
     i++;
    }
    System.out.println();
   }





   void LevelOrder(Node root)
    {
      createList(root,0);
      printList();
    }
