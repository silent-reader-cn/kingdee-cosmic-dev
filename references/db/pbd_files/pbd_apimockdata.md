# 接口模拟数据-pbd_apimockdata

## 接口模拟数据-主表 t_pbd_apimockdata

- **表名称：** 接口模拟数据-主表
- **表名：** t_pbd_apimockdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fresult_tag | 结果_详情 | text | 0 |  |  | null | 结果_详情 |
| 3 | fparams_tag | 参数匹配_详情 | text | 0 |  |  | null | 参数匹配_详情 |
| 4 | fextsysapi | 接口配置 | int8 | 64 |  | √ | 0 | [外部系统API pbd_extsys_api](../pbd_files/pbd_extsys_api.md) |
| 5 | fdynamic_value_fields | 动态值字段 | varchar | 50 |  | √ | ' ' | 动态值字段 |
| 6 | fparams | 参数匹配 | text | 0 |  |  | null | 参数匹配 |
| 7 | fresult | 结果 | text | 0 |  |  | null | 结果 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pbd_apimockdata |  | fid |
| 2 | idx_pbd_apimockdata_fextsysapi |  | fextsysapi |
