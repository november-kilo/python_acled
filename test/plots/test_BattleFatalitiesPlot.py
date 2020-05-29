from argparse import Namespace

from plots.BattleFatalitiesPlot import BattleFatalitiesPlot
from test.base_test import BaseTest


class BattleFatalitiesPlotTest(BaseTest):
    def test_build_data(self):
        args = Namespace(data=self.options['data_filename'], title='foo')

        actual_date_data, actual_battle_data, actual_fatalities_data = BattleFatalitiesPlot(args).build_data()

        self.assertEqual(actual_date_data, ['11', '10'])
        self.assertEqual(actual_battle_data, [1, 2])
        self.assertEqual(actual_fatalities_data, [15, 21])
