# 慢接口统计-openapi_costdata

## 慢接口统计-主表 t_openapi_costdata

- **表名称：** 慢接口统计-主表
- **表名：** t_openapi_costdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapiname | API名称 | varchar | 100 |  | √ | ' ' | API名称 |
| 3 | favgcost | 平均耗时(ms) | int8 | 64 |  | √ | 0 | 平均耗时(ms) |
| 4 | fmaxcost | 最大响应时间(ms) | int8 | 64 |  | √ | 0 | 最大响应时间(ms) |
| 5 | fcreatetime | 统计时间 | timestamp | 0 |  |  | null | 统计时间 |
| 6 | fapiid | apiId | int8 | 64 |  | √ | 0 | apiId |
| 7 | furl | 请求地址 | varchar | 400 |  | √ | ' ' | 请求地址 |
| 8 | fcount | 慢接口次数 | int8 | 64 |  | √ | 0 | 慢接口次数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_costdata_createtime |  | fcreatetime |
| 2 | pk_t_openapi_costdata |  | fid |
