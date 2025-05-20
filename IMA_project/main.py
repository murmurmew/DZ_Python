from nodal_analysis.inflow_performance.ipr_model import IPR
from nodal_analysis.outflow_performance.vlp_model import VLP
from nodal_analysis.plotting import craete_plot
from nodal_analysis.solver import solve

if __name__ == "__main__":
    vlp = VLP(0.3, 2)
    ipr = IPR(2, 10)
    craete_plot(vlp, ipr, range(10))
    print('Дебит', solve(vlp, ipr)[0])
    print('Давление', solve(vlp, ipr)[1])