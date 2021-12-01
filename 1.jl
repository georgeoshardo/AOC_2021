using DelimitedFiles
file = readdlm("1.txt")
diffs = diff(file[:,1])
println(sum(diffs .> 0))