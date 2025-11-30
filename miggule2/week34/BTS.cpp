#include <iostream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

struct Node{
    string value;
    Node* left;
    Node* right;
    Node(string& str) : value(str), left(NULL), right(NULL){}
};

class Tree{
private :
    Node* root = nullptr;
    Node* insert(Node* node, string& str){
        if(node == NULL) return new Node(str);
        if(str < node->value ) node->left = insert(node->left, str);
        else if(str > node-> value) node->right = insert(node->right, str);
        return node;
    }

    Node* remove(Node* node, string& str){
        if(node == nullptr) return nullptr;

        // find logic
        if(str < node->value) node->left = remove(node->left,str);
        else if(str > node->value) node -> right = remove(node->right, str);
        else{
            // correct
            if(node->left == nullptr && node->right == nullptr){
                delete node;
                return nullptr;
            }

            //using gemini: When I found the node, I didn't know how to process it recursively, so I only referred to gemini for the left node.
            else if(node->left != nullptr){
                Node* leftMaxNode = node->left;
                while(leftMaxNode->right != nullptr) leftMaxNode = leftMaxNode->right;
                node->value = leftMaxNode->value;
                node->left = remove(node->left, leftMaxNode->value);
            }
            // Write almost the same thing with reference to the logic above
            else{
                Node* rightMinNode = node->right;
                while(rightMinNode->left != nullptr) rightMinNode = rightMinNode->left;
                node->value = rightMinNode->value;
                node->right = remove(node->right, rightMinNode->value);
            }
        }
        return node;
    }

    // To sort lexicographically in bst, use in order traversal.
    void depth(Node* node, int nowDepth, int targetDepth, vector<string>& result){
        if(node == nullptr) return;

        depth(node->left, nowDepth+1, targetDepth, result);
        if(nowDepth == targetDepth) result.push_back(node->value);
        depth(node->right, nowDepth+1, targetDepth, result);
    }

    // To sort lexicographically in bst, use in order traversal.
    void leaf(Node* node, vector<string>& result){
        if(node == nullptr) return;
        leaf(node->left, result);
        if(node->left == nullptr && node->right == nullptr) result.push_back(node->value);
        leaf(node->right,result);
    }

public:
    void add(string& str){
        root = insert(root,str);
    }
    void erase(string& str){
        root = remove(root, str);
    }
    void print(string& mode, int targetDepth){
        vector<string> result;
        if(mode == "leaf"){
            leaf(root,result);
        } else{
            depth(root,1,targetDepth,result);
            if(result.empty()) cout << "NO";
        }
        for(string& s : result) cout << s << " ";
        cout << endl;
    }
};

int main(){
    string input;
    Tree tree{};
    while(true){
        getline(cin,input);

        stringstream ss(input);

        string word;
        vector<string> words;

        while(getline(ss,word,' ')){
            words.push_back(word);
        }

        if(input == "quit") break;
        else if(words[0] == "+") tree.add(words[1]);
        else if(words[0] == "-") tree.erase(words[1]);
        else if(words[0] == "depth") tree.print(words[0],stoi(words[1]));
        else tree.print(words[0],0);
    }
}
