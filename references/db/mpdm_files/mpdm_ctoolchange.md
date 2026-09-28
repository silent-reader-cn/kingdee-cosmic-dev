# 工卡工具变更单-mpdm_ctoolchange

## 关联子实体-子表 t_mpdm_ctoolentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpdm_ctoolentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_ctoolentry_lk_fk |  | fentryid |
| 2 | pk_mpdm_ctoolentry_lk |  | fpkid |

---

## 检修设备类型-多选基础资料表 t_mpdm_rtoolmrtypec

- **表名称：** 检修设备类型-多选基础资料表
- **表名：** t_mpdm_rtoolmrtypec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_rtoolmrtypec |  | fpkid |
| 2 | idx_mpdm_rtoolmrtypec_fk |  | fentryid |

---

## 关联子实体-子表 t_mpdm_ctoolchange_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpdm_ctoolchange_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_ctoolchange_lk_fk |  | fid |
| 2 | pk_mpdm_ctoolchange_lk |  | fpkid |

---

## 附件-附件表 t_mpdm_docappendixc

- **表名称：** 附件-附件表
- **表名：** t_mpdm_docappendixc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_docappendixc_fk |  | fentryid |
| 2 | pk_mpdm_docappendixc |  | fpkid |

---

## 工卡工具变更单-反写记录表 t_mpdm_ctoolchange_wb

- **表名称：** 工卡工具变更单-反写记录表
- **表名：** t_mpdm_ctoolchange_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_ctoolchange_wb |  | fentryid |
| 2 | idx_mpdm_ctoolchange_wb_fk |  | fid |

---

## 工卡工具变更单-关联追踪表 t_mpdm_ctoolchange_tc

- **表名称：** 工卡工具变更单-关联追踪表
- **表名：** t_mpdm_ctoolchange_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_ctoolchange_tc |  | fid |
| 2 | idx_mpdm_ctoolchange_tc_tbill |  | ftbillid |
| 3 | idx_mpdm_ctoolchange_tc_tid |  | ftid |

---

## 关联子实体-子表 t_mpdm_cardtooldocc_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpdm_cardtooldocc_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_cardtooldocc_lk_fk |  | fentryid |
| 2 | pk_mpdm_cardtooldocc_lk |  | fpkid |

---

## 工具清单-子表 t_mpdm_ctoolentry

- **表名称：** 工具清单-子表
- **表名：** t_mpdm_ctoolentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplyorg | 供货库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | foldentryid | 工具分录id | int8 | 64 |  | √ | 0 | 工具分录id |
| 4 | fgroupversion | 替代组版本 | varchar | 80 |  | √ | ' ' | 替代组版本 |
| 5 | fentryownertype | 供应方式 | varchar | 50 |  | √ | ' ' | 供应方式,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 6 | fentrybaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | frowtype | 行类型 | varchar | 50 |  | √ | ' ' | 行类型,枚举: A :修改 B :新增 |
| 8 | flocation | 默认仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fentryhistoryusetime | 历史使用时长（小时） | numeric | 23 | 10 | √ | 0 | 历史使用时长（小时） |
| 11 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | ftoolsubgroup | 替代组 | int8 | 64 |  | √ | 0 | [工具替代组 mpdm_toolsubgroup](../mpdm_files/mpdm_toolsubgroup.md) |
| 13 | ftoollevel | 工具使用级别 | varchar | 50 |  | √ | ' ' | 工具使用级别,枚举: A :必选 B :可选 |
| 14 | fwarehouse | 默认仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 15 | fenrtyunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 17 | fentrybaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 18 | fentryqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 19 | fentrymaterial | 工具件号 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 20 | frepgrpentryid | 替代组entryid | int8 | 64 |  | √ | 0 | 替代组entryid |
| 21 | fentryowner | 供应方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_ctoolentry |  | fentryid |
| 2 | idx_mpdm_ctoolentry_fk |  | fid |

---

## 工卡工具变更单-主表 t_mpdm_ctoolchange

- **表名称：** 工卡工具变更单-主表
- **表名：** t_mpdm_ctoolchange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 变更组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftoolid | 工卡工具需求id | int8 | 64 |  | √ | 0 | 工卡工具需求id |
| 7 | fmaterialnum | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmaterialtype | 检修设备类型 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fhourunit | 时长单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fmaterialunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fchangetime | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 15 | fworkcard | 工卡编码 | int8 | 64 |  | √ | 0 | [工卡 mpdm_mrocardroute](../mpdm_files/mpdm_mrocardroute.md) |
| 16 | fisneedtool | 需要工具 | bpchar | 1 |  | √ | '1' | 需要工具 |
| 17 | fchangereasion | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_ctoolchange_ftoolid |  | ftoolid |
| 2 | pk_mpdm_ctoolchange |  | fid |

---

## 手册-子表 t_mpdm_cardtooldocc

- **表名称：** 手册-子表
- **表名：** t_mpdm_cardtooldocc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdocdescribe | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fdocpagenumber | 手册章节号 | varchar | 50 |  | √ | ' ' | 手册章节号 |
| 4 | fdocmanualversion | 手册版本 | varchar | 50 |  | √ | ' ' | 手册版本 |
| 5 | fdocmanualnumber | 手册编码 | varchar | 80 |  | √ | ' ' | 手册编码 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdocentryid | 手册分录id | int8 | 64 |  | √ | 0 | 手册分录id |
| 8 | fdocname | 手册名称 | varchar | 80 |  | √ | ' ' | 手册名称 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_cardtooldocc_fk |  | fid |
| 2 | pk_mpdm_cardtooldocc |  | fentryid |
