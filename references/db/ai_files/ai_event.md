# 异构数据-ai_event

## 异构数据-主表 t_ai_event

- **表名称：** 异构数据-主表
- **表名：** t_ai_event

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 5 | feventid | feventid | varchar | 100 |  | √ | ' ' |  |
| 6 | feventclass | 异构数据模型 | int8 | 64 |  | √ | 0 | [异构数据对接模型 ai_eventclass](../ai_files/ai_eventclass.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fdata_tag | 数据_详情 | text | 0 |  |  | null | 数据_详情 |
| 9 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 10 | fsourcesys | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统 |
| 11 | forg | 业务单元 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 1 :生效 2 :废弃 3 :校验失败 |
| 14 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 15 | fentrycount | 分录数 | int8 | 64 |  | √ | 0 | 分录数 |
| 16 | fpaging | 分页 | bpchar | 1 |  | √ | ' ' | 分页,枚举: N :未开启分页 T :已完成 F :未完成 |
| 17 | ftextareafield | ftextareafield | bpchar | 1 |  | √ | ' ' |  |
| 18 | fenable | fenable | bpchar | 1 |  | √ | '0' |  |
| 19 | fnumber | 异构数据编码 | varchar | 80 |  | √ | ' ' | 异构数据编码 |
| 20 | fdata | 数据 | bpchar | 1 |  | √ | ' ' | 数据 |
| 21 | fversionnum | 版本编号 | int4 | 32 |  | √ | 1 | 版本编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_event |  | fid |
| 2 | idx_ai_event |  | fnumber,feventclass,feventid |
