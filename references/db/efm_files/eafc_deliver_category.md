# 移交种类-eafc_deliver_category

## 移交种类-主表 tk_eafc_deliver_category

- **表名称：** 移交种类-主表
- **表名：** tk_eafc_deliver_category

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_volume_num | 案卷数 | int4 | 32 |  | √ | 0 | 案卷数 |
| 3 | fk_eafc_category_name | 类别名称 | varchar | 50 |  | √ | ' ' | 类别名称 |
| 4 | fk_eafc_category_no | 类别号 | varchar | 50 |  | √ | ' ' | 类别号 |
| 5 | fk_eafc_file_num | 文件数 | int4 | 32 |  | √ | 0 | 文件数 |
| 6 | fk_eafc_contain_entity | 是否存在实物 | varchar | 50 |  | √ | ' ' | 是否存在实物,枚举: 1 :否 2 :是 |
| 7 | fk_eafc_apply_no | 申请单号 | varchar | 50 |  | √ | ' ' | 申请单号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eafc_deliver_apply_no |  | fk_eafc_apply_no |
| 2 | pk_eafc_deliver_category |  | fid |
