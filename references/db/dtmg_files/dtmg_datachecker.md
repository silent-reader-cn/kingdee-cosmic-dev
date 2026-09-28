# 校对器-dtmg_datachecker

## 校对器-主表 t_dtmg_dc_datachekers

- **表名称：** 校对器-主表
- **表名：** t_dtmg_dc_datachekers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fentryinfo | 分录配置明细 | varchar | 255 |  | √ | ' ' | 分录配置明细 |
| 5 | fexcelsourcestartrow | 表头显示第 | int4 | 32 |  | √ | 0 | 表头显示第 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fentryinfo_tag | 分录配置明细_详情 | text | 0 |  |  | null | 分录配置明细_详情 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fexceltargetendrow | 表头显示第 | int4 | 32 |  | √ | 0 | 表头显示第 |
| 10 | fexcelsourceendrow | 表头显示第 | int4 | 32 |  | √ | 0 | 表头显示第 |
| 11 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | frunstatus | 运行状态 | varchar | 50 |  | √ | 'A' | 运行状态,枚举: A :创建 B :审核中 C :已审核 D :重新审核 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fexceltargetstartrow | 表头显示第 | int4 | 32 |  | √ | 0 | 表头显示第 |
| 17 | fbillno | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 18 | fbilltype | 类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dtmg_dc_datachekers |  | fid |
| 2 | idx_fbillno |  | fbillno |
