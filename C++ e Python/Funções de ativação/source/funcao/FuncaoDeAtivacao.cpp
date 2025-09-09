#include <bits/stdc++.h>
using namespace std;

const string separador = ",";

//Mostra os valores no Terminal
void mostrarVector(const vector<double>& valores){
    for(double valoresI : valores ){
        cout<<valoresI<<endl;
    }
}
//Gera os valores de teste
void gerarRandom(vector<double>& valoresTeste, int limite){
random_device rd;
mt19937 random{ rd()};
uniform_real_distribution<double> distribuicao(-2.0,2.0);
    for(int i = 0 ; i<limite ; i++){
        double temp = distribuicao(random);
        valoresTeste.push_back(temp);
    }
}


void gerarArquivo(string titulo, const vector<double>& entrada,const vector<double>& saida){
        string arquivoNome  = "resultados/"+titulo + ".csv";
        ofstream gerenciarArquivo(arquivoNome);
        cout << gerenciarArquivo.tellp();
        gerenciarArquivo << "entradas"<<separador<<"saidas" << endl;
        for(int i = 0 ; i<entrada.size() ; i++){
            gerenciarArquivo<<entrada.at(i)<<separador<<saida.at(i)<<endl;
        }
        gerenciarArquivo.close();
    }

//Funcao de Limiar
void funcaoDeLimiar(const vector<double>& valores){
    vector<double> y;
    for(double v : valores){
        if(v >=0){
            y.push_back(1);
        }else if(v < 0){
            y.push_back(0);
        }
    }
    gerarArquivo("ResultadoLimiar", valores, y);
}
//Funcao Linear por Partes
void funcaoLinearPorPartes(const vector<double>& valores){
    vector<double> y;
    for(double v : valores){
        if( v >= 0.5){
            y.push_back(1);

        }else if((-0.5<v)&&(v<0.5)){
            y.push_back(v+0.5);

        }else if(v < -0.5){
            y.push_back(0);

        }
    }
    gerarArquivo("ResultadoLinearParte",valores,y);
}
//funcao Logistica com Amplicacao:
void funcaoLogisticaAmpliacao(const vector<double>& valores, int amplificacao){
vector <double> y;
for(double v : valores){
        y.push_back(1/(1+exp(-amplificacao*v)));

}
    string arquivoNome = "ResultadoLogisticaA"+ to_string(amplificacao);
    gerarArquivo(arquivoNome,valores,y);
}

//funcao Tangente Hiperbolica com Ampliacao:
void funcaoTangenteHiperbolicaAmpliacao(const vector<double>& valores, int amplificacao){
vector <double> y;
for(double v : valores){
        y.push_back(tanh(v*amplificacao));

}
    string arquivoNome = "ResultadoTanHipA"+ to_string(amplificacao);
    gerarArquivo(arquivoNome,valores,y);
}


int main() {





const int numeroLimite = 1000;
vector<double> valoresTeste = {};
gerarRandom(valoresTeste,numeroLimite);
mostrarVector(valoresTeste);
funcaoDeLimiar(valoresTeste);
funcaoLinearPorPartes(valoresTeste);
funcaoLogisticaAmpliacao(valoresTeste, 1);
funcaoLogisticaAmpliacao(valoresTeste, 10);
funcaoTangenteHiperbolicaAmpliacao(valoresTeste,1);
funcaoTangenteHiperbolicaAmpliacao(valoresTeste,10);

return 0;
}
