# 纳税企业通用传递单销项-tcvat_yzhz_cddxxse

## 纳税企业通用传递单销项-主表 t_tcvat_yzhz_cddxxse

- **表名称：** 纳税企业通用传递单销项-主表
- **表名：** t_tcvat_yzhz_cddxxse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :合计 2 :2 |
| 3 | fysxm | 应税项目 | varchar | 400 |  | √ | ' ' | 应税项目 |
| 4 | fyzl | 预征率 | numeric | 20 | 4 | √ | 0 | 预征率 |
| 5 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 6 | fynse | 应纳税额 | numeric | 20 | 2 | √ | 0 | 应纳税额 |
| 7 | fyjse | 已缴税额 | numeric | 20 | 2 | √ | 0 | 已缴税额 |
| 8 | fewblname | 二维表行名称 | varchar | 50 |  | √ | ' ' | 二维表行名称 |
| 9 | fysxxsr | 应税销售收入 | numeric | 20 | 2 | √ | 0 | 应税销售收入 |
| 10 | ffpse | 分配税额 | numeric | 20 | 2 | √ | 0 | 分配税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_yzhz_cddxxse |  | fid |
| 2 | idx_cdd_fsbbid |  | fsbbid,fewblxh |
