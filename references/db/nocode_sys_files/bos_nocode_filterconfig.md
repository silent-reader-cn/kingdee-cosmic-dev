# 筛选项配置-bos_nocode_filterconfig

## 筛选项配置-主表 t_nocode_filterconfig

- **表名称：** 筛选项配置-主表
- **表名：** t_nocode_filterconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 7 | ffilterrows | 筛选配置项 | text | 0 |  |  | null | 筛选配置项 |
| 8 | fformid | 表单id | varchar | 50 |  | √ | ' ' | 表单id |
| 9 | fappid | 应用id | varchar | 50 |  | √ | ' ' | 应用id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_nocode_filterconfig |  | fid |
| 2 | idx_nc_fc_afu |  | fappid,fformid,fuserid |
