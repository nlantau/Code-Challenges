/*****************************************************************************
 * Playground - Thread and I/O
 *
 * nlantau, 2022-02-
 ****************************************************************************/
#include <assert.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

#define NTHREADS 10

pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;

/**** Functions *************************************************************/
void *print_name(void *args)
{
	pthread_mutex_lock(&mutex1);
	int *id = (int*)args;
	sleep(1);
	printf("> My name Jeff\n");
	if (id)
		printf("> args: %d, pthread_self(): %ld\n", *id, pthread_self());
	pthread_mutex_unlock(&mutex1);
	return NULL;
}


void using_one_thread(void)
{
	pthread_t thread_id;
	printf("> Before thread\n");
	pthread_create(&thread_id, NULL, print_name, NULL);
	pthread_join(thread_id, NULL);
	printf("> After thread\n");
}

void using_three_threads(void)
{
	int i;
	pthread_t tid[NTHREADS];

	printf("> Creating threads...\n");
	for (i = 0; i < NTHREADS; ++i) {
		pthread_create(&tid[i], NULL, print_name, (void*)&i);
	}
	printf("> Joining threads...\n");

	for (i = 0; i < NTHREADS; ++i)
		pthread_join(tid[i], NULL);
}

int main(void)
{
	using_three_threads();
	using_one_thread();

	return 0;
}
