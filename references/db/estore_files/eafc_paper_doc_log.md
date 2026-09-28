# 纸档整理日志-eafc_paper_doc_log

## 纸档整理日志-主表 tk_eafc_paper_doc_log

- **表名称：** 纸档整理日志-主表
- **表名：** tk_eafc_paper_doc_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_title | 题名 | varchar | 255 |  | √ | ' ' | 题名 |
| 3 | fk_eafc_paper_manage_mode | 装盒方式 | varchar | 50 |  | √ | ' ' | 装盒方式,枚举: 1 :按卷装盒 2 :按件装盒 |
| 4 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  | √ | 0 | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 5 | fk_eafc_operator | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fk_eafc_box | 盒子ID | int8 | 64 |  | √ | 0 | 盒子ID |
| 7 | fk_eafc_number | 编号 | varchar | 255 |  | √ | ' ' | 编号 |
| 8 | fk_eafc_operation_time | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 9 | fk_eafc_base_bill | 件ID | int8 | 64 |  | √ | 0 | 件ID |
| 10 | fk_eafc_organization_way | 整理方式 | varchar | 50 |  | √ | ' ' | 整理方式,枚举: 1 :装盒 2 :解绑盒号 3 :上架 4 :下架 5 :移除库房 |
| 11 | fk_eafc_volume | 卷ID | int8 | 64 |  | √ | 0 | 卷ID |
| 12 | fk_eafc_box_title | 盒子题名 | varchar | 255 |  | √ | ' ' | 盒子题名 |
| 13 | fk_eafc_business_type | 分类 | int8 | 64 |  | √ | 0 | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 14 | fk_eafc_box_num | 盒号 | varchar | 255 |  | √ | ' ' | 盒号 |
| 15 | fk_eafc_box_serial | 盒内序号 | int8 | 64 |  | √ | 0 | 盒内序号 |
| 16 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  | √ | 0 | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__tk_eafc_paper_doc_log |  | fid |
