# 卷册与文件关联关系表-eafc_volume_book_bill

## 卷册与文件关联关系表-主表 tk_eafc_volume_book_bill

- **表名称：** 卷册与文件关联关系表-主表
- **表名：** tk_eafc_volume_book_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_base_billid | 公共单据id | int8 | 64 |  |  | null | 公共单据id |
| 3 | forgid | 组织 | int8 | 64 |  |  | null | 组织 |
| 4 | fk_eafc_book_type | 账簿类型 | int8 | 64 |  |  | null | 账簿类型 |
| 5 | fk_eafc_book_relationid | 册id | int8 | 64 |  |  | null | 册id |
| 6 | fk_eafc_volume_relationid | 卷id | int8 | 64 |  |  | null | 卷id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_volume_book_bill |  | fid |
