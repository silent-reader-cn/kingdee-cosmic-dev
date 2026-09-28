# 核算组织本位币设置-bd_accountingsys_base

## 核算组织本位币设置-主表 t_bd_accountingsys_base

- **表名称：** 核算组织本位币设置-主表
- **表名：** t_bd_accountingsys_base

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperiodtypeid | fperiodtypeid | int8 | 64 |  | √ | 0 |  |
| 3 | fbasecurrrencyid | 综合本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 5 | fbaseacctorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_accountingsys_base_pkey |  | fid |
| 2 | idx_bd_accountingsys_base_org |  | fbaseacctorgid |
