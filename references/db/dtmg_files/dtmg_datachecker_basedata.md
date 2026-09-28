# 校对器基础资料-dtmg_datachecker_basedata

## 校对器基础资料-主表 t_dtmg_dc_datachekers

- **表名称：** 校对器基础资料-主表
- **表名：** t_dtmg_dc_datachekers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fentryinfo | fentryinfo | varchar | 255 |  | √ | ' ' |  |
| 5 | fexcelsourcestartrow | fexcelsourcestartrow | int4 | 32 |  | √ | 0 |  |
| 6 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 7 | fentryinfo_tag | fentryinfo_tag | text | 0 |  |  | null |  |
| 8 | fmodifier | fmodifier | int8 | 64 |  | √ | 0 |  |
| 9 | fexceltargetendrow | fexceltargetendrow | int4 | 32 |  | √ | 0 |  |
| 10 | fexcelsourceendrow | fexcelsourceendrow | int4 | 32 |  | √ | 0 |  |
| 11 | fispreset | fispreset | bpchar | 1 |  | √ | '0' |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | frunstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :创建 B :审核中 C :已审核 D :重新审核 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fexceltargetstartrow | fexceltargetstartrow | int4 | 32 |  | √ | 0 |  |
| 17 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | fbilltype | fbilltype | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dtmg_dc_datachekers |  | fid |
| 2 | idx_fbillno |  | fbillno |
