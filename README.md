# DataCompression
In this project, I wanted to make a huffman code data compressor but turns out I shifted my focus on finding the alternative approaches to huffman encoder. Turns out that I was not able to accomplish my goal but I learnt a lot during the process, that is what a CSE major who is in his 1st year looks out for. Exploration :)

In the attempt or FAILURE 1.0, I instead of making a huffman tree using heaps, I tried to do array formations and make a complete binary tree, and fill zeroes where the tree wasn't complete, well turns out it was inefficient and time complexity was way over, because as the tree increased for large txt files, the loops got much complexed. Hence, Failed.....

In the second attempt or FAILURE 2.0, I wanted to keep the time complexity less, so here I used heap. This version wasn't much different from huffman approach. I just took all huffman nodes and formed a max heap using it, codes can backtracked while using loops and parent node (2*n) & (2*n + 1) formulas. This approach was efficient but some codes were repeating. I tried my best to find different methods to fix that bug but in the end wasn't able too. Hence, Failed.....

What I learned from these failures was that creating something innovative or new requries years of expertise and ofcourse passion. Historical concepts like Calculus or the discovery of "Quanta" by Max Planck, were not created in a week or midnight. Though I failed but gained a lot too.

If you are still reading, thank you so much for checking this out. I'm still a freshmen who needs to learn a lot of DSA.

“I have not failed. I've just found 10,000 ways that won't work.” --Thomas Alva Edison

Thank You.
