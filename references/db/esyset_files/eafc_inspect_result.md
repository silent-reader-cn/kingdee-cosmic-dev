# 四性检测结果(废弃)-eafc_inspect_result

## 四性检测结果(废弃)-主表 tk_eafc_inspect_result

- **表名称：** 四性检测结果(废弃)-主表
- **表名：** tk_eafc_inspect_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_check_type | fk_eafc_check_type | varchar | 50 |  | √ | ' ' |  |
| 3 | fk_eafc_inspector | 检测人员 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | forgid | forgid | int8 | 64 |  |  | null |  |
| 5 | fk_eafc_inspect_time | 检测日期 | timestamp | 0 |  |  | null | 检测日期 |
| 6 | fk_eafc_result_warn_level | fk_eafc_result_warn_level | varchar | 50 |  | √ | ' ' |  |
| 7 | fk_eafc_inspect_range | 检测范围 | varchar | 50 |  | √ | ' ' | 检测范围 |
| 8 | fk_eafc_inspect_proc | 检测环节 | varchar | 50 |  | √ | ' ' | 检测环节,枚举: 1 :接收环节 2 :归档环节 3 :移交环节 4 :保存环节 |
| 9 | fk_fpy_status | fk_fpy_status | varchar | 50 |  | √ | ' ' |  |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fk_fpy_report | fk_fpy_report | varchar | 500 |  |  | ' ' |  |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  |  | null |  |
| 13 | fbillno | fbillno | varchar | 100 |  | √ | ' ' |  |
| 14 | fk_eafc_qualified | 检测结果颜色标注 | varchar | 50 |  | √ | ' ' | 检测结果颜色标注,枚举: 1 :绿色 2 :红色 3 :蓝色 4 :黄色 |
| 15 | fmodifierid | fmodifierid | int8 | 64 |  |  | null |  |
| 16 | fbillstatus | fbillstatus | varchar | 50 |  | √ | ' ' |  |
| 17 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 18 | fk_eafc_inspect_config | 四性检测配置 | int8 | 64 |  |  | null | [四性检测配置 eafc_inspect_config](../esyset_files/eafc_inspect_config.md) |
| 19 | fk_eafc_inspect_schema | fk_eafc_inspect_schema | int8 | 64 |  |  | null |  |
| 20 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 21 | fk_eafc_manual_items | fk_eafc_manual_items | varchar | 50 |  | √ | ' ' |  |
| 22 | fk_eafc_inspect_explain | 检测结果 | varchar | 50 |  | √ | ' ' | 检测结果 |
| 23 | fk_fpy_progress | fk_fpy_progress | varchar | 50 |  | √ | ' ' |  |
| 24 | fk_eafc_check_user | fk_eafc_check_user | int8 | 64 |  |  | null |  |
| 25 | fk_eafc_inspect_type | 检测类型 | varchar | 50 |  | √ | ' ' | 检测类型,枚举: 1 :自动检测 2 :手动检测 |
| 26 | fk_fpy_general_org | fk_fpy_general_org | int8 | 64 |  | √ | 0 |  |
| 27 | fk_eafc_batch_num | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 28 | fk_eafc_file_count | fk_eafc_file_count | int8 | 64 |  |  | null |  |
| 29 | fk_eafc_result | fk_eafc_result | varchar | 2000 |  | √ | ' ' |  |
| 30 | fk_eafc_check_process | fk_eafc_check_process | varchar | 50 |  | √ | ' ' |  |
| 31 | fauditorid | fauditorid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_inspect_result |  | fid |
| 2 | idx_eafc_inspect_result_no |  | fbillno |
