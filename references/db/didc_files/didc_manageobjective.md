# 目标管理-didc_manageobjective

## 目标值-子表 t_didc_targetentry

- **表名称：** 目标值-子表
- **表名：** t_didc_targetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubquarter2 | Q2 | numeric | 23 | 10 | √ | 0 | Q2 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fsubmonth10 | 10月 | numeric | 23 | 10 | √ | 0 | 10月 |
| 4 | fsubquarter3 | Q3 | numeric | 23 | 10 | √ | 0 | Q3 |
| 5 | fsubmonth11 | 11月 | numeric | 23 | 10 | √ | 0 | 11月 |
| 6 | fsubquarter4 | Q4 | numeric | 23 | 10 | √ | 0 | Q4 |
| 7 | fsubmonth12 | 12月 | numeric | 23 | 10 | √ | 0 | 12月 |
| 8 | fsubmonth7 | 7月 | numeric | 23 | 10 | √ | 0 | 7月 |
| 9 | fsubmonth6 | 6月 | numeric | 23 | 10 | √ | 0 | 6月 |
| 10 | fsubmonth9 | 9月 | numeric | 23 | 10 | √ | 0 | 9月 |
| 11 | fsubmonth8 | 8月 | numeric | 23 | 10 | √ | 0 | 8月 |
| 12 | fsubmonth3 | 3月 | numeric | 23 | 10 | √ | 0 | 3月 |
| 13 | fsubmonth2 | 2月 | numeric | 23 | 10 | √ | 0 | 2月 |
| 14 | fsubmonth5 | 5月 | numeric | 23 | 10 | √ | 0 | 5月 |
| 15 | fsubmonth4 | 4月 | numeric | 23 | 10 | √ | 0 | 4月 |
| 16 | fdimensionvalue | 维度值 | varchar | 255 |  | √ | ' ' | 维度值 |
| 17 | fsubmonth1 | 1月 | numeric | 23 | 10 | √ | 0 | 1月 |
| 18 | fsubquarter1 | Q1 | numeric | 23 | 10 | √ | 0 | Q1 |
| 19 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 21 | fsubyear | 年 | numeric | 23 | 10 | √ | 0 | 年 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_targetentry |  | fentryid |
| 2 | pk_didc_targetentry |  | fdetailid |

---

## 目标管理-主表 t_didc_manageobjective

- **表名称：** 目标管理-主表
- **表名：** t_didc_manageobjective

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frulevalue | 显示规则内容 | varchar | 255 |  | √ | ' ' | 显示规则内容 |
| 3 | fquarter2 | 第二季度 | numeric | 23 | 10 | √ | 0 | 第二季度 |
| 4 | fquarter3 | 第三季度 | numeric | 23 | 10 | √ | 0 | 第三季度 |
| 5 | fquarter4 | 第四季度 | numeric | 23 | 10 | √ | 0 | 第四季度 |
| 6 | findexid | 所属指标 | int8 | 64 |  | √ | 0 | [数智指标 didc_indexcatalogue](../didc_files/didc_indexcatalogue.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |
| 8 | fquarter1 | 第一季度 | numeric | 23 | 10 | √ | 0 | 第一季度 |
| 9 | fmonth5 | 5月 | numeric | 23 | 10 | √ | 0 | 5月 |
| 10 | fmonth4 | 4月 | numeric | 23 | 10 | √ | 0 | 4月 |
| 11 | fmonth3 | 3月 | numeric | 23 | 10 | √ | 0 | 3月 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fisquarter | 季 | bpchar | 1 |  | √ | ' ' | 季 |
| 14 | fmonth2 | 2月 | numeric | 23 | 10 | √ | 0 | 2月 |
| 15 | fmonth9 | 9月 | numeric | 23 | 10 | √ | 0 | 9月 |
| 16 | fmonth10 | 10月 | numeric | 23 | 10 | √ | 0 | 10月 |
| 17 | frulevalue_tag | 显示规则内容_详情 | text | 0 |  |  | null | 显示规则内容_详情 |
| 18 | fsum | 年度总值 | numeric | 23 | 10 | √ | 0 | 年度总值 |
| 19 | fmonth8 | 8月 | numeric | 23 | 10 | √ | 0 | 8月 |
| 20 | fmonth7 | 7月 | numeric | 23 | 10 | √ | 0 | 7月 |
| 21 | fmonth12 | 12月 | numeric | 23 | 10 | √ | 0 | 12月 |
| 22 | fmonth6 | 6月 | numeric | 23 | 10 | √ | 0 | 6月 |
| 23 | fmonth11 | 11月 | numeric | 23 | 10 | √ | 0 | 11月 |
| 24 | fdisplayrule | 进度显示规则 | varchar | 255 |  | √ | ' ' | 进度显示规则 |
| 25 | fmonth1 | 1月 | numeric | 23 | 10 | √ | 0 | 1月 |
| 26 | fbillno | 目标编码 | varchar | 50 |  | √ | ' ' | 目标编码 |
| 27 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fbillstatus | 目标状态 | varchar | 50 |  | √ | ' ' | 目标状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 30 | fcomparison | 对比条件 | varchar | 50 |  | √ | ' ' | 对比条件,枚举: schedule :按进度 numerical :按数值 |
| 31 | fismonth | 月 | bpchar | 1 |  | √ | ' ' | 月 |
| 32 | fauditdate | 审核日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 审核日期 |
| 33 | fyear | 目标年度 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 目标年度 |
| 34 | fisyear | 年 | bpchar | 1 |  | √ | ' ' | 年 |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_didc_manageobjective |  | fid |
| 2 | idx_didc_manageobjective |  | findexid |

---

## 维度-子表 t_didc_dimensionentry

- **表名称：** 维度-子表
- **表名：** t_didc_dimensionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 3 | fdimensionid | 维度id | varchar | 255 |  | √ | ' ' | 维度id |
| 4 | fdimensionname | 维度名称 | varchar | 255 |  | √ | ' ' | 维度名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_dimensionentry |  | fid |
| 2 | pk_didc_dimensionentry |  | fentryid |
