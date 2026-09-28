# 辅助账支出表实体表临时(废弃)-rdem_fzz_zc_entity_tp

## 辅助账支出表实体表临时(废弃)-主表 t_rdem_fzz_zc_entity_tp

- **表名称：** 辅助账支出表实体表临时(废弃)-主表
- **表名：** t_rdem_fzz_zc_entity_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvouchertype | 种类 | varchar | 50 |  | √ | ' ' | 种类 |
| 3 | fzjtr | 直接投入费用 | numeric | 23 | 2 | √ | 0 | 直接投入费用 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 |
| 5 | fkjpzjz | 会计凭证记载金额 | numeric | 23 | 2 | √ | 0 | 会计凭证记载金额 |
| 6 | fvoucherremark | 摘要 | varchar | 2000 |  | √ | ' ' | 摘要 |
| 7 | fsfgd | 税法规定的归集金额 | numeric | 23 | 2 | √ | 0 | 税法规定的归集金额 |
| 8 | fjnjg | 委托境内机构或个人进行研发活动所发生的费用 | numeric | 23 | 2 | √ | 0 | 委托境内机构或个人进行研发活动所发生的费用 |
| 9 | fqt | 其他相关费用 | numeric | 23 | 2 | √ | 0 | 其他相关费用 |
| 10 | fvouchercode | 号数 | varchar | 50 |  | √ | ' ' | 号数 |
| 11 | fvoucherdate | 日期 | varchar | 50 |  | √ | ' ' | 日期 |
| 12 | fwtjwjg | 委托境外机构进行研发活动所发生的费用 | numeric | 23 | 2 | √ | 0 | 委托境外机构进行研发活动所发生的费用 |
| 13 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 14 | fryrg | 人员人工费用 | numeric | 23 | 2 | √ | 0 | 人员人工费用 |
| 15 | fwxzctx | 无形资产摊销 | numeric | 23 | 2 | √ | 0 | 无形资产摊销 |
| 16 | fxcpsjf | 新产品设计费等 | numeric | 23 | 2 | √ | 0 | 新产品设计费等 |
| 17 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 18 | fzjfy | 折旧费用 | numeric | 23 | 2 | √ | 0 | 折旧费用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_fzz_zc_entity_tp |  | fid |
| 2 | idx_rdem_fzz_zc_entity_tp_m0 |  | fvoucherdate |
