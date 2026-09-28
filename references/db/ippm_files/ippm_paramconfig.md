# 报告参数配置-ippm_paramconfig

## 报告参数配置-主表 t_ippm_paramconfig

- **表名称：** 报告参数配置-主表
- **表名：** t_ippm_paramconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparamdatasourceid | 参数数据源 | int8 | 64 |  | √ | 0 | [报告参数数据源 ippm_paramdatasource](../ippm_files/ippm_paramdatasource.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fparamvaluejson_tag | 参数配置JSON_详情 | text | 0 |  |  | null | 参数配置JSON_详情 |
| 8 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fparamvaluejson | 参数配置JSON | varchar | 255 |  | √ | ' ' | 参数配置JSON |
| 10 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ippm_paramconfig |  | fid |
| 2 | idx_ippm_paramconfig |  | fnumber |
