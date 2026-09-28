# 四性检测基础资料-eafc_inspect_base

## 四性检测基础资料-主表 tk_eafc_inspect_strategy

- **表名称：** 四性检测基础资料-主表
- **表名：** tk_eafc_inspect_strategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_strategy_nature | 检测性质 | varchar | 50 |  | √ | ' ' | 检测性质,枚举: 1 :真实性 2 :完整性 3 :可用性 4 :安全性 |
| 3 | forgid | forgid | int8 | 64 |  |  | null |  |
| 4 | fk_eafc_strategy_name | 检测项目 | varchar | 150 |  | √ | ' ' | 检测项目 |
| 5 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 6 | fk_eafc_archive_link | 归档环节 | bpchar | 1 |  | √ | '1' | 归档环节 |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  |  | null |  |
| 10 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 11 | fk_eafc_strategy_desc | 检测依据和方法 | varchar | 2000 |  | √ | ' ' | 检测依据和方法 |
| 12 | fk_eafc_transfer_link | 移交与接收环节 | bpchar | 1 |  | √ | '1' | 移交与接收环节 |
| 13 | fsourcedataid | fsourcedataid | int8 | 64 |  |  | null |  |
| 14 | fbitindex | fbitindex | int8 | 64 |  |  | null |  |
| 15 | fk_eafc_org_y | fk_eafc_org_y | int8 | 64 |  |  | null |  |
| 16 | fk_eafc_strategy_purpose | 检测目的 | varchar | 200 |  | √ | ' ' | 检测目的 |
| 17 | fk_eafc_long_save_link | 长期保存环节 | bpchar | 1 |  | √ | '1' | 长期保存环节 |
| 18 | fk_eafc_strategy_obj | 检测对象 | varchar | 150 |  | √ | ' ' | 检测对象 |
| 19 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 20 | fname | fname | varchar | 50 |  |  | null |  |
| 21 | fmodifierid | fmodifierid | int8 | 64 |  |  | null |  |
| 22 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 23 | fk_eafc_strategy_code | 编号 | varchar | 50 |  | √ | ' ' | 编号 |
| 24 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 25 | fk_eafc_strategy_type | 检测类别 | varchar | 200 |  | √ | ' ' | 检测类别 |
| 26 | fenable | fenable | varchar | 50 |  | √ | ' ' |  |
| 27 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |
| 28 | fsourcebitindex | fsourcebitindex | int8 | 64 |  |  | null |  |
| 29 | fk_eafc_collect_link | 采集环节 | bpchar | 1 |  | √ | '1' | 采集环节 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_eafc_inspect_strategy_master |  | fmasterid |
| 2 | pk__eafc_inspect_strategy |  | fid |
| 3 | idx_tk_eafc_inspect_strategy_createorg |  | fcreateorgid |
