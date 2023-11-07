# Benchmarking Current models

Model | Drop Features | Aggregation | Feature Engineering | Kaggle | Benchmark ALL | A | B | C
--- | --- | --- | --- | --- | --- | --- | --- | ---
AutoGluon rnd:42 | A: snowcol | Mena, median(categorical) | time_season, OHE, Estimated, est_time_diff | 154,72 (`good_quality`) | 56,92 (`medium_quality`) | 136 | 18 | 15
AutoGluon rnd:42 | None | Mena, median(categorical)| time_season, OHE, Estimated, est_time_diff, combine_feat, combine(cloud,radiation)|N/A|57.2 (`medium_quality`)|136|19|15.8
XG 31.10 | None | Mean, median(categorical) | time_season, OHE, column_merge | 157 | 64,9 | 154 | 23,5 | 18
XG 6.11 | None | Mean, median(categorical) | time_season, OHE, column_merge, estimated, est_time_diff, Pred*`is_day` | 158 | 63,5| 152 | 21 | 17
CatBoost 6.11 | None | Mena, median(categorical) | time_season, OHE, Estimated, est_time_diff, combine_feat, Pred*`is_day` | 148.00 | 64,3 | 153,7 | 22,16 | 16,4
