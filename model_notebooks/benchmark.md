# Benchmarking Current models

Model | Drop Features | Aggregation | Feature Engineering | Kaggle | Benchmark ALL | A | B | C
--- | --- | --- | --- | --- | --- | --- | --- | ---
AutoGluon rnd:42 | A: snowcol | Mena, median(categorical) | time_season, OHE, Estimated, est_time_diff | 154,72 (`good_quality`) | 56,92 (`medium_quality`) | 136 | 18 | 15
AutoGluon rnd:42 | None | mean, median(categorical)| time_season, OHE, Estimated, est_time_diff, combine_feat, combine(cloud,radiation), temp_flag|N/A|57.2 (`medium_quality`)|136|19|15.8
AutoGluon rnd:42 | A: snowcol | mean, median(categorical)| time_season, OHE, Estimated, est_time_diff, combine_feat, combine(cloud,radiation), combine(density, sun_elevation), temp_flag|N/A|57.2 (`medium_quality`)|136|19|15.7
XG 31.10 | None | Mean, median(categorical) | time_season, OHE, column_merge | 157 | 64,9 | 154 | 23,5 | 18
XG 6.11 | None | Mean, median(categorical) | time_season, OHE, column_merge, estimated, est_time_diff, Pred*`is_day` | 158 | 63,5| 152 | 21 | 17
CatBoost 6.11 | None | Mena, median(categorical) | time_season, OHE, Estimated, est_time_diff, combine_feat, Pred*`is_day` | 148.00 | 64,3 | 153,7 | 22,16 | 16,4


MAE for A:  136.75182481196686
MAE for B:  19.206511737846757
MAE for C:  15.769352065254601
Mean MAE:  57.24256287168941