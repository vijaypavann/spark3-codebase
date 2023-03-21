---
icon: north-star
tags: [csv, json, dataset]
---
# Parser Utils

#### **Schema_Of_JSON**: 
Use Cases ::
1. To Process EventHub / Kafka Payload
2. Parse and extract the JSON columns (including nested array columns) to the top level DataFrame

Sample Payload::
![Payload](~/assets/input/payload.png)


### Solution:
1. Use [schema_of_json](https://spark.apache.org/docs/latest/api/sql/#schema_of_json) to parse the JSON column

```
df = spark.sql(f"""select schema_of_json('{json_str}') as jsch""")
    # print(json_str)
    # print(df.collect()[0])
    # df.printSchema()
    df.show(10, False)
    sch = df.head()[0]
    print(type(sch), sch)
```

2. 

```
df = (spark.read.format("csv")
          .option("header", "true")
          .option("escape", "\"")
          .load(param_file_path))

    print(f'{"--" * 10} Original Data {"--" * 10}')

    df.show()
    df.printSchema()
    # print(df.schema)

    schema_str = "STRUCT<events: ARRAY<STRUCT<attribute_list: ARRAY<STRUCT<name: STRING, value_new: STRING, " \
                 "value_old: STRING>>, audited_obj_id: STRING, chronicle_id: STRING, current_state: STRING, " \
                 "event_description: STRING, event_name: STRING, event_source: STRING, host_name: STRING, " \
                 "id_1: STRING, id_2: STRING, id_3: STRING, id_4: STRING, id_5: STRING, object_name: STRING, " \
                 "object_type: STRING, policy_id: STRING, r_object_id: STRING, session_id: STRING, string_1: STRING, " \
                 "string_2: STRING, string_3: STRING, string_4: STRING, string_5: STRING, time_stamp: STRING, " \
                 "time_stamp_utc: STRING, user_name: STRING, version_label: STRING, workflow_id: STRING>>, " \
                 "json_date: STRING, source: STRING> "

    parsed_df = (df.withColumn("json_data", from_json(col("json"), schema_str))
                 .withColumn("evnt", explode("json_data.events"))
                 .withColumn("attrib_list", explode("evnt.attribute_list"))
                 .selectExpr("doc_id",
                             "module_content_id",
                             "module_type",
                             "history_index",
                             "source",
                             "json_data.json_date",
                             "json_data.source as events_source",
                             "evnt.time_stamp_utc",
                             "evnt.r_object_id",
                             "evnt.audited_obj_id",
                             "evnt.workflow_id",
                             "evnt.policy_id",
                             "evnt.user_name",
                             "evnt.chronicle_id",
                             "evnt.event_description",
                             "evnt.event_source",
                             "evnt.object_name",
                             "evnt.version_label",
                             "evnt.id_5",
                             "evnt.id_4",
                             "evnt.time_stamp",
                             "evnt.object_type",
                             "evnt.current_state",
                             "evnt.session_id",
                             "attrib_list.name",
                             "attrib_list.value_new",
                             "attrib_list.value_old",
                             "evnt.string_3",
                             "evnt.event_name",
                             "evnt.string_2",
                             "evnt.string_5",
                             "evnt.string_4",
                             "evnt.id_1",
                             "evnt.host_name",
                             "evnt.string_1",
                             "evnt.id_3",
                             "evnt.id_2"
                             )

                 )

    print(f'{"==" * 10} Parsed Data {"==" * 10}')
    parsed_df.show(20, False)
    parsed_df.printSchema()

    out_path = "out/parsed_sample"
    parsed_df.write.mode("overwrite").parquet(out_path)

    print(f'{"**" * 10} Parquet Data {"**" * 10}')
    spark.read.parquet(out_path).show(10, False)
```


