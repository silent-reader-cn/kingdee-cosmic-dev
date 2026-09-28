# 公共配置-openapi_common_config

## 公共配置-主表 t_openapi_common

- **表名称：** 公共配置-主表
- **表名：** t_openapi_common

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 类型 | int4 | 32 |  | √ | 0 | 类型 |
| 3 | fenable | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: 0 :不可用 1 :可用 |
| 4 | fdesc | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 5 | fcomkey | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 6 | fcomvalue | 值 | varchar | 500 |  | √ | ' ' | 值 |
| 7 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_openapi_common |  | fid |
| 2 | idx_common_type |  | ftype,fcomkey |
