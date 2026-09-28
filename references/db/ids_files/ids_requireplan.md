# 需求计划单-ids_requireplan

## 需求计划单-主表 t_ids_requireplan

- **表名称：** 需求计划单-主表
- **表名：** t_ids_requireplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fperiodid | 来源销售计划周期 | int8 | 64 |  | √ | 0 | [销售计划周期 ids_salesplan_period](../ids_files/ids_salesplan_period.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fmodeltypename | 预测方案名称（隐藏字段） | varchar | 100 |  | √ | ' ' | 预测方案名称（隐藏字段） |
| 10 | fconfig | 配置（隐藏字段） | varchar | 255 |  | √ | ' ' | 配置（隐藏字段） |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fconfig_tag | 配置（隐藏字段）_详情 | text | 0 |  |  | null | 配置（隐藏字段）_详情 |
| 13 | fbilltitle | 单据标题 | varchar | 50 |  | √ | ' ' | 单据标题 |
| 14 | fmodeltypeid | 预测方案 | varchar | 50 |  | √ | ' ' | 预测方案,枚举: |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ids_requireplan_fbillno |  | fbillno |
| 2 | idx_ids_requireplan_fbilldate |  | fbilldate |
| 3 | idx_ids_requireplan_fbilltitle |  | fbilltitle |
| 4 | pk_t_ids_requireplan |  | fid |
