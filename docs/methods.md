## car

### car.assets()

image paths are relative to https://images-static.iracing.com/


link: ```https://members-ng.iracing.com/data/car/assets```

### car.get()

No Description


link: ```https://members-ng.iracing.com/data/car/get```

---

## carclass

### carclass.get()

No Description


link: ```https://members-ng.iracing.com/data/carclass/get```

---

## constants

### constants.categories()

Constant; returned directly as an array of objects


link: ```https://members-ng.iracing.com/data/constants/categories```

### constants.divisions()

Constant; returned directly as an array of objects


link: ```https://members-ng.iracing.com/data/constants/divisions```

### constants.event_types()

Constant; returned directly as an array of objects


link: ```https://members-ng.iracing.com/data/constants/event_types```

---

## hosted

### hosted.combined_sessions()

Sessions that can be joined as a driver or spectator, and also includes non-league pending sessions for the user.

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `package_id` | `number` | If set, return only sessions using this car or track package ID. | False |

link: ```https://members-ng.iracing.com/data/hosted/combined_sessions```

### hosted.sessions()

Sessions that can be joined as a driver. Without spectator and non-league pending sessions for the user.


link: ```https://members-ng.iracing.com/data/hosted/sessions```

---

## league

### league.cust_league_sessions()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `mine` | `boolean` | If true, return only sessions created by this user. | False |
| `package_id` | `number` | If set, return only sessions using this car or track package ID. | False |

link: ```https://members-ng.iracing.com/data/league/cust_league_sessions```

### league.directory()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `search` | `string` | Will search against league name, description, owner, and league ID. | False |
| `tag` | `string` | One or more tags, comma-separated. | False |
| `restrict_to_member` | `boolean` | If true include only leagues for which customer is a member. | False |
| `restrict_to_recruiting` | `boolean` | If true include only leagues which are recruiting. | False |
| `restrict_to_friends` | `boolean` | If true include only leagues owned by a friend. | False |
| `restrict_to_watched` | `boolean` | If true include only leagues owned by a watched member. | False |
| `minimum_roster_count` | `number` | If set include leagues with at least this number of members. | False |
| `maximum_roster_count` | `number` | If set include leagues with no more than this number of members. | False |
| `lowerbound` | `number` | First row of results to return.  Defaults to 1. | False |
| `upperbound` | `number` | Last row of results to return. Defaults to lowerbound + 39. | False |
| `sort` | `string` | One of relevance, leaguename, displayname, rostercount. displayname is owners's name. Defaults to relevance. | False |
| `order` | `string` | One of asc or desc.  Defaults to asc. | False |

link: ```https://members-ng.iracing.com/data/league/directory```

### league.get()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `league_id` | `number` | No description available | True |
| `include_licenses` | `boolean` | For faster responses, only request when necessary. | False |

link: ```https://members-ng.iracing.com/data/league/get```

### league.get_points_systems()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `league_id` | `number` | No description available | True |
| `season_id` | `number` | If included and the season is using custom points (points_system_id:2) then the custom points option is included in the returned list. Otherwise the custom points option is not returned. | False |

link: ```https://members-ng.iracing.com/data/league/get_points_systems```

### league.membership()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `cust_id` | `number` | If different from the authenticated member, the following resrictions apply: - Caller cannot be on requested customer's block list or an empty list will result; - Requested customer cannot have their online activity prefrence set to hidden or an empty list will result; - Only leagues for which the requested customer is an admin and the league roster is not private are returned. | False |
| `include_league` | `boolean` | No description available | False |

link: ```https://members-ng.iracing.com/data/league/membership```

### league.roster()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `league_id` | `number` | No description available | True |
| `include_licenses` | `boolean` | For faster responses, only request when necessary. | False |

link: ```https://members-ng.iracing.com/data/league/roster```

### league.seasons()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `league_id` | `number` | No description available | True |
| `retired` | `boolean` | If true include seasons which are no longer active. | False |

link: ```https://members-ng.iracing.com/data/league/seasons```

### league.season_standings()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `league_id` | `number` | No description available | True |
| `season_id` | `number` | No description available | True |
| `car_class_id` | `number` | No description available | False |
| `car_id` | `number` | If car_class_id is included then the standings are for the car in that car class, otherwise they are for the car across car classes. | False |

link: ```https://members-ng.iracing.com/data/league/season_standings```

### league.season_sessions()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `league_id` | `number` | No description available | True |
| `season_id` | `number` | No description available | True |
| `results_only` | `boolean` | If true include only sessions for which results are available. | False |

link: ```https://members-ng.iracing.com/data/league/season_sessions```

---

## lookup

### lookup.club_history()

Returns an earlier history if requested quarter does not have a club history.

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `season_year` | `number` | No description available | True |
| `season_quarter` | `number` | No description available | True |

link: ```https://members-ng.iracing.com/data/lookup/club_history```

### lookup.countries()

No Description


link: ```https://members-ng.iracing.com/data/lookup/countries```

### lookup.drivers()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `search_term` | `string` | A cust_id or partial name for which to search. | True |
| `league_id` | `number` | Narrow the search to the roster of the given league. | False |

link: ```https://members-ng.iracing.com/data/lookup/drivers```

### lookup.get()

?weather=weather_wind_speed_units&weather=weather_wind_speed_max&weather=weather_wind_speed_min&licenselevels=licenselevels


link: ```https://members-ng.iracing.com/data/lookup/get```

### lookup.licenses()

No Description


link: ```https://members-ng.iracing.com/data/lookup/licenses```

---

## member

### member.awards()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `cust_id` | `number` | Defaults to the authenticated member. | False |

link: ```https://members-ng.iracing.com/data/member/awards```

### member.chart_data()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `cust_id` | `number` | Defaults to the authenticated member. | False |
| `category_id` | `number` | 1 - Oval; 2 - Road; 3 - Dirt oval; 4 - Dirt road | True |
| `chart_type` | `number` | 1 - iRating; 2 - TT Rating; 3 - License/SR | True |

link: ```https://members-ng.iracing.com/data/member/chart_data```

### member.get()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `cust_ids` | `numbers` | ?cust_ids=2,3,4 | True |
| `include_licenses` | `boolean` | No description available | False |

link: ```https://members-ng.iracing.com/data/member/get```

### member.info()

Always the authenticated member.


link: ```https://members-ng.iracing.com/data/member/info```

### member.participation_credits()

Always the authenticated member.


link: ```https://members-ng.iracing.com/data/member/participation_credits```

### member.profile()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `cust_id` | `number` | Defaults to the authenticated member. | False |

link: ```https://members-ng.iracing.com/data/member/profile```

---

## results

### results.get()

Get the results of a subsession, if authorized to view them. series_logo image paths are relative to https://images-static.iracing.com/img/logos/series/

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `subsession_id` | `number` | No description available | True |
| `include_licenses` | `boolean` | No description available | False |

link: ```https://members-ng.iracing.com/data/results/get```

### results.event_log()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `subsession_id` | `number` | No description available | True |
| `simsession_number` | `number` | The main event is 0; the preceding event is -1, and so on. | True |

link: ```https://members-ng.iracing.com/data/results/event_log```

### results.lap_chart_data()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `subsession_id` | `number` | No description available | True |
| `simsession_number` | `number` | The main event is 0; the preceding event is -1, and so on. | True |

link: ```https://members-ng.iracing.com/data/results/lap_chart_data```

### results.lap_data()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `subsession_id` | `number` | No description available | True |
| `simsession_number` | `number` | The main event is 0; the preceding event is -1, and so on. | True |
| `cust_id` | `number` | Required if the subsession was a single-driver event. Optional for team events. If omitted for a team event then the laps driven by all the team's drivers will be included. | False |
| `team_id` | `number` | Required if the subsession was a team event. | False |

link: ```https://members-ng.iracing.com/data/results/lap_data```

### results.search_hosted()

Hosted and league sessions.  Maximum time frame of 90 days. Results split into one or more files with chunks of results. For scraping results the most effective approach is to keep track of the maximum end_time found during a search then make the subsequent call using that date/time as the finish_range_begin and skip any subsessions that are duplicated.  Results are ordered by subsessionid which is a proxy for start time. Requires one of: start_range_begin, finish_range_begin. Requires one of: cust_id, team_id, host_cust_id, session_name.

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `start_range_begin` | `string` | Session start times. ISO-8601 UTC time zero offset: "2022-04-01T15:45Z". | False |
| `start_range_end` | `string` | ISO-8601 UTC time zero offset: "2022-04-01T15:45Z". Exclusive. May be omitted if start_range_begin is less than 90 days in the past. | False |
| `finish_range_begin` | `string` | Session finish times. ISO-8601 UTC time zero offset: "2022-04-01T15:45Z". | False |
| `finish_range_end` | `string` | ISO-8601 UTC time zero offset: "2022-04-01T15:45Z". Exclusive. May be omitted if finish_range_begin is less than 90 days in the past. | False |
| `cust_id` | `number` | The participant's customer ID. Ignored if team_id is supplied. | False |
| `team_id` | `number` | The team ID to search for. Takes priority over cust_id if both are supplied. | False |
| `host_cust_id` | `number` | The host's customer ID. | False |
| `session_name` | `string` | Part or all of the session's name. | False |
| `league_id` | `number` | Include only results for the league with this ID. | False |
| `league_season_id` | `number` | Include only results for the league season with this ID. | False |
| `car_id` | `number` | One of the cars used by the session. | False |
| `track_id` | `number` | The ID of the track used by the session. | False |
| `category_ids` | `numbers` | Track categories to include in the search.  Defaults to all. ?category_ids=1,2,3,4 | False |

link: ```https://members-ng.iracing.com/data/results/search_hosted```

### results.search_series()

Official series.  Maximum time frame of 90 days. Results split into one or more files with chunks of results. For scraping results the most effective approach is to keep track of the maximum end_time found during a search then make the subsequent call using that date/time as the finish_range_begin and skip any subsessions that are duplicated.  Results are ordered by subsessionid which is a proxy for start time but groups together multiple splits of a series when multiple series launch sessions at the same time. Requires at least one of: season_year and season_quarter, start_range_begin, finish_range_begin.

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `season_year` | `number` | Required when using season_quarter. | False |
| `season_quarter` | `number` | Required when using season_year. | False |
| `start_range_begin` | `string` | Session start times. ISO-8601 UTC time zero offset: "2022-04-01T15:45Z". | False |
| `start_range_end` | `string` | ISO-8601 UTC time zero offset: "2022-04-01T15:45Z". Exclusive. May be omitted if start_range_begin is less than 90 days in the past. | False |
| `finish_range_begin` | `string` | Session finish times. ISO-8601 UTC time zero offset: "2022-04-01T15:45Z". | False |
| `finish_range_end` | `string` | ISO-8601 UTC time zero offset: "2022-04-01T15:45Z". Exclusive. May be omitted if finish_range_begin is less than 90 days in the past. | False |
| `cust_id` | `number` | Include only sessions in which this customer participated. Ignored if team_id is supplied. | False |
| `team_id` | `number` | Include only sessions in which this team participated. Takes priority over cust_id if both are supplied. | False |
| `series_id` | `number` | Include only sessions for series with this ID. | False |
| `race_week_num` | `number` | Include only sessions with this race week number. | False |
| `official_only` | `boolean` | If true, include only sessions earning championship points. Defaults to all. | False |
| `event_types` | `numbers` | Types of events to include in the search. Defaults to all. ?event_types=2,3,4,5 | False |
| `category_ids` | `numbers` | License categories to include in the search.  Defaults to all. ?category_ids=1,2,3,4 | False |

link: ```https://members-ng.iracing.com/data/results/search_series```

### results.season_results()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `season_id` | `number` | No description available | True |
| `event_type` | `number` | Retrict to one event type: 2 - Practice; 3 - Qualify; 4 - Time Trial; 5 - Race | False |
| `race_week_num` | `number` | The first race week of a season is 0. | False |

link: ```https://members-ng.iracing.com/data/results/season_results```

---

## season

### season.list()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `season_year` | `number` | No description available | True |
| `season_quarter` | `number` | No description available | True |

link: ```https://members-ng.iracing.com/data/season/list```

### season.race_guide()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `from` | `string` | ISO-8601 offset format. Defaults to the current time. Include sessions with start times up to 3 hours after this time. Times in the past will be rewritten to the current time. | False |
| `include_end_after_from` | `boolean` | Include sessions which start before 'from' but end after. | False |

link: ```https://members-ng.iracing.com/data/season/race_guide```

### season.spectator_subsessionids()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `event_types` | `numbers` | Types of events to include in the search. Defaults to all. ?event_types=2,3,4,5 | False |

link: ```https://members-ng.iracing.com/data/season/spectator_subsessionids```

---

## series

### series.assets()

image paths are relative to https://images-static.iracing.com/


link: ```https://members-ng.iracing.com/data/series/assets```

### series.get()

No Description


link: ```https://members-ng.iracing.com/data/series/get```

### series.past_seasons()

Get all seasons for a series. Filter list by official:true for seasons with standings.

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `series_id` | `number` | No description available | True |

link: ```https://members-ng.iracing.com/data/series/past_seasons```

### series.seasons()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `include_series` | `boolean` | No description available | False |

link: ```https://members-ng.iracing.com/data/series/seasons```

### series.stats_series()

To get series and seasons for which standings should be available, filter the list by official: true.


link: ```https://members-ng.iracing.com/data/series/stats_series```

---

## stats

### stats.member_bests()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `cust_id` | `number` | Defaults to the authenticated member. | False |
| `car_id` | `number` | First call should exclude car_id; use cars_driven list in return for subsequent calls. | False |

link: ```https://members-ng.iracing.com/data/stats/member_bests```

### stats.member_career()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `cust_id` | `number` | Defaults to the authenticated member. | False |

link: ```https://members-ng.iracing.com/data/stats/member_career```

### stats.member_division()

Divisions are 0-based: 0 is Division 1, 10 is Rookie. See /data/constants/divisons for more information. Always for the authenticated member.

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `season_id` | `number` | No description available | True |
| `event_type` | `number` | The event type code for the division type: 4 - Time Trial; 5 - Race | True |

link: ```https://members-ng.iracing.com/data/stats/member_division```

### stats.member_recap()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `cust_id` | `number` | Defaults to the authenticated member. | False |
| `year` | `number` | Season year; if not supplied the current calendar year (UTC) is used. | False |
| `season` | `number` | Season (quarter) within the year; if not supplied the recap will be fore the entire year. | False |

link: ```https://members-ng.iracing.com/data/stats/member_recap```

### stats.member_recent_races()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `cust_id` | `number` | Defaults to the authenticated member. | False |

link: ```https://members-ng.iracing.com/data/stats/member_recent_races```

### stats.member_summary()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `cust_id` | `number` | Defaults to the authenticated member. | False |

link: ```https://members-ng.iracing.com/data/stats/member_summary```

### stats.member_yearly()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `cust_id` | `number` | Defaults to the authenticated member. | False |

link: ```https://members-ng.iracing.com/data/stats/member_yearly```

### stats.season_driver_standings()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `season_id` | `number` | No description available | True |
| `car_class_id` | `number` | No description available | True |
| `club_id` | `number` | Defaults to all (-1). | False |
| `division` | `number` | Divisions are 0-based: 0 is Division 1, 10 is Rookie. See /data/constants/divisons for more information. Defaults to all. | False |
| `race_week_num` | `number` | The first race week of a season is 0. | False |

link: ```https://members-ng.iracing.com/data/stats/season_driver_standings```

### stats.season_supersession_standings()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `season_id` | `number` | No description available | True |
| `car_class_id` | `number` | No description available | True |
| `club_id` | `number` | Defaults to all (-1). | False |
| `division` | `number` | Divisions are 0-based: 0 is Division 1, 10 is Rookie. See /data/constants/divisons for more information. Defaults to all. | False |
| `race_week_num` | `number` | The first race week of a season is 0. | False |

link: ```https://members-ng.iracing.com/data/stats/season_supersession_standings```

### stats.season_team_standings()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `season_id` | `number` | No description available | True |
| `car_class_id` | `number` | No description available | True |
| `race_week_num` | `number` | The first race week of a season is 0. | False |

link: ```https://members-ng.iracing.com/data/stats/season_team_standings```

### stats.season_tt_standings()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `season_id` | `number` | No description available | True |
| `car_class_id` | `number` | No description available | True |
| `club_id` | `number` | Defaults to all (-1). | False |
| `division` | `number` | Divisions are 0-based: 0 is Division 1, 10 is Rookie. See /data/constants/divisons for more information. Defaults to all. | False |
| `race_week_num` | `number` | The first race week of a season is 0. | False |

link: ```https://members-ng.iracing.com/data/stats/season_tt_standings```

### stats.season_tt_results()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `season_id` | `number` | No description available | True |
| `car_class_id` | `number` | No description available | True |
| `race_week_num` | `number` | The first race week of a season is 0. | True |
| `club_id` | `number` | Defaults to all (-1). | False |
| `division` | `number` | Divisions are 0-based: 0 is Division 1, 10 is Rookie. See /data/constants/divisons for more information. Defaults to all. | False |

link: ```https://members-ng.iracing.com/data/stats/season_tt_results```

### stats.season_qualify_results()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `season_id` | `number` | No description available | True |
| `car_class_id` | `number` | No description available | True |
| `race_week_num` | `number` | The first race week of a season is 0. | True |
| `club_id` | `number` | Defaults to all (-1). | False |
| `division` | `number` | Divisions are 0-based: 0 is Division 1, 10 is Rookie. See /data/constants/divisons for more information. Defaults to all. | False |

link: ```https://members-ng.iracing.com/data/stats/season_qualify_results```

### stats.world_records()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `car_id` | `number` | No description available | True |
| `track_id` | `number` | No description available | True |
| `season_year` | `number` | Limit best times to a given year. | False |
| `season_quarter` | `number` | Limit best times to a given quarter; only applicable when year is used. | False |

link: ```https://members-ng.iracing.com/data/stats/world_records```

---

## team

### team.get()

No Description

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `team_id` | `number` | No description available | True |
| `include_licenses` | `boolean` | For faster responses, only request when necessary. | False |

link: ```https://members-ng.iracing.com/data/team/get```

---

## time_attack

### time_attack.member_season_results()

Results for the authenticated member, if any.

| Parameter | Type | Description | Required |
|:---------|:----:|:------------|:--------:|
| `ta_comp_season_id` | `number` | No description available | True |

link: ```https://members-ng.iracing.com/data/time_attack/member_season_results```

---

## track

### track.assets()

image paths are relative to https://images-static.iracing.com/


link: ```https://members-ng.iracing.com/data/track/assets```

### track.get()

No Description


link: ```https://members-ng.iracing.com/data/track/get```

---

