open type System.Math
open FSharp.Data

type Params =
    JsonProvider<"./parameters.json", InferenceMode=InferenceMode.ValuesAndInlineSchemasOverrides>

[<EntryPoint>]
let main argv =
    let pars = Params.GetSample()

    let steps = pars.Steps
    let N = pars.N
    let n = pars.N2 |> float
    let dtau = pars.Dtau |> float
    let kappa = pars.Kappa |> float

    let omega = argv[0] |> float

    let dx = 1.0 / float N

    let xs = [|
        for i = 0 to pars.N do
            yield float i * dx
    |]

    let psi_R =
        Array.map (fun x -> sqrt 2.0 * sin (n * PI * x)) xs

    psi_R[0] <- 0.0
    psi_R[psi_R.Length - 1] <- 0.0

    let psi_I = Array.zeroCreate (N + 1)

    let inline calc_H (psi: float array) (H: float array) tau =
        H[0] <- 0.0
        H[psi.Length - 1] <- 0.0

        for k in 1 .. psi.Length - 2 do
            H[k] <-
                -0.5
                * (psi[k + 1] + psi[k - 1] - 2.0 * psi[k])
                / dx
                / dx
                + kappa
                  * (xs[k] - 0.5)
                  * psi[k]
                  * sin (omega * tau)

    let H_R = Array.zeroCreate (N + 1)
    let H_I = Array.zeroCreate (N + 1)

    calc_H psi_R H_R 0.0
    calc_H psi_I H_I 0.0

    for step = 0 to steps do
        let tau = float step * dtau in

        calc_H psi_I H_I tau

        for k in 0 .. N - 1 do
            psi_R[k] <- psi_R[k] + H_I[k] * dtau / 2.0

        calc_H psi_R H_R tau

        for k in 0 .. N - 1 do
            psi_I[k] <- psi_I[k] - H_R[k] * dtau

        calc_H psi_I H_I tau

        for k in 0 .. N - 1 do
            psi_R[k] <- psi_R[k] + H_I[k] * dtau / 2.0

        if step % 10 = 0 then
            let norm =
                dx
                * (Array.zip psi_R psi_I
                   |> Array.sumBy (fun (r, i) -> r * r + i * i))

            let x =
                dx
                * (Array.zip3 xs psi_R psi_I
                   |> Array.sumBy (fun (x, r, i) -> x * (r * r + i * i)))

            let eps =
                dx
                * (Array.zip H_R H_I
                   |> Array.sumBy (fun (r, i) -> r * r + i * i))

            printfn "%f %f %f %f" tau norm x eps

            for k in 0 .. N - 1 do
                let rho =
                    psi_R[k] * psi_R[k]
                    + psi_I[k] * psi_I[k] in

                eprintfn "%f %d %f" tau k rho

    0
