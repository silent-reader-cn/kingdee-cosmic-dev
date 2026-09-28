# 需方记录表-mds_requestrecord

## 需方记录表-主表 t_mds_requestrecord

- **表名称：** 需方记录表-主表
- **表名：** t_mds_requestrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsetoffqty | 原单数量 | numeric | 23 | 10 | √ | 0.0000000000 | 原单数量 |
| 3 | ftransferid | 实体字段映射ID | int8 | 64 |  | √ | 0 | 实体字段映射ID |
| 4 | fsetid | 预测冲减定义 | int8 | 64 |  | √ | 0 | [预测冲减定义 mds_setoffsetting](../mds_files/mds_setoffsetting.md) |
| 5 | fmatverid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :正常 B :已关闭 |
| 8 | fdeleverydate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 9 | flogid | 冲减日志ID | int8 | 64 |  | √ | 0 | 冲减日志ID |
| 10 | fsxh | 顺序号 | int8 | 64 |  | √ | 0 | 顺序号 |
| 11 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | frecorddate | 记录日期 | timestamp | 0 |  |  | null | 记录日期 |
| 14 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 15 | fbno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | ftrackid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 18 | fepd | 预计交单日期 | timestamp | 0 |  |  | null | 预计交单日期 |
| 19 | faccoutqty | 累计已出库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计已出库数量 |
| 20 | fdefineconfig | 自定义配置字符 | varchar | 50 |  | √ | ' ' | 自定义配置字符 |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fmateriel | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 23 | fsaleorderoutid | 销售出库单ID | int8 | 64 |  | √ | 0 | 销售出库单ID |
| 24 | fqty | 单据数量 | numeric | 23 | 10 | √ | 0.0000000000 | 单据数量 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fbilltag | 单据标识 | varchar | 50 |  | √ | ' ' | 单据标识 |
| 27 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 28 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | ftoolid | 预测冲减运算 | int8 | 64 |  | √ | 0 | [预测冲减运算 mds_setofftool](../mds_files/mds_setofftool.md) |
| 31 | fbillunit | 单据计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 32 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 33 | fbilltypename | 单据类型名称 | varchar | 50 |  | √ | ' ' | 单据类型名称 |
| 34 | fgroupno | 组号 | int4 | 32 |  | √ | 0 | 组号 |
| 35 | frpd | 要求交单日期 | timestamp | 0 |  |  | null | 要求交单日期 |
| 36 | fisbotp | 预测单下推关联数据 | bpchar | 1 |  | √ | '0' | 预测单下推关联数据 |
| 37 | fconfigid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 38 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 39 | fbom | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 40 | fbillrowno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 41 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 42 | fbillorg | 单据组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 45 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 46 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_requestrecord_setmid |  | fsetid,fmateriel |
| 2 | pk_mds_requestrecord |  | fid |
| 3 | idx_mds_requestrecord_mat |  | fmateriel |
