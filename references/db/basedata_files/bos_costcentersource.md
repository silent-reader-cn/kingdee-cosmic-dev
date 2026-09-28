# 成本中心来源-bos_costcentersource

## 成本中心来源-主表 t_bas_costcentersource

- **表名称：** 成本中心来源-主表
- **表名：** t_bas_costcentersource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 3 | fdataid | 来源数据 | int8 | 64 |  | √ | 0 | 来源数据 |
| 4 | fsourcetypeid | 来源类型 | int8 | 64 |  | √ | 0 | [来源类型 bos_costcentersourcetype](../basedata_files/bos_costcentersourcetype.md) |
| 5 | fseq | 整数 | int8 | 64 |  | √ | 0 | 整数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_costcentersource_pkey |  | fid |
| 2 | idx_bas_costcentersrc_typedata |  | fsourcetypeid,fdataid |
