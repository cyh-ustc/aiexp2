rawdata = zeros(400, 10304);
for i = 1:40
    for j = 1:10
        filename = sprintf('faces\\s%d\\%d.pgm', i, j);
        f = fopen(filename, 'rb');
        fread(f, 10);
        rawdata(i*10+j-10,:) = fread(f,10304);
        fclose(f);
    end
end