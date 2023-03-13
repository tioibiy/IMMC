#pragma GCC optimize(2)

#include<bits/stdc++.h>
#define LL long long
#define DB double
#define IT set<node>::iterator
using namespace std;
const DB dt=0.01,cx=0.0346,cy=0.061;
const int T=1000;
int N,M=8,type[1005],xmax=54,ymax=37;
DB a[60][40][10][1005],A[2005][1005];
struct Pos{
    int x,y;
    Pos(int X=0,int Y=0):x(X),y(Y){}
    Pos operator+(const Pos&b)const{
        return Pos(x+b.x,y+b.y);
    }
    Pos operator-(const Pos&b)const{
        return Pos(x-b.x,y-b.y);
    }
    Pos operator*(const Pos&b)const{
        return Pos(x*b.x,y*b.y);
    }
}pos[1005];
DB dis(Pos a,Pos b){
    Pos d=a-b;
    DB x=((DB)d.x)*cx,y=((DB)d.y)*cy;
    return sqrt(x*x+y*y);
}
DB U(int j,int i,Pos posk,Pos pos){
    //位于posk的第j种建筑对位于pos的第i个指标的影响程度
    if(i==0||i==2||i==3||i==4||i==5){
        return 0;
    }
    if(i==6){
        if(j==0) return 0.004*365;
        if(j==4) return 0.0023*365;
        return 0;
    }
    if(i==7){
        return 1.0/(dis(posk,pos)+1.0);
    }
    if(i==1){
        return -1.0/(dis(posk,pos)+1.0);
    }
}
DB suit[10][10]={
    {7,1.43,0,0,6},
    {0.35,-1,-1,-1,0.3},
    {15,70,60,55,55},
    {-1,70,76,70,67},
    {6.7,12,7.3,6.9,8},
    {-4,21,20,18,16},
    {2e9,-1,-1,-1,2e9},
    {0,0,0,0,0}
};
DB V(int i,int j,DB a){
    // 衡量第j种建筑的对第i个指标的要求与实际是相似程度
    DB ssuit=suit[i][j];
    if(ssuit==-1){
        return 0.5;
    }
    if(ssuit==2e9){
        return a/1000;
    }
    return 1/(abs(a-ssuit)+1);
}
DB a0[60][40][10]={};
void init(){
    freopen("C:/Users/linru/Desktop/IMMC/Code/Python/out","r",stdin);
    for(int x=0;x<xmax;x++){
        for(int y=0;y<ymax;y++){
            cin>>a0[x][y][0];
        }
    }
    freopen("C:/Users/linru/Desktop/IMMC/Code/Python/tree","r",stdin);
    for(int x=0;x<xmax;x++){
        for(int y=0;y<ymax;y++){
            cin>>a0[x][y][1];
        }
    }
    freopen("pos.txt","r",stdin);
    int x,y;
    while(cin>>x>>y){
        pos[N++]=Pos(x,y);
        if(N<=120){
            type[N]=0;
        }else if(N<=208){
            type[N]=1;
        }else{
            type[N]=0;
        }
    }
}
void dif(DB a0[][40][10],DB W[]){
    DB sumW=0;
    for(int i=0;i<M;i++){
        sumW+=W[i];
    }
    for(int x=0;x<xmax;x++){
        for(int y=0;y<ymax;y++){
            for(int i=0;i<M;i++){
                a[x][y][i][0]=a0[x][y][i];
            }
        }
    }
    memset(A,0,sizeof(A));
    for(int t=1;t<T;t++){
        for(int k=0;k<N;k++){
            for(int i=0;i<M;i++){
                A[k][t]+=V(i,type[k],a[pos[k].x][pos[k].y][i][t-1])*W[i];
            }
            A[k][t]/=sumW;
        }
        for(int kk=0;kk<N;kk++){
            int x=pos[kk].x,y=pos[kk].y;
            for(int i=1;i<M;i++){
                DB da=0;
                for(int k=0;k<N;k++){
                    da+=A[k][t]*U(type[k],i,pos[k],pos[kk]);
                }
                a[pos[kk].x][pos[kk].y][i][t]=a[pos[kk].x][pos[kk].y][i][t-1]+da*dt;
            }
        }
    }
}
DB s[10]={13.59-3.22,2.59-0.11,0.675-0.41,1.97-0.06,64.26,3.71};
DB c[10]={32.16,0.18,0.075,3.71,185.35};
DB S(int j,DB tim){
    if(tim) return s[j];
    return -c[j];
}
DB h(int flag,DB tim){
    if(flag==1){
        return ((DB)1.0)/(exp(tim-1)+1);
    }
    return (DB)1.0-((DB)1.0)/(exp(tim-1)+1);
}
DB rate(DB r,DB tim){
    return r*h(1,tim)+(1-r)*h(2,tim);
}
DB P(DB r,DB a0[][40][10],DB W[]){
    dif(a0,W);
    DB p=0;
    for(int t=0;t<T;t++){
        DB tim=((DB)t)*dt;
        DB dp=0;
        for(int k=0;k<N;k++){
            if(t){
                dp+=A[k][t]*S(type[k],tim)*rate(r,tim);
            }else{
                dp+=S(type[k],tim)*rate(r,tim);
            }
        }
        p+=dp*dt;
    }
    return p;
}
int main(){
    init();
    DB W[M]={};
    for(int i=0;i<M;i++) W[i]=1;
    cout<<P(0.5,a0,W);
    freopen("out","w",stdout);
    for(int i=0;i<T;i++){
        // cout<<dt*(DB)i<<" "<<A[0][i]<<endl;
        cout<<dt*(DB)i<<" "<<a[11][2][1][i]<<" "<<a[11][2][6][i]<<" "<<a[11][2][7][i]<<endl;
    }
    return 0;
}