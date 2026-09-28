# 高新认定文档管理-rdem_gxrd_docmanage

## 高新认定文档管理-主表 t_rdem_gxrd_docmanage

- **表名称：** 高新认定文档管理-主表
- **表名：** t_rdem_gxrd_docmanage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | forgfield | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdocumenttag | 文档标签 | int8 | 64 |  | √ | 0 | [文档标签 rdem_document_tag](../rdem_files/rdem_document_tag.md) |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdocname | 文档名称 | varchar | 200 |  | √ | ' ' | 文档名称 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fyear | 年度 | timestamp | 0 |  |  | null | 年度 |
| 12 | furl | 文件路径 | varchar | 1000 |  | √ | ' ' | 文件路径 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillno | 文档编号 | varchar | 30 |  | √ | ' ' | 文档编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_gxrd_docmanage |  | fid |
| 2 | idx_rdem_gxrd_docmanage_m0 |  | fbillno |
