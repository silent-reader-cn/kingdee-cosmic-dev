# 期初委外在制材料-om_init_inprocess

## 关联子实体-子表 t_om_inpstockentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_om_inpstockentry_lk

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
| 1 | pk_om_inpstockentry_lk |  | fpkid |
| 2 | idx_om_inpstockentry_lk_fk |  | fentryid |

---

## 期初生产用料清单-子表 t_om_inpstockentry

- **表名称：** 期初生产用料清单-子表
- **表名：** t_om_inpstockentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fstockid | 委外用料清单 | int8 | 64 |  | √ | 0 | 委外组件清单f7 om_mftstock_headf7 |
| 5 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 6 | fstockentryid | 委外用料清单分录 | int8 | 64 |  | √ | 0 | 委外用料清单分录f7 om_mftstockf7 |
| 7 | finpbuswipbaseqty | 本次分摊基本数量 | numeric | 23 | 10 | √ | 0 | 本次分摊基本数量 |
| 8 | finpentryentityid | 期初委外在制材料分录ID | int8 | 64 |  | √ | 0 | 期初委外在制材料分录ID |
| 9 | finpsubunitid | 期初委外在制材料.子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | flocationid | 发料仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 11 | fbaseunitid | 期初在制材料.基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | finpbuswipqty | 本次分摊数量 | numeric | 23 | 10 | √ | 0 | 本次分摊数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_inpstockentry |  | fid |
| 2 | pk_om_inpstockentry |  | fentryid |

---

## 期初委外在制材料-主表 t_om_inprocess

- **表名称：** 期初委外在制材料-主表
- **表名：** t_om_inprocess

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fproducedeptid | fproducedeptid | int8 | 64 |  | √ | 0 |  |
| 7 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fisnewbill | 是否新单 | bpchar | 1 |  | √ | '0' | 是否新单 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fprddeptid | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_inprocess_billno |  | fbillno |
| 2 | pk_om_inprocess |  | fid |

---

## 期初委外在制材料-关联追踪表 t_om_inprocess_tc

- **表名称：** 期初委外在制材料-关联追踪表
- **表名：** t_om_inprocess_tc

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
| 1 | pk_om_inprocess_tc |  | fid |
| 2 | idx_om_inprocess_tc_tid |  | ftid |
| 3 | idx_om_inprocess_tc_tbill |  | ftbillid |

---

## 期初在制材料-子表 t_om_inprocessentry

- **表名称：** 期初在制材料-子表
- **表名：** t_om_inprocessentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 3 | fproducedeptid | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fisshare | 已分摊 | bpchar | 1 |  | √ | '0' | 已分摊 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsubunitid | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 9 | fsupplierid | 委外加工商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 10 | finvunitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 12 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 13 | finpinvorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | finvunitqty | 库存单位.在制数量 | numeric | 23 | 10 | √ | 0 | 库存单位.在制数量 |
| 15 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 16 | fsubunitqty | 子项单位.在制数量 | numeric | 23 | 10 | √ | 0 | 子项单位.在制数量 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fisrealation | 已关联用料清单 | bpchar | 1 |  | √ | '0' | 已关联用料清单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_inprocessentry |  | fentryid |
| 2 | idx_om_inprocessentry |  | fid |

---

## 关联子实体-子表 t_om_inprocess_lk

- **表名称：** 关联子实体-子表
- **表名：** t_om_inprocess_lk

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
| 1 | pk_om_inprocess_lk |  | fpkid |
| 2 | idx_om_inprocess_lk_fk |  | fid |

---

## 期初委外在制材料-反写记录表 t_om_inprocess_wb

- **表名称：** 期初委外在制材料-反写记录表
- **表名：** t_om_inprocess_wb

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
| 1 | pk_om_inprocess_wb |  | fentryid |
| 2 | idx_om_inprocess_wb_fk |  | fid |

---

## 期初委外在制材料-多语言表 t_om_inprocess_l

- **表名称：** 期初委外在制材料-多语言表
- **表名：** t_om_inprocess_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_inprocess_l |  | fid,flocaleid |
| 2 | pk_om_inprocess_l |  | fpkid |
