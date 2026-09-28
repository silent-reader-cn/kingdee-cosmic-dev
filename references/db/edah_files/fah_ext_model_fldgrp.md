# 数据字段分组定义-fah_ext_model_fldgrp

## 数据字段分组定义-主表 t_fah_ext_modfldgrp

- **表名称：** 数据字段分组定义-主表
- **表名：** t_fah_ext_modfldgrp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flevel | 级别 | int4 | 32 |  | √ | 0 | 级别 |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子,枚举: |
| 4 | fparentid | 上级节点 | int8 | 64 |  | √ | 0 | [数据字段分组定义 fah_ext_model_fldgrp](../edah_files/fah_ext_model_fldgrp.md) |
| 5 | fmodelid | 模型 | int8 | 64 |  | √ | 0 | [异构数据对接模型 fah_ext_datamodel](../edah_files/fah_ext_datamodel.md) |
| 6 | flongnumber | 长编码 | varchar | 62 |  | √ | ' ' | 长编码 |
| 7 | fseq | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 8 | fgroupnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 9 | ftablename | 表名 | varchar | 30 |  | √ | ' ' | 表名 |
| 10 | fgrouptype | 分组类型 | bpchar | 1 |  | √ | ' ' | 分组类型 |
| 11 | fgroupname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fah_ext_modfldgrp |  | fid |
| 2 | idx_fah_ext_modfldgrp_mid |  | fmodelid |
