# 检查项执行结果-idi_itemexeresult

## 检查项执行结果-主表 t_idi_itemexeresult

- **表名称：** 检查项执行结果-主表
- **表名：** t_idi_itemexeresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdeduction | 分数 | numeric | 23 | 10 | √ | 0 | 分数 |
| 3 | fitemid | 检查项id | varchar | 50 |  | √ | ' ' | 检查项id |
| 4 | fstatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: running :执行中 succeed :执行成功 failed :执行失败 |
| 5 | fschemaresultid | 方案执行结果id | int8 | 64 |  | √ | 0 | 方案执行结果id |
| 6 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmatchtype | 检查项类型 | varchar | 50 |  | √ | ' ' | 检查项类型,枚举: linkup_bill :单据检查 news :新闻类 alarm :事件重复 general_ledger :账表查询类 future :未来计划展示 keyword :敏感词检测 invoice :票据检查 budget :预算查询 logistics_information :物流信息查询 billflow :上下游关键单据节点 statistics :数据统计及展示 fasindex :指标查询 attachment :附件检查 |
| 8 | fconfig | 检查项配置 | varchar | 255 |  |  | ' ' | 检查项配置 |
| 9 | freuslt | 检查项执行结果 | varchar | 255 |  |  | ' ' | 检查项执行结果 |
| 10 | fitem | 检查项名 | varchar | 50 |  | √ | ' ' | 检查项名 |
| 11 | fconfig_tag | 检查项配置_详情 | text | 0 |  |  | null | 检查项配置_详情 |
| 12 | farea | 分类名 | varchar | 50 |  | √ | ' ' | 分类名 |
| 13 | fareaid | 分类id | varchar | 50 |  | √ | ' ' | 分类id |
| 14 | freuslt_tag | 检查项执行结果_详情 | text | 0 |  |  | null | 检查项执行结果_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_idi_itemexeresult_item |  | fitemid |
| 2 | pk_t_idi_itemexeresult |  | fid |
| 3 | idx_idi_itemexeresult |  | fschemaresultid |
| 4 | idx_idi_itemexeresult_area |  | fareaid |
