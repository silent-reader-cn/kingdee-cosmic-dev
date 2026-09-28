# 用料收货-scp_modulereceipt

## 附件-附件表 t_pur_modulereceiptrejatt

- **表名称：** 附件-附件表
- **表名：** t_pur_modulereceiptrejatt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_modulereceiptrejatt |  | fpkid |
| 2 | idx_pur_morecrejatt_fid |  | fid |
| 3 | idx__pur_morecrejatt_fbaseid |  | fbasedataid |

---

## 关联子实体-子表 t_pur_modulereceiptentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_modulereceiptentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | freceiptqty_old | 确认收货数量_原始携带值 | numeric | 23 | 10 |  | null | 确认收货数量_原始携带值 |
| 2 | freceiptbasicqty_old | 确认收货基本数量_原始携带值 | numeric | 23 | 10 |  | null | 确认收货基本数量_原始携带值 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fdeliverybasicqty_old | 确认发货基本数量_原始携带值 | numeric | 23 | 10 |  | null | 确认发货基本数量_原始携带值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 7 | freceiptqty | 确认收货数量_确认携带值 | numeric | 23 | 10 |  | null | 确认收货数量_确认携带值 |
| 8 | fdeliveryqty_old | 确认发货数量_原始携带值 | numeric | 23 | 10 |  | null | 确认发货数量_原始携带值 |
| 9 | freceiptbasicqty | 确认收货基本数量_确认携带值 | numeric | 23 | 10 |  | null | 确认收货基本数量_确认携带值 |
| 10 | fdeliveryqty | 确认发货数量_确认携带值 | numeric | 23 | 10 |  | null | 确认发货数量_确认携带值 |
| 11 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 12 | fdeliverybasicqty | 确认发货基本数量_确认携带值 | numeric | 23 | 10 |  | null | 确认发货基本数量_确认携带值 |
| 13 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_modulereceiptentry_lk_fk |  | fentryid |
| 2 | pk_pur_modulereceiptentry_lk |  | fpkid |

---

## 用料收货-关联追踪表 t_pur_modulereceipt_tc

- **表名称：** 用料收货-关联追踪表
- **表名：** t_pur_modulereceipt_tc

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
| 1 | pk_pur_modulereceipt_tc |  | fid |
| 2 | idx_pur_modulereceipt_tc_tid |  | ftid |
| 3 | idx_pur_modulereceipt_tc_tbill |  | ftbillid |

---

## 用料收货-反写记录表 t_pur_modulereceipt_wb

- **表名称：** 用料收货-反写记录表
- **表名：** t_pur_modulereceipt_wb

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
| 1 | idx_pur_modulereceipt_wb_fk |  | fid |
| 2 | pk_pur_modulereceipt_wb |  | fentryid |

---

## 用料收货-多语言表 t_pur_modulereceipt_l

- **表名称：** 用料收货-多语言表
- **表名：** t_pur_modulereceipt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_modulereceipt_l |  | fid,flocaleid |
| 2 | pk_t_pur_modulereceipt_l |  | fpkid |

---

## 用料收货-主表 t_pur_modulereceipt

- **表名称：** 用料收货-主表
- **表名：** t_pur_modulereceipt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freceipttype | 收货类型 | bpchar | 1 |  | √ | ' ' | 收货类型,枚举: 0 :收货 3 :退货 1 :退补货 |
| 3 | forgid | 库存方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fbilldate | 收货日期 | timestamp | 0 |  |  | null | 收货日期 |
| 5 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | frejectdate | 打回时间 | timestamp | 0 |  |  | null | 打回时间 |
| 10 | fsourcetype | 来源单据类型 | bpchar | 1 |  | √ | ' ' | 来源单据类型,枚举: 1 :用料发货通知 2 :用料收货 |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | frejectreason | 打回原因 | varchar | 512 |  | √ | '0' | 打回原因 |
| 17 | frejecterid | 打回人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 20 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 22 | fsrctype | 来源类型 | bpchar | 1 |  | √ | ' ' | 来源类型,枚举: 1 :材料直送 2 :直接调拨 3 :分步调拨 |
| 23 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 E :自动确认 |
| 24 | fpersonid | 采购方联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 26 | fcontacterid | 供应商联系人 | int8 | 64 |  | √ | 0 | [协同业务员 scp_bizperson](../scp_files/scp_bizperson.md) |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pur_modulereceipt |  | fid |
| 2 | idx_pur_modulereceipt_fbillno |  | fbillno |
| 3 | idx_pur_modulereceipt_fbizid |  | fbizpartnerid |
| 4 | idx_pur_modulerec_fbilldate |  | fbilldate |

---

## 分录信息-子表 t_pur_modulereceiptentry

- **表名称：** 分录信息-子表
- **表名：** t_pur_modulereceiptentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 3 | fproddate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 4 | fmainbillentity | 核心单据实体 | varchar | 80 |  | √ | ' ' | 核心单据实体 |
| 5 | fdownstreambillid | 下游单据ID | varchar | 50 |  | √ | ' ' | 下游单据ID |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 8 | fsrcbillentryseq | 来源单据行号 | varchar | 20 |  | √ | ' ' | 来源单据行号 |
| 9 | fmainbillid | 核心单据ID | varchar | 50 |  | √ | ' ' | 核心单据ID |
| 10 | ftransdirbillentryid | 调拨单行ID | varchar | 50 |  | √ | ' ' | 调拨单行ID |
| 11 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fpurorgid | 发出组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fdiffbasicqty | 差异基本数量 | numeric | 23 | 10 | √ | 0 | 差异基本数量 |
| 14 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 15 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 16 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 17 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fwarehouseid | 发出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 19 | freceiptqty | 确认收货数量 | numeric | 23 | 10 | √ | 0 | 确认收货数量 |
| 20 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 21 | frelreturnbasiqty | 关联退货基本数量 | numeric | 23 | 10 | √ | 0 | 关联退货基本数量 |
| 22 | flotid | 批号 | int8 | 64 |  | √ | 0 | [批号 pur_lot](../pbd_files/pur_lot.md) |
| 23 | fsaloutnum | 销售发货单编码 | varchar | 80 |  | √ | ' ' | 销售发货单编码 |
| 24 | fdownstreambilltype | 下游单据类型 | varchar | 80 |  | √ | ' ' | 下游单据类型,枚举: im_purinbill :采购入库单 im_transdirbill :直接调拨单 |
| 25 | fsuplot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 26 | fdownstreambillentryid | 下游单据行ID | varchar | 50 |  | √ | ' ' | 下游单据行ID |
| 27 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 28 | frelreturnqty | 关联退货数量 | numeric | 23 | 10 | √ | 0 | 关联退货数量 |
| 29 | fsrcbilltype | 来源单据类型 | varchar | 80 |  | √ | ' ' | 来源单据类型 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 32 | fsrcbillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 33 | fmainbillentryseq | 核心单据分录序号 | varchar | 20 |  | √ | ' ' | 核心单据分录序号 |
| 34 | ftransdirbillid | 调拨单ID | varchar | 50 |  | √ | ' ' | 调拨单ID |
| 35 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 36 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 |
| 37 | fbasicqty | fbasicqty | numeric | 23 | 10 | √ | 0 |  |
| 38 | fdiffqty | 差异数量 | numeric | 23 | 10 | √ | 0 | 差异数量 |
| 39 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 40 | frecwarehouseid | 收货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 41 | fdeliveryqty | 确认发货数量 | numeric | 23 | 10 | √ | 0 | 确认发货数量 |
| 42 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 43 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 44 | freclocationid | 收货仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 45 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 46 | fprocesstype | 处理方式 | bpchar | 1 |  | √ | ' ' | 处理方式,枚举: 1 :退回采购方 2 :退回材料供应商 |
| 47 | fsrcbillentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 48 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 49 | freceiptbasicqty | 确认收货基本数量 | numeric | 23 | 10 | √ | 0 | 确认收货基本数量 |
| 50 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 51 | fdownstreambillno | 下游单据编号 | varchar | 80 |  | √ | ' ' | 下游单据编号 |
| 52 | fmainbillentryid | 核心单据行ID | varchar | 50 |  | √ | ' ' | 核心单据行ID |
| 53 | frecwarehouselocid | 收货仓位 | varchar | 50 |  | √ | '0' | 收货仓位 |
| 54 | fdeliverybasicqty | 确认发货基本数量 | numeric | 23 | 10 | √ | 0 | 确认发货基本数量 |
| 55 | fsaloutid | 销售发货单id | int8 | 64 |  | √ | 0 | 销售发货单id |
| 56 | fsaloutentryid | 销售发货单行id | int8 | 64 |  | √ | 0 | 销售发货单行id |
| 57 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_modulereceiptentry |  | fentryid |
| 2 | idx_pur_modrecentry_fmatid |  | fmaterialid |
| 3 | idx_pur_modrecentry_fid_fseq |  | fid,fseq |
