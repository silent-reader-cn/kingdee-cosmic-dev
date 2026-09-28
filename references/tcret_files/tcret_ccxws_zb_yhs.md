# 财产行为税主表-印花税明细-tcret_ccxws_zb_yhs

## 财产行为税主表-印花税明细-主表 t_tcret_ccxws_zb_yhs

- **表名称：** 财产行为税主表-印花税明细-主表
- **表名：** t_tcret_ccxws_zb_yhs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsm | 税目 | varchar | 50 |  | √ | ' ' | 税目 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 |
| 4 | fseqno | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 5 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 6 | fjsyj | 计税依据 | numeric | 23 | 10 | √ | 0.0000000000 | 计税依据 |
| 7 | fenddate | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 8 | fjmse | 减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 减免税额 |
| 9 | fybse | 应补（退）税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应补（退）税额 |
| 10 | fstartdate | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 11 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 12 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额 |
| 13 | fyjse | 已缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 已缴税额 |
| 14 | ftaxtype | 税种 | varchar | 50 |  | √ | ' ' | 税种 |
| 15 | fsl | 税率 | varchar | 50 |  |  | ' ' | 税率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_ccxws_zb_yhs |  | fid |
| 2 | idx_tcret_ccxws_zb_yhs |  | fsbbid |
