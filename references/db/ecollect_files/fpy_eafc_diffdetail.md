# 差异明细-fpy_eafc_diffdetail

## 差异明细-主表 tk_eafc_diff_detail

- **表名称：** 差异明细-主表
- **表名：** tk_eafc_diff_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fk_eafc_file_id | ID | varchar | 64 |  | √ | ' ' | ID |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fk_eafc_period | 会计期间 | varchar | 50 |  | √ | ' ' | 会计期间 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  | √ | 0 | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 9 | fk_eafc_should_status | 应归 | varchar | 50 |  | √ | '0' | 应归,枚举: 1 :正常 0 :异常 |
| 10 | fk_eafc_file_sign | 文件题名 | varchar | 500 |  | √ | ' ' | 文件题名 |
| 11 | fk_eafc_describe | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |
| 12 | fk_eafc_execute_status | 执行 | varchar | 50 |  | √ | '0' | 执行,枚举: 1 :正常 0 :异常 |
| 13 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fk_eafc_receive_status | 接收 | varchar | 50 |  | √ | '0' | 接收,枚举: 1 :正常 0 :异常 |
| 16 | fk_eafc_file_code | 文件编号 | varchar | 500 |  | √ | ' ' | 文件编号 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fk_eafc_period_year | 会计期间-年份 | varchar | 50 |  | √ | ' ' | 会计期间-年份 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  | √ | 0 | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 21 | fk_eafc_business | 三级门类 | int8 | 64 |  | √ | 0 | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_diff_period_year_bus |  | fk_eafc_period_year,fk_eafc_business |
| 2 | pk_eafc_diff_detail |  | fid |
| 3 | idx_diff_period_org_type_bus |  | fk_eafc_period,fk_eafc_arcorg,fk_eafc_book_type,fk_eafc_business,fk_eafc_file_id |
