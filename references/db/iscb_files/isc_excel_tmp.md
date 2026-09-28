# excel文件导入-isc_excel_tmp

## excel文件导入-主表 t_iscb_excel_tmp

- **表名称：** excel文件导入-主表
- **表名：** t_iscb_excel_tmp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fitemclassid | 资源 | int8 | 64 |  | √ | 0 | 值转换规则 isc_value_conver_rule |
| 7 | fitemclasstype | 资源类型 | varchar | 100 |  | √ | ' ' | 资源类型,枚举: isc_value_conver_rule :值转换规则 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_excel_frule |  | fitemclassid |
| 2 | pk_t_iscb_excel_tmp |  | fid |
