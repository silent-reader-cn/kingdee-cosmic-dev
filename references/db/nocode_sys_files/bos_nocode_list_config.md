# 表单列表配置项-bos_nocode_list_config

## 表单列表配置项-主表 t_nocode_list_config

- **表名称：** 表单列表配置项-主表
- **表名：** t_nocode_list_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flockedfields | 冻结列 | text | 0 |  |  | null | 冻结列 |
| 3 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 4 | fselectedfields | 已选字段 | text | 0 |  |  | null | 已选字段 |
| 5 | fformid | 表单id | varchar | 50 |  | √ | ' ' | 表单id |
| 6 | fappid | 应用id | varchar | 50 |  | √ | ' ' | 应用id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_nocode_list_config |  | fid |
| 2 | idx_nc_lc_afu |  | fappid,fformid,fuserid |
