# 预缴纳税总览表-tccit_seasonal_calc_det

## 预缴纳税总览表-主表 t_tccit_seasonal_calc_det

- **表名称：** 预缴纳税总览表-主表
- **表名：** t_tccit_seasonal_calc_det

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行次 | varchar | 50 |  | √ | ' ' | 行次 |
| 3 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型 |
| 4 | fmypkid | 行id | int8 | 64 |  | √ | 0 | 行id |
| 5 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 6 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 1 :总机构类型 2 :分支类型 |
| 7 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 8 | fsumamount | 累计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计金额 |
| 9 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 10 | fskssqq | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 11 | fissmall | 是否小微企业 | bpchar | 1 |  | √ | '0' | 是否小微企业 |
| 12 | fmyparentid | 父级id | int8 | 64 |  | √ | 0 | 父级id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_seasonal_calc_det |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_seasonal_calc_det |  | fid |
