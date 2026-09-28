# 期初在制材料-pom_init_inprocess

## 期初生产用料清单-多语言表 t_pom_iinpstockentry_l

- **表名称：** 期初生产用料清单-多语言表
- **表名：** t_pom_iinpstockentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fentryremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_iinpstockentry_l |  | fentryid,flocaleid |
| 2 | pk_pom_iinpstockentry_l |  | fpkid |

---

## 期初在制材料-子表 t_pom_inprocessentry

- **表名称：** 期初在制材料-子表
- **表名：** t_pom_inprocessentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 4 | fproducedeptid | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fisshare | 已分摊 | bpchar | 1 |  | √ | '0' | 已分摊 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fsubunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 10 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 11 | finvunitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 13 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 14 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 15 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 16 | finpinvorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | finvunitqty | 库存单位.在制数量 | numeric | 23 | 10 | √ | 0 | 库存单位.在制数量 |
| 18 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 19 | fsubunitqty | 子项单位.在制数量 | numeric | 23 | 10 | √ | 0 | 子项单位.在制数量 |
| 20 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fisrealation | 已关联用料清单 | bpchar | 1 |  | √ | '0' | 已关联用料清单 |
| 23 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_inprocessentry |  | fid |
| 2 | pk_pom_inprocessentry |  | fentryid |

---

## 关联子实体-子表 t_pom_inpstockentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_inpstockentry_lk

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
| 1 | pk_pom_inpstockentry_lk |  | fpkid |
| 2 | idx_pom_inpstockentry_lk_fk |  | fentryid |

---

## 期初在制材料-反写记录表 t_pom_inprocess_wb

- **表名称：** 期初在制材料-反写记录表
- **表名：** t_pom_inprocess_wb

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
| 1 | idx_pom_inprocess_wb_fk |  | fid |
| 2 | pk_pom_inprocess_wb |  | fentryid |

---

## 期初在制材料-主表 t_pom_inprocess

- **表名称：** 期初在制材料-主表
- **表名：** t_pom_inprocess

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fproducedeptid | fproducedeptid | int8 | 64 |  | √ | 0 |  |
| 7 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fisnewbill | 是否新单 | bpchar | 1 |  | √ | '0' | 是否新单 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fscheme | 盘点方案 | varchar | 5 |  | √ | 'A' | 盘点方案,枚举: A :根据在制数量分摊 B :直接录入在制清单 |
| 13 | fgenerte | 已生成领料单 | bpchar | 1 |  | √ | '0' | 已生成领料单 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_inprocess |  | fid |
| 2 | idx_pom_inprocess_billno |  | fbillno |

---

## 关联子实体-子表 t_pom_inprocess_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_inprocess_lk

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
| 1 | idx_pom_inprocess_lk_fk |  | fid |
| 2 | pk_pom_inprocess_lk |  | fpkid |

---

## 期初在制材料-关联追踪表 t_pom_inprocess_tc

- **表名称：** 期初在制材料-关联追踪表
- **表名：** t_pom_inprocess_tc

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
| 1 | pk_pom_inprocess_tc |  | fid |
| 2 | idx_pom_inprocess_tc_tbill |  | ftbillid |
| 3 | idx_pom_inprocess_tc_tid |  | ftid |

---

## 期初生产用料清单-子表 t_pom_iinpstockentry

- **表名称：** 期初生产用料清单-子表
- **表名：** t_pom_iinpstockentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 4 | fissuemode | 领送料方式 | varchar | 5 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 C :不领料 |
| 5 | fiscannegative | 退料 | bpchar | 1 |  | √ | '0' | 退料 |
| 6 | flocation | 发料仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | foutlocation | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 9 | fsubunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fnumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 11 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0 | 变动损耗率% |
| 12 | fiwipbaseqty | 在制基本数量 | numeric | 23 | 10 | √ | 0 | 在制基本数量 |
| 13 | fentrylicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 14 | fdenominator | 分母 | numeric | 23 | 10 | √ | 1 | 分母 |
| 15 | fbaseqtydenominator | 基本单位分母 | numeric | 23 | 10 | √ | 1 | 基本单位分母 |
| 16 | fisreturninspect | 生产退料检验 | bpchar | 1 |  | √ | '0' | 生产退料检验 |
| 17 | fisstockallot | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 18 | foutorgunitid | 调出库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | foverissuecontrl | 超发控制 | varchar | 5 |  | √ | ' ' | 超发控制,枚举: A :可超发 B :不可超发 C :最小包装量 |
| 20 | fbaseunitid | 生产基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fentrybonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 22 | flot | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 23 | fissinhighlimit | 领料上限允差(%) | numeric | 23 | 10 | √ | 0 | 领料上限允差(%) |
| 24 | frework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 25 | fupdatetype | 更新方式 | varchar | 5 |  | √ | 'A' | 更新方式,枚举: A :修改 B :新增 |
| 26 | fqtytype | 用量类型 | varchar | 5 |  | √ | 'A' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 27 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 28 | fstockentry | 生产用料清单分录 | int8 | 64 |  | √ | 0 | [生产用料清单分录f7 pom_mftstockentryf7](../pom_files/pom_mftstockentryf7.md) |
| 29 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 30 | fstock | 生产用料清单引入 | int8 | 64 |  | √ | 0 | [生产用料清单f7_编码引入 pom_mftstockf7_import](../pom_files/pom_mftstockf7_import.md) |
| 31 | fbaseqtynumerator | 基本单位分子 | numeric | 23 | 10 | √ | 0 | 基本单位分子 |
| 32 | fisbackflush | 倒冲 | varchar | 5 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 33 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 34 | fentryremarks | fentryremarks | varchar | 255 |  | √ | ' ' |  |
| 35 | fentrybomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 36 | fsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | fsubbaseunitid | 子项基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 38 | fiskeypart | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 39 | fsupplymode | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 40 | fentrytracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 41 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 42 | fwipqty | 在制数量 | numeric | 23 | 10 | √ | 0 | 在制数量 |
| 43 | fentrymaterilversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 44 | fprovideorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | fsupplyorgid | 发料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 47 | fstockproductid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_iinpstockentry |  | fentryid |
| 2 | idx_pom_iinpstockentry_fstock |  | fstock |
| 3 | idx_pom_iinpstockentry_fid |  | fid |

---

## 期初生产用料清单-子表 t_pom_inpstockentry

- **表名称：** 期初生产用料清单-子表
- **表名：** t_pom_inpstockentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fstockid | 生产用料清单 | int8 | 64 |  | √ | 0 | [生产用料清单f7 pom_mftstockf7](../pom_files/pom_mftstockf7.md) |
| 5 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 6 | fstockentryid | 生产用料清单分录 | int8 | 64 |  | √ | 0 | [生产用料清单分录f7 pom_mftstockentryf7](../pom_files/pom_mftstockentryf7.md) |
| 7 | finpbuswipbaseqty | 本次分摊基本数量 | numeric | 23 | 10 | √ | 0 | 本次分摊基本数量 |
| 8 | finpentryentityid | 期初在制材料分录ID | int8 | 64 |  | √ | 0 | 期初在制材料分录ID |
| 9 | finpsubunitid | 期初在制材料.子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | flocationid | 发料仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 11 | fbaseunitid | 期初在制材料.基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fsupplyorgid | 发料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | finpbuswipqty | 本次分摊数量 | numeric | 23 | 10 | √ | 0 | 本次分摊数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_inpstockentry |  | fid |
| 2 | pk_pom_inpstockentry |  | fentryid |

---

## 关联子实体-子表 t_pom_iinpstockentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_iinpstockentry_lk

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
| 1 | pk_pom_iinpstockentry_lk |  | fpkid |
| 2 | idx_pom_iinpstockentry_lk_fk |  | fentryid |

---

## 期初在制材料-多语言表 t_pom_inprocess_l

- **表名称：** 期初在制材料-多语言表
- **表名：** t_pom_inprocess_l

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
| 1 | pk_pom_inprocess_l |  | fpkid |
| 2 | idx_pom_inprocess_l |  | fid,flocaleid |
