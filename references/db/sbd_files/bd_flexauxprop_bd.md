# 辅助属性值纵表（基础资料类型）-bd_flexauxprop_bd

## 辅助属性值纵表（基础资料类型）-主表 t_bd_flexauxpropdata_bd

- **表名称：** 辅助属性值纵表（基础资料类型）-主表
- **表名：** t_bd_flexauxpropdata_bd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 横表 | int8 | 64 |  | √ | 0 | 辅助属性值 bd_flexauxprop |
| 2 | fvalue | 辅助属性值 | int8 | 64 |  | √ | 0 | 辅助属性值 |
| 3 | fflexfield | 辅助属性类型 | varchar | 30 |  | √ | ' ' | 辅助属性类型 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_flexauxpropdata_bd_pkey |  | fentryid |
| 2 | idx_bd_auxptybd_auxptybd |  | fflexfield,fvalue,fid |
