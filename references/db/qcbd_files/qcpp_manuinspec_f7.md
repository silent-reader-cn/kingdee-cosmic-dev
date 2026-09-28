# 生产检验单单头F7-qcpp_manuinspec_f7

## 生产检验单单头F7-主表 t_qcpp_inspbill

- **表名称：** 生产检验单单头F7-主表
- **表名：** t_qcpp_inspbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcomment | fcomment | varchar | 512 |  | √ | '' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fisyieldrecieve | fisyieldrecieve | bpchar | 1 |  | √ | '0' |  |
| 8 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 9 | finspectorid | finspectorid | int8 | 64 |  | √ | 0 |  |
| 10 | fconfirmauxpty | fconfirmauxpty | int4 | 32 |  | √ | 0 |  |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | finspestartdate | finspestartdate | timestamp | 0 |  |  | null |  |
| 13 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 14 | fprocessorg | fprocessorg | int8 | 64 |  | √ | 0 |  |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fprintcount | fprintcount | int4 | 32 |  | √ | 0 |  |
| 17 | finspeenddate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 18 | fjoininspectflag | fjoininspectflag | bpchar | 1 |  | √ | '0' |  |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 21 | finspedeptid | finspedeptid | int8 | 64 |  | √ | 0 |  |
| 22 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcpp_inspbill |  | fid |
| 2 | idx_qcpp_inspbill_fbillno |  | fbillno |
| 3 | idx_qcpp_inspbill_fcreatetime |  | fcreatetime |
