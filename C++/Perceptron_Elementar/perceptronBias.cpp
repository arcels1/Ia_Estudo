#include <bits/stdc++.h>
using namespace std;

typedef struct{
vector<int>entradaX;
vector<double>pesosW;
double saida = 0;
}PerceptronInf;

PerceptronInf perceptronCalculo(PerceptronInf perceptron){
 for(int i =0 ; i< perceptron.entradaX.size();i++){
  perceptron.saida += perceptron.entradaX.at(i)*perceptron.pesosW.at(i);
 }
return perceptron;
}

int main() {
vector<int> X;
vector<double> W;
PerceptronInf perceptron;
//Bias
X.push_back(1);
W.push_back(0.5);

//Entradas
int temp;
for (int i = 0; i <2; i++){
    cin>>temp;
    X.push_back(temp);
    W.push_back(0.5);
}

perceptron.entradaX = X;
perceptron.pesosW = W;
perceptron = perceptronCalculo(perceptron);
cout << perceptron.saida;



return 0;
}
