# 计息方法设置-ifm_intcalcwaysetting

## 计息方法设置-主表 t_ifm_intcalcwaysetting

- **表名称：** 计息方法设置-主表
- **表名：** t_ifm_intcalcwaysetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fintcaclway | fintcaclway | bpchar | 30 |  | √ | ' ' |  |
| 3 | fintcalcway | 计息方法 | varchar | 30 |  | √ | ' ' | 计息方法,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ifm_intcalcwaysetting |  | fid |
| 2 | idx_ifm_intcalcwaysetting |  | fintcaclway |
