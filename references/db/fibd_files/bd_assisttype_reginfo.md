# 核算维度注册信息-bd_assisttype_reginfo

## 核算维度注册信息-主表 t_bd_assisttype_reginfo

- **表名称：** 核算维度注册信息-主表
- **表名：** t_bd_assisttype_reginfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountfield | 科目字段名 | varchar | 30 |  | √ | ' ' | 科目字段名 |
| 3 | fmetadata | 元数据 | varchar | 30 |  | √ | ' ' | 业务对象 bos_objecttype |
| 4 | frowidfield | 特殊表单行ID字段名 | varchar | 30 |  | √ | ' ' | 特殊表单行ID字段名 |
| 5 | fassgrpfield | 核算维度字段名 | varchar | 30 |  | √ | ' ' | 核算维度字段名 |
| 6 | fsubentryassgrp | 子分录核算维度字段名 | varchar | 30 |  | √ | ' ' | 子分录核算维度字段名 |
| 7 | fentryname | 分录标识 | varchar | 30 |  | √ | ' ' | 分录标识 |
| 8 | fpluginname | 插件名 | varchar | 255 |  | √ | ' ' | 插件名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_assisttype_reginfo |  | fmetadata |
| 2 | pk_t_bd_assisttype_reginfo |  | fid |
