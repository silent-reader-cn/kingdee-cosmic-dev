# 费用归集单-凭证关系-pca_record_voucher_rel

## 费用归集单-凭证关系-主表 t_pca_rec_voucher_rel

- **表名称：** 费用归集单-凭证关系-主表
- **表名：** t_pca_rec_voucher_rel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvoucherid | 凭证id | int8 | 64 |  | √ | 0 | 凭证id |
| 3 | frecordid | 归集单id | int8 | 64 |  | √ | 0 | 归集单id |
| 4 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 期间 |
| 5 | frelrecordentryid | 关联归集单分录id | int8 | 64 |  | √ | 0 | 关联归集单分录id |
| 6 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | 项目核算主体 |
| 7 | frecordtype | 归集单类型 | varchar | 50 |  | √ | ' ' | 归集单类型,枚举: 1 :项目成本核算单 2 :公共费用归集单 |
| 8 | frecordentryid | 归集单分录id | int8 | 64 |  | √ | 0 | 归集单分录id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_rec_voucher_rel_ca |  | fcostaccountid |
| 2 | pk_pca_rec_voucher_rel |  | fid |
