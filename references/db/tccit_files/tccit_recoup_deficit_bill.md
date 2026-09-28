# 弥补以前年度亏损台账单据-tccit_recoup_deficit_bill

## 弥补以前年度亏损台账单据-主表 t_tccit_recoup_deficit

- **表名称：** 弥补以前年度亏损台账单据-主表
- **表名：** t_tccit_recoup_deficit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountresource | 金额来源 | varchar | 50 |  | √ | ' ' | 金额来源,枚举: lastdeclare :上期申报表 lastdraft :上期底稿 |
| 3 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 4 | fitem | 项目 | varchar | 50 |  | √ | ' ' | 项目,枚举: item1 :利润总额 item2 :加：特定业务计算的应纳税所得额 item3 :减：不征税收入 item4 :减：免税收入、减计收入、加计扣除 item5 :减：资产加速折旧、摊销 item6 :减：所得减免 item7 :享受减免后的应纳税所得额(1+2-3-4-5-6) item8 :待弥补以前年度亏损金额 item9 :本年所得弥补以前年度亏损金额 item10 :弥补以前年度亏损后所得(7-9) |
| 5 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 6 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 7 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_recoup_deficit |  | fid |
| 2 | idx_tccit_recoup_deficit |  | forg,fskssqq,fskssqz |
