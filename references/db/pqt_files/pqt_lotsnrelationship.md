# 批号序列号关系-pqt_lotsnrelationship

## 子项页签-子表 t_qpt_lotsnsubentry

- **表名称：** 子项页签-子表
- **表名：** t_qpt_lotsnsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsublot | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 2 | fsubserialid | 序列号主档id | int8 | 64 |  | √ | 0 | [序列号主档 bd_snmainfile](../sbd_files/bd_snmainfile.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsubinvmaterier | 物料编码 | int8 | 64 |  | √ | 9 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 5 | fsubserialno | 序列号 | varchar | 100 |  | √ | ' ' | 序列号 |
| 6 | fsubserunit | 序列号单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fsublotqty | 批号数量 | numeric | 23 | 10 | √ | 0 | 批号数量 |
| 8 | fsublotid | 批号主档id | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 9 | fsubunit | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fsubcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 11 | fsubmaterialid | 子项主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 12 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qpt_lotsnsubentry |  | fdetailid |
| 2 | idx_lotsnsub_entryid |  | fentryid |

---

## 批号序列号关系-主表 t_qpt_lotsnrs

- **表名称：** 批号序列号关系-主表
- **表名：** t_qpt_lotsnrs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fserunit | 序列号单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fworknumber | 工单编号 | varchar | 100 |  | √ | ' ' | 工单编号 |
| 6 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 7 | fsourecerowseq | 源单行号 | int4 | 32 |  | √ | 0 | 源单行号 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fsourcetype | 源单类型 | varchar | 80 |  | √ | ' ' | 源单类型,枚举: handnew :手工录入 im_purinbill :采购入库单 pom_mftorder :生产工单 pom_mftorderreport :生产汇报单 im_mdc_mftmanuinbill :完工入库单 om_mftorder :委外工单 om_outsourcereceipt :委外收货单 im_mdc_omprdinbill :委外完工入库单 |
| 11 | fproductorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 17 | fdepartmentid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 19 | fworkrowseq | 工单行号 | int4 | 32 |  | √ | 0 | 工单行号 |
| 20 | fsourcenumber | 源单编号 | varchar | 100 |  | √ | ' ' | 源单编号 |
| 21 | finvmaterier | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 22 | fsbillid | 源单单据id | varchar | 100 |  | √ | '0' | 源单单据id |
| 23 | fsrowid | 源单分录id | varchar | 100 |  | √ | '0' | 源单分录id |
| 24 | fprocureorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qpt_lotsnrs |  | fid |
| 2 | idx_lotsn_number |  | fbillno |

---

## 成品页签-子表 t_qpt_lotsnentry

- **表名称：** 成品页签-子表
- **表名：** t_qpt_lotsnentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flotqty | 批号数量 | numeric | 23 | 10 | √ | 0 | 批号数量 |
| 3 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 4 | flotid | 批号主档id | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 5 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fserialno | 序列号 | varchar | 100 |  | √ | ' ' | 序列号 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | flot | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 9 | fserialid | 序列号主档id | int8 | 64 |  | √ | 0 | [序列号主档 bd_snmainfile](../sbd_files/bd_snmainfile.md) |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | funit | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qpt_lotsnentry |  | fentryid |
| 2 | idx_lotsnentry_fid |  | fid |

---

## 批号序列号关系-关联追踪表 t_qpt_lotsnrs_tc

- **表名称：** 批号序列号关系-关联追踪表
- **表名：** t_qpt_lotsnrs_tc

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
| 1 | idx_qpt_lotsnrs_tc_tbill |  | ftbillid |
| 2 | idx_qpt_lotsnrs_tc_tid |  | ftid |
| 3 | pk_qpt_lotsnrs_tc |  | fid |

---

## 关联子实体-子表 t_qpt_lotsnentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qpt_lotsnentry_lk

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
| 1 | pk_qpt_lotsnentry_lk |  | fpkid |
| 2 | idx_qpt_lotsnentry_lk_fk |  | fentryid |

---

## 批号序列号关系-反写记录表 t_qpt_lotsnrs_wb

- **表名称：** 批号序列号关系-反写记录表
- **表名：** t_qpt_lotsnrs_wb

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
| 1 | pk_qpt_lotsnrs_wb |  | fentryid |
| 2 | idx_qpt_lotsnrs_wb_fk |  | fid |
