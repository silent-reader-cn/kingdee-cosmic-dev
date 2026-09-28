# 即征即退资格备案-tcvat_jzjt_filing

## 即征即退资格备案-主表 t_tcvat_jzjt_filing

- **表名称：** 即征即退资格备案-主表
- **表名：** t_tcvat_jzjt_filing

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjmxmmc | 减免项目名称 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |
| 3 | fbayxqq | 备案有效期起 | timestamp | 0 |  |  | null | 备案有效期起 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fnsrsbno | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fbayxqz | 备案有效期止 | timestamp | 0 |  |  | null | 备案有效期止 |
| 9 | forg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_jzjt_filing |  | fid |
| 2 | jzjt_filing_forg_idx |  | forg,fjmxmmc,fbayxqq,fbayxqz |
| 3 | idx_tcvat_jzjt_filing_forg |  | forg,fbillno |
