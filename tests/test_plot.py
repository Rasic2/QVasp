import os
import unittest
from pathlib import Path

from common.plot import PlotOpt, PlotBand, PlotDOS, PlotPES, PlotNEB
from common.task import NEBTask


class TestPlot(unittest.TestCase):

    def test_opt(self):
        plotter = PlotOpt("OUTCAR_opt")
        plotter.plot()
        plotter.save()

    def test_band(self):
        plotter = PlotBand("EIGENVAL", title="Band Structure")
        plotter.plot()
        plotter.save()

    def test_dos(self):
        plotter = PlotDOS(dos_file='DOSCAR-test', pos_file='CONTCAR-test')
        plotter.plot(color='#ed0345')
        plotter.plot(atoms='Ce', color='#000000')
        plotter.save()

    def test_pes1(self):
        plotter = PlotPES(height=8)
        colors = ['#ed0345', '#004370', '#000000']
        lines = [[None, None, None, 0.06, 0.39, -1.51],
                 [None, None, None, None, None, -2.46, -0.95, -1.66],
                 [0, -0.09, 0.75, 0.06, 0.26, -2.46, -1.02, -1.58]]

        for line, color in zip(lines, colors):
            plotter.plot(line, color)

        plotter.save()

    def test_pes2(self):
        energy_1 = [0, -0.09, 0.75, 0.06, 0.26, -2.46, -1.02, -1.58]
        label_1 = ["MS", "MS", "TS", "MS", "TS", "MS", "TS", "MS"]

        energy_2 = [None, None, None, None, None, -2.46, -0.95, -1.66]
        label_2 = [None, None, None, None, None, "MS", "TS", "MS"]

        energy_3 = [0, None, None, 0.06, None, None, 0.39, -1.51]
        label_3 = ["MS", None, None, "MS", None, None, "TS", "MS"]

        plotter = PlotPES(width=8, height=6)
        plotter.plot(data=(energy_1, label_1), color="#000000", style="solid_curve")
        plotter.plot(data=(energy_2, label_2), color="#ed0345", style="solid_curve")
        plotter.plot(data=(energy_3, label_3), color="#A8F760", style="solid_curve")

        plotter.save()

    def test_neb(self):
        plotter = PlotNEB()
        plotter.plot(workdir=Path("neb-test"))
        plotter.save()


if __name__ == '__main__':
    unittest.main()
