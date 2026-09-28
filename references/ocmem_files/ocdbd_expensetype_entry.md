# 费用行类型分录-ocdbd_expensetype_entry

## 费用行类型分录-主表 t_ocdbd_subexpensetype

- **表名称：** 费用行类型分录-主表
- **表名：** t_ocdbd_subexpensetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 费用行类型 | int8 | 64 |  | √ | 0 | 费用行类型 ocdbd_entryexpensetype |
| 2 | fwriteoff | fwriteoff | bpchar | 1 |  | √ | 'A' |  |
| 3 | fwriteoffno | 核销方式编码 | varchar | 80 |  | √ | ' ' | 核销方式编码 |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fwriteoffname | 核销方式名称 | varchar | 80 |  | √ | ' ' | 核销方式名称 |
| 6 | fentryname | 行类型名称 | varchar | 80 |  | √ | ' ' | 行类型名称 |
| 7 | fmustinputtype | 产品必录信息 | bpchar | 1 |  | √ | ' ' | 产品必录信息,枚举: A :录入产品数量单价 B :录入产品和申请金额 |
| 8 | fentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |
| 9 | fwriteoffaccountid | 报销转结到关联账户 | int8 | 64 |  | √ | 0 | 资金账户 ocdbd_incentiveaccount |
| 10 | ffeecashtypeid | 费用兑付方式 | int8 | 64 |  | √ | 0 | 费用兑付方式 ocdbd_feecashtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_subexpensetype |  | fentryid |
| 2 | idx_ocdbd_subexpensetype_fid |  | fid |
