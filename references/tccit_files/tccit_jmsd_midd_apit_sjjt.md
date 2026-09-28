# 税金计提减免所得税后台表-tccit_jmsd_midd_apit_sjjt

## 税金计提减免所得税后台表-主表 t_tccit_jmsd_midd_ap_sjjt

- **表名称：** 税金计提减免所得税后台表-主表
- **表名：** t_tccit_jmsd_midd_ap_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行次 | varchar | 50 |  | √ | ' ' | 行次 |
| 3 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 4 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 5 | fsumamount | 累计减免税额 | numeric | 23 | 10 | √ | 0 | 累计减免税额 |
| 6 | fitem | 优惠项目 | int8 | 64 |  | √ | 0 | 优惠项目（树） tpo_discount_tree |
| 7 | fitemname | 减免所得税额优惠事项 | varchar | 200 |  | √ | ' ' | 减免所得税额优惠事项 |
| 8 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 9 | fparentcode | 父编码 | varchar | 50 |  | √ | ' ' | 父编码 |
| 10 | fcode | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_jmsd_midd_ap_sjjt |  | fid |
| 2 | idx_tccit_jmsd_midd_ap_sjjt_1 |  | forgid,fskssqq,fskssqz |
