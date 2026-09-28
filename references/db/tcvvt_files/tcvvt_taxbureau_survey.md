# 税局版重点税源表（企业景气调查表）-tcvvt_taxbureau_survey

## 税局版重点税源表（企业景气调查表）-主表 t_tcvvt_taxbureau_survey

- **表名称：** 税局版重点税源表（企业景气调查表）-主表
- **表名：** t_tcvvt_taxbureau_survey

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 指标名称 | varchar | 50 |  | √ | ' ' | 指标名称,枚举: 1 :1.营业收入（万元） 2 :2.利润总额（万元） 3 :3.出口销售额（万元） 4 :4.新增固定资产（万元） 5 :5.国内税收合计（万元）(41=42+43+44+45+46) 5.1 :其中：增值税（万元） 5.2 :消费税（万元） 5.3 :企业所得税（万元） 5.4 :个人所得税（万元） 5.5 :其他税收（万元） |
| 3 | ftbsnysjwc | 上年下月实际 | numeric | 23 | 10 | √ | 0 | 上年下月实际 |
| 4 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 7 | ftbnqnyc | 本年全年预测 | numeric | 23 | 10 | √ | 0 | 本年全年预测 |
| 8 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 9 | ftbsnqnsj | 上年全年实际 | numeric | 23 | 10 | √ | 0 | 上年全年实际 |
| 10 | fewblname | 二维表行名称 | varchar | 200 |  | √ | ' ' | 二维表行名称 |
| 11 | ftbnyyc | 本年下月预测 | numeric | 23 | 10 | √ | 0 | 本年下月预测 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_taxbureau_surorg |  | forgid,fewblxh |
| 2 | pk_tcvvt_taxbureau_survey |  | fid |
