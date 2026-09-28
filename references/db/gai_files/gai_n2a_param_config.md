# 参数-gai_n2a_param_config

## 参数-主表 t_gai_nl2api_param_cfg

- **表名称：** 参数-主表
- **表名：** t_gai_nl2api_param_cfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 参数名 | varchar | 50 |  | √ | ' ' | 参数名 |
| 3 | fvalue | 参数值 | varchar | 2000 |  | √ | ' ' | 参数值 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fvalue_tag | 参数值_详情 | text | 0 |  |  | null | 参数值_详情 |
| 6 | ftype | 参数类型 | varchar | 50 |  | √ | ' ' | 参数类型,枚举: String :文本 Integer :整数 DateTime :日期/时间 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fdesc | 参数说明 | varchar | 255 |  | √ | ' ' | 参数说明 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_n2a_param_cfg_fname |  | fname |
| 2 | pk_t_gai_nl2api_param_cfg |  | fid |
