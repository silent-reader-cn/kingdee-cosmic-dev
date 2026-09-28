# 供方记录表-mds_providerrecord

## 供方记录表-主表 t_mds_providerrecord

- **表名称：** 供方记录表-主表
- **表名：** t_mds_providerrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsetoffqty | 冲减数量 | numeric | 23 | 10 | √ | 0.0000000000 | 冲减数量 |
| 3 | ftransferid | 实体字段映射ID | int8 | 64 |  | √ | 0 | 实体字段映射ID |
| 4 | fsetid | 预测冲减定义 | int8 | 64 |  | √ | 0 | [预测冲减定义 mds_setoffsetting](../mds_files/mds_setoffsetting.md) |
| 5 | fmatverid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :正常 B :已关闭 |
| 8 | flogid | 冲减日志ID | int8 | 64 |  | √ | 0 | 冲减日志ID |
| 9 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | frecorddate | 记录日期 | timestamp | 0 |  |  | null | 记录日期 |
| 12 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | fenddate | 预测结束日期 | timestamp | 0 |  |  | null | 预测结束日期 |
| 14 | fbno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fsourcetype | 来源 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 17 | ftrackid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 18 | fprovidergroupno | 组号 | int4 | 32 |  | √ | 0 | 组号 |
| 19 | fdefineconfig | 自定义配置字符 | varchar | 50 |  | √ | ' ' | 自定义配置字符 |
| 20 | fforecastbillno | 预测单编号 | varchar | 60 |  | √ | ' ' | 预测单编号 |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fmateriel | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 23 | fqty | 单据数量 | numeric | 23 | 10 | √ | 0.0000000000 | 单据数量 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fbilltag | 单据标识 | varchar | 50 |  | √ | ' ' | 单据标识 |
| 26 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 27 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 28 | fforecastfcvrnnum | 版本编码 | int8 | 64 |  | √ | 0 | [版本定义 mds_vrds](../mds_files/mds_vrds.md) |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | ftoolid | 预测冲减运算 | int8 | 64 |  | √ | 0 | [预测冲减运算 mds_setofftool](../mds_files/mds_setofftool.md) |
| 31 | fbillunit | 单据计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 32 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 33 | fbilltypename | 单据类型名称 | varchar | 50 |  | √ | ' ' | 单据类型名称 |
| 34 | ffcvrnnum | 预测版本ID | int8 | 64 |  | √ | 0 | 预测版本ID |
| 35 | fclosestatus | 关闭状态 | varchar | 30 |  | √ | ' ' | 关闭状态,枚举: 0 :正常 1 :关闭 |
| 36 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 37 | fbom | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 38 | fstartdate | 预测开始日期 | timestamp | 0 |  |  | null | 预测开始日期 |
| 39 | fbillrowno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 40 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 41 | fbillorg | 单据组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 44 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 45 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_providerrecord_setmid |  | fsetid,fmateriel |
| 2 | idx_mds_providerrecord_mat |  | fmateriel |
| 3 | pk_mds_providerrecord |  | fid |
