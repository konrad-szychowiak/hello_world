// kompilacja: gcc <nazwa tego pliku> -Wall -o <nazwa pliku wynikowego>
// nadanie uprawnień do uruchomienia pliku wynikowego: chmod +x <nazwa pliku wynikowego>
// uruchomienie: ./<nazwa pliku wynikowego>

//TODO dołączenie wymaganych plików nagłówkowych
// poszukać w man <nazwa funkcji> i w man 7 ip
// ewentualnie przy kompilacji z -Wall może pojawić się sugestia, wskazująca którego pliku nagłówkowego brakuje
#include <string.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <unistd.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	printf("poszlo0 \n");
	const char* IP = argv[1];
	int port = atoi(argv[2]);

	struct sockaddr_in server_addr;

	int my_socket = socket(AF_INET,SOCK_STREAM,0);

	printf("poszlo1 \n");

	memset(&server_addr, 0, sizeof(struct sockaddr_in));
	server_addr.sin_family = AF_INET;
	server_addr.sin_port = htons(port);
	printf("poszlo2 \n");
	//TODO przypisać adres IP serwera
	//do pola server_addr.sin_addr.s_addr
	//używając funkcji inet_pton
	inet_pton(AF_INET,IP,&(server_addr.sin_addr));
	printf("poszlo3 \n");

	if(connect(my_socket, (struct sockaddr *)&server_addr, sizeof(struct sockaddr))==-1){
		printf("ERROR: niepowodzenie w polaczeniu! \n");
		return 1;
	}
	printf("poszlo4 \n");

	//TODO odebranie danych przesłanych przez serwer i wyświetlenie ich na ekranie
	//przy użyciu printf uwaga na buforowanie tekstu; nowa linia '\n' wymusza opróżnienie buforu (flush)
	char buffor;
	while(buffor != '\n'){
		if(read(my_socket,&buffor,1)==-1){
			printf("ERROR: nie udalo sie zczytac danych! \n");
			return 1;
		};
		printf(&buffor);
	}

	close(my_socket);
}
