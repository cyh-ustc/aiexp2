function g = jacobi(e, A)
    n = length(A);
    while 1
        z = A - A .* eye(n);
        if sum(sum(z .* z)) <= e
            break
        end
        z = abs(z);
        [a, p] = max(z);
        [a, q] = max(a);
        p = p(q);
        s = (A(q, q) - A(p, p)) / a / 2;
        if s == 0
            t = 1;
        else
            t = max(abs(- s - sqrt(s ^ 2 + 1)), abs(- s + sqrt(s ^ 2 + 1)));
        end
        c = 1 / sqrt(1 + t ^ 2);
        d = t / sqrt(1 + t ^ 2);
        Q = eye(n);
        Q(p, p) = c;
        Q(q, q) = c;
        Q(p, q) = d;
        Q(q, p) = -d;
        A = Q' * A * Q;
    end
    g = ones(1, n) * A;
end
