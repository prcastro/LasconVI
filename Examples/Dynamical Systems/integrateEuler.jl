# Integrate simple linear differential equation
# Run using "julia integrateEuler.jl"

using PyPlot

function integrate(dxdt, params; x0 = 0, dt = 0.1, iters = 1000, threshold = 15, reset = 0)
    # Initialize the vector of x as a function of t
    xs = zeros(iters)
    xs[1] = x0

    # Spike counter
    spikes = 0

    for i in 2:iters
        xs[i] = xs[i - 1] + dt*dxdt(xs[i - 1], params)
        # If x exceeds the threshold, reset x and increment the spike counter
        if xs[i] > threshold
            xs[i] = reset
            spikes += 1
        end
    end

    # Return the vector of x as a function of time and the spike frequency
    return xs, spikes/(iters*dt)
end

# dx/dt = -(x - I)/τ
linear(x,params) = -(x - params[:I])/(params[:τ])

# Default parameters
params = Dict(:I => 20.0, :τ => 20)

# Integrate and store the results
xs, _ = integrate(linear, params)

# Plot voltage-time graph
plot(xs)
xlabel("Time")
ylabel("Voltage")
title("Linear Model - V(t)")
savefig("linear_vt.png")
clf()

# Determine spike frequency as a function of I
freqs = Float64[]
for I in 15.05:0.5:300
    params[:I] = I
    _ , freq = integrate(linear, params)
    push!(freqs, freq)
end

# Plot simulated frequency as a function of I
plot(15.05:0.5:300, freqs, label="Simulated")

# Compute and plot analytic frequency
afreq(I, params, threshold = 15) = 1/(-params[:τ] * log(1 - (threshold/I)))
afreqs = [afreq(I, params) for I in 15.05:0.5:300]
plot(15.05:0.5:300, afreqs, label="Analytic")

xlabel("I")
ylabel("Frequency")
legend()
title("Linear Model - f(I)")
savefig("linear_fi.png")
clf()
