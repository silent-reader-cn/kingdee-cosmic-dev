# 不生成凭证-ai_nogenvoucher

## 不生成凭证-主表 t_ai_nogenvoucher

- **表名称：** 不生成凭证-主表
- **表名：** t_ai_nogenvoucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsourcebillstatus | 源单据状态 | varchar | 50 |  | √ | ' ' | 源单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdisplayname | 源系统 | varchar | 50 |  | √ | ' ' | 源系统 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fsourcebillid | 源单据id | int8 | 64 |  | √ | 0 | 源单据id |
| 12 | fsourcebillno | 源单据编号 | varchar | 50 |  | √ | ' ' | 源单据编号 |
| 13 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcomefrom | 源系统编码 | varchar | 50 |  | √ | ' ' | 源系统编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_nogenvoucher |  | fid |
| 2 | index_nogenvoucher_sourcebill |  | fsourcebillid |
