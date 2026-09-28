# 供应组织待分配记录表-mds_siterecord

## 供应组织待分配记录表-主表 t_mds_siterecord

- **表名称：** 供应组织待分配记录表-主表
- **表名：** t_mds_siterecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fundistqty | fundistqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstockoutqty | 累计出库数量 | numeric | 23 | 10 | √ | 0 | 累计出库数量 |
| 7 | frecorddate | 记录日期 | timestamp | 0 |  |  | null | 记录日期 |
| 8 | fsourceqty | 原订单数量 | numeric | 23 | 10 | √ | 0 | 原订单数量 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | ftrackid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 11 | fsaleorg | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbilltag | 单据标识 | varchar | 50 |  | √ | ' ' | 单据标识 |
| 16 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fbillunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fsiteschemeid | 供应组织分配方案编码 | int8 | 64 |  | √ | 0 | [供应组织分配方案定义 mds_siteschemedef](../mds_files/mds_siteschemedef.md) |
| 21 | fconfigid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 22 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 23 | fbillrowno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 24 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_siterecord_matno |  | fmaterialid |
| 2 | pk_mds_siterecord |  | fid |
| 3 | idx_mds_siterecord_no |  | fsiteschemeid |
