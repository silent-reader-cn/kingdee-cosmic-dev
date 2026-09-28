# 批号/序列号最大流水号-bd_lotcoderule_maxserial

## 批号/序列号最大流水号-主表 t_bd_lotmaxserial

- **表名称：** 批号/序列号最大流水号-主表
- **表名：** t_bd_lotmaxserial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaxserial | 最大流水号 | int8 | 64 |  | √ | 0 | 最大流水号 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | flotcoderuleid | 批号编码规则 | int8 | 64 |  | √ | 0 | [供应链编码规则 bd_lotcoderule](../sbd_files/bd_lotcoderule.md) |
| 5 | faccordprop | 流水号依据属性 | varchar | 255 |  |  | null | 流水号依据属性 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_lotmaxserial_pkey |  | fid |
| 2 | idx_bd_lotmaxserial_lotrule |  | flotcoderuleid |
