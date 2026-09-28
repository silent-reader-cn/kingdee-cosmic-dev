# 项目发货通知单F7-mpm_projdelivernotice_f7

## 项目发货通知单F7-主表 t_mpm_delivernotice

- **表名称：** 项目发货通知单F7-主表
- **表名：** t_mpm_delivernotice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvgroupid | finvgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 4 | fterminatedate | fterminatedate | timestamp | 0 |  |  | null |  |
| 5 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fclosedate | fclosedate | timestamp | 0 |  |  | null |  |
| 7 | ftransactepathid | ftransactepathid | int8 | 64 |  | √ | 0 |  |
| 8 | ftransportstatus | ftransportstatus | bpchar | 1 |  | √ | 'A' |  |
| 9 | fbiztime | 通知日期 | timestamp | 0 |  |  | null | 通知日期 |
| 10 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | fterminatestatus | fterminatestatus | varchar | 5 |  | √ | ' ' |  |
| 12 | fdeliverdeptid | fdeliverdeptid | int8 | 64 |  | √ | 0 |  |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fterminaterid | fterminaterid | int8 | 64 |  | √ | 0 |  |
| 15 | fasyncstatus | fasyncstatus | bpchar | 1 |  | √ | 'B' |  |
| 16 | fisvirtualbill | fisvirtualbill | bpchar | 1 |  | √ | '0' |  |
| 17 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 18 | fdeliveroperatorid | fdeliveroperatorid | int8 | 64 |  | √ | 0 |  |
| 19 | fcloserid | fcloserid | int8 | 64 |  | √ | 0 |  |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fheadprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | fencasestatus | fencasestatus | bpchar | 1 |  | √ | 'A' |  |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fisprojectbegin | fisprojectbegin | bpchar | 1 |  | √ | '0' |  |
| 27 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 28 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 29 | fdeliverpatternid | fdeliverpatternid | int8 | 64 |  | √ | 0 |  |
| 30 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 33 | fclosestatus | fclosestatus | varchar | 5 |  | √ | ' ' |  |
| 34 | fclosemanual | fclosemanual | bpchar | 1 |  | √ | '0' |  |
| 35 | flogistics | flogistics | bpchar | 1 |  | √ | '0' |  |
| 36 | fdeliveruserid | 发货负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 38 | fdeliverorgid | 发货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fpointstatus | fpointstatus | bpchar | 1 |  | √ | 'A' |  |
| 40 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_delivernotice_bilno |  | fbillno |
| 2 | pk_mpm_delivernotice |  | fid |
| 3 | idx_mpm_delinotice_biztim |  | fbiztime |
