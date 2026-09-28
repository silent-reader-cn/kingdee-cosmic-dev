# 免税、减计收入及加计扣除调整汇总底稿-tccit_hzdg_msjj_sum

## 免税、减计收入及加计扣除调整汇总底稿-主表 t_tccit_hzdg_msjj_sum

- **表名称：** 免税、减计收入及加计扣除调整汇总底稿-主表
- **表名：** t_tccit_hzdg_msjj_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 展示序号 | varchar | 50 |  | √ | ' ' | 展示序号 |
| 3 | fitemtype | 项目 | varchar | 50 |  | √ | ' ' | 项目 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :符合免税条件的投资收益 2 :清算或撤资中应确认的股息所得调整 3 :其他免税收入、减计收入及加计扣除调整 4 :研发费用加计扣除 5 :合计 |
| 5 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 6 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 7 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 8 | famount | 调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整金额 |
| 9 | fskssqq | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 10 | fewblname | 二维表名称 | varchar | 500 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_hzdg_msjj_sum |  | fid |
| 2 | idx_tccit_hzdg_msjj_sum |  | forgid,fskssqq,fskssqz |
