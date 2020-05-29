from argparse import Namespace

from summaries.BattleFatalitiesSummary import BattleFatalitiesSummary
from test.base_test import BaseTest


class BattleFatalitiesSummaryTest(BaseTest):
    def test_build_data(self):
        args = Namespace(data=self.options['data_filename'])

        actual_date_data, actual_battle_data, actual_fatalities_data = BattleFatalitiesSummary(args).build_data()

        self.assertEqual(actual_date_data, ['11', '10'])
        self.assertEqual(actual_battle_data, [1, 2])
        self.assertEqual(actual_fatalities_data, [15, 21])

    def test_build_summary(self):
        actual = BattleFatalitiesSummary(self.args).build_summary()

        self.compare_actual_to_expected('test/expected/BattleFatalitiesSummary_expected.txt', actual)
