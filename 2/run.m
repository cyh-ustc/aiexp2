z = [];
x = [];
t = [0.2 0.4 0.6 0.8 0.9 0.95 0.99 0.999 0.9999 1];
for i = t
    [u_reduce, k] = PCA(u, s, i);
    z = [z,k];
    a = traindata * u_reduce;
    b = testdata * u_reduce;
    g = predict(a,b);
    x = [x, g];
end