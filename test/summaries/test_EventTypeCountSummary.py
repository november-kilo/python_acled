from summaries.EventTypeCountSummary import EventTypeCountSummary
from test.base_test import BaseTest


class EventTypeCountSummaryTest(BaseTest):
    def test_build_summary(self):
        actual = EventTypeCountSummary(self.args).build_summary()

        self.compare_actual_to_expected('test/expected/EventTypeCountSummary_expected.txt', actual)
