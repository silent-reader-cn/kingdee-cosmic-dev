# 快速搜索-bos_cbs_qs_config

## 快速搜索-主表 t_ft_qs_config

- **表名称：** 快速搜索-主表
- **表名：** t_ft_qs_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftimingsequence | 时序字段 | varchar | 100 |  | √ | ' ' | 时序字段,枚举: |
| 3 | fentitynumber | 实体对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 4 | fregion | 目标地址 | varchar | 30 |  | √ | ' ' | 目标地址,枚举: quicksearch :quicksearch |
| 5 | fenable | 是否启用 | bpchar | 1 |  | √ | ' ' | 是否启用 |
| 6 | fentityfields | 同步字段 | varchar | 1000 |  | √ | ' ' | 同步字段,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ft_qs_config |  | fregion,fentitynumber |
| 2 | pk_ft_qs_config |  | fid |
