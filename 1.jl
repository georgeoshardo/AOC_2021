using DelimitedFiles
file = readdlm("1.txt")
diffs = diff(file[:,1])
println(sum(diffs .> 0))

function rolling_diff(file, window)
    a = []
    for x ∈ 1:(length(file)-window)
        push!(a,sum(file[x+1:x+window]) - sum(file[x:x+window-1]))
    end
    return a
end
println(sum(rolling_diff(file,3) .> 0))

