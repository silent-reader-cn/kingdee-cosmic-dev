# 列表统计项-bos_nocode_statconfig

## 列表统计项-主表 t_nocode_statconfig

- **表名称：** 列表统计项-主表
- **表名：** t_nocode_statconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatinfo | 列表统计项 | text | 0 |  |  | null | 列表统计项 |
| 3 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 8 | fformid | 表单id | varchar | 50 |  | √ | ' ' | 表单id |
| 9 | fappid | 应用id | varchar | 50 |  | √ | ' ' | 应用id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_nocode_statconfig |  | fid |
| 2 | idx_nc_scon_afu |  | fappid,fformid,fuserid |
