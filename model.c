#include <string.h>
void score(double * input, double * output) {
    double var0[2];
    if (input[0] <= 0.14915071427822113) {
        if (input[0] <= 0.1184019148349762) {
            if (input[3] <= 0.20052754133939743) {
                memcpy(var0, (double[]){1.0, 0.0}, 2 * sizeof(double));
            } else {
                memcpy(var0, (double[]){0.0, 1.0}, 2 * sizeof(double));
            }
        } else {
            if (input[1] <= 1.258592426776886) {
                memcpy(var0, (double[]){0.0, 1.0}, 2 * sizeof(double));
            } else {
                if (input[3] <= -0.18242330849170685) {
                    memcpy(var0, (double[]){0.0, 1.0}, 2 * sizeof(double));
                } else {
                    memcpy(var0, (double[]){1.0, 0.0}, 2 * sizeof(double));
                }
            }
        }
    } else {
        if (input[1] <= 2.215593934059143) {
            if (input[0] <= 0.15814803540706635) {
                if (input[3] <= -0.07266231626272202) {
                    memcpy(var0, (double[]){0.0, 1.0}, 2 * sizeof(double));
                } else {
                    if (input[1] <= 1.2421725988388062) {
                        memcpy(var0, (double[]){0.0, 1.0}, 2 * sizeof(double));
                    } else {
                        memcpy(var0, (double[]){1.0, 0.0}, 2 * sizeof(double));
                    }
                }
            } else {
                memcpy(var0, (double[]){0.0, 1.0}, 2 * sizeof(double));
            }
        } else {
            if (input[3] <= -0.18015022575855255) {
                memcpy(var0, (double[]){0.0, 1.0}, 2 * sizeof(double));
            } else {
                if (input[2] <= 1.8049999475479126) {
                    if (input[3] <= -0.02940214052796364) {
                        memcpy(var0, (double[]){1.0, 0.0}, 2 * sizeof(double));
                    } else {
                        memcpy(var0, (double[]){0.5, 0.5}, 2 * sizeof(double));
                    }
                } else {
                    memcpy(var0, (double[]){0.0, 1.0}, 2 * sizeof(double));
                }
            }
        }
    }
    memcpy(output, var0, 2 * sizeof(double));
}
