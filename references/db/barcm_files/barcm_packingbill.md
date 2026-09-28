# 装箱单-barcm_packingbill

## 包装明细-子表 t_barcm_packingbillety

- **表名称：** 包装明细-子表
- **表名：** t_barcm_packingbillety

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprddate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 3 | fauxsplitedqty2 | 已拆出辅助数量(2) | numeric | 23 | 10 | √ | 0 | 已拆出辅助数量(2) |
| 4 | fsnnumbertext | 序列号文本 | varchar | 255 |  | √ | ' ' | 序列号文本 |
| 5 | fdtlpackingbillid | 明细装箱单ID | int8 | 64 |  | √ | 0 | 明细装箱单ID |
| 6 | fsrcbillno | 包装来源单据编号 | varchar | 80 |  | √ | ' ' | 包装来源单据编号 |
| 7 | fbarcodeobjectid | 条码对象 | int8 | 64 |  |  | 0 | 条码对象 barcm_barcodeobject |
| 8 | fbarcoderuleid | 条码规则 | int8 | 64 |  |  | 0 | [条码规则 barcm_barcoderule](../barcm_files/barcm_barcoderule.md) |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fruletype | 规则类型 | bpchar | 1 |  | √ | ' ' | 规则类型,枚举: A :主档对照 B :定长解析 C :分段解析 |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | fpackageqty | 包装数量 | numeric | 23 | 10 | √ | 0 | 包装数量 |
| 13 | flotcode | 批号文本 | varchar | 80 |  | √ | ' ' | 批号文本 |
| 14 | fbarcode | 明细条码 | varchar | 255 |  | √ | ' ' | 明细条码 |
| 15 | fauxsplitedqty | 已拆出辅助数量 | numeric | 23 | 10 | √ | 0 | 已拆出辅助数量 |
| 16 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fpackingtime | 包装时间 | timestamp | 0 |  |  | null | 包装时间 |
| 18 | fbaseremainqty | 剩余包装基本数量 | numeric | 23 | 10 | √ | 0 | 剩余包装基本数量 |
| 19 | fsncomment | 序列号备注（作废） | varchar | 255 |  | √ | ' ' | 序列号备注（作废） |
| 20 | fbasesplitedqty | 已拆出基本数量 | numeric | 23 | 10 | √ | 0 | 已拆出基本数量 |
| 21 | fenablesnmanage | 启用序列号管理 | bpchar | 1 |  | √ | '0' | 启用序列号管理 |
| 22 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fbomversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 24 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 25 | fauxremainqty | 剩余包装辅助数量 | numeric | 23 | 10 | √ | 0 | 剩余包装辅助数量 |
| 26 | fsrcbillid | 包装来源单据ID | int8 | 64 |  | √ | 0 | 包装来源单据ID |
| 27 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fbasepackageqty | 包装基本数量 | numeric | 23 | 10 | √ | 0 | 包装基本数量 |
| 29 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 30 | fsplitedqty | 已拆出数量 | numeric | 23 | 10 | √ | 0 | 已拆出数量 |
| 31 | fauxpackageqty | 辅助包装数量 | numeric | 23 | 10 | √ | 0 | 辅助包装数量 |
| 32 | fmaterialetyid | 物料编码 | int8 | 64 |  |  | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 33 | fdtlpackingbillno | 明细装箱单编号 | varchar | 80 |  | √ | ' ' | 明细装箱单编号 |
| 34 | fpackinguserid | 包装用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fauxremainqty2 | 剩余包装辅助数量(2) | numeric | 23 | 10 | √ | 0 | 剩余包装辅助数量(2) |
| 36 | fsrcbillentryid | 包装来源单据行ID | int8 | 64 |  | √ | 0 | 包装来源单据行ID |
| 37 | fbarcodemainfileetyid | 条码主档 | int8 | 64 |  |  | 0 | [条码主档 barcm_barcodemainfile](../barcm_files/barcm_barcodemainfile.md) |
| 38 | flotid | 批号 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 39 | fauxpackageqty2 | 辅助包装数量(2) | numeric | 23 | 10 | √ | 0 | 辅助包装数量(2) |
| 40 | fsnnumberid | 序列号（作废） | int8 | 64 |  | √ | 0 | [序列号主档 bd_snmainfile](../sbd_files/bd_snmainfile.md) |
| 41 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 43 | fremainqty | 剩余包装数量 | numeric | 23 | 10 | √ | 0 | 剩余包装数量 |
| 44 | fgroupnum | 组号（作废） | varchar | 255 |  | √ | ' ' | 组号（作废） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_pbentry_fid |  | fid |
| 2 | pk_barcm_packingbety |  | fentryid |

---

## 装箱单-多语言表 t_barcm_packingbill_l

- **表名称：** 装箱单-多语言表
- **表名：** t_barcm_packingbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 3 | fdescription | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_packingbill_l |  | fpkid |
| 2 | idx_barcm_packingb_l_fidfld |  | fid,flocaleid |

---

## 装箱单-主表 t_barcm_packingbill

- **表名称：** 装箱单-主表
- **表名：** t_barcm_packingbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpackagelevel | 包装层级 | int4 | 32 |  | √ | 1 | 包装层级 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmaterialid | 内装物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 7 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fpackagedcount | 已装条码个数 | int4 | 32 |  | √ | 0 | 已装条码个数 |
| 9 | fmainbizentitymark | 主业务实体标识 | varchar | 255 |  | √ | ' ' | 主业务实体标识 |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fdescription | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 12 | fismixpackage | 混装 | bpchar | 1 |  | √ | ' ' | 混装 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fbarcodemainfileid | 容器条码 | int8 | 64 |  | √ | 0 | [条码主档 barcm_barcodemainfile](../barcm_files/barcm_barcodemainfile.md) |
| 15 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fbizobjwhitelistid | 包装来源单据 | int8 | 64 |  | √ | 0 | [条码业务对象白名单 barcm_bizobjwhitelist](../barcm_files/barcm_bizobjwhitelist.md) |
| 17 | fbizobjectid | 单据名称 | varchar | 255 |  |  | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcontainerbcodesrctype | 容器条码来源 | bpchar | 1 |  | √ | ' ' | 容器条码来源,枚举: A :预先生成 B :封箱后生成 |
| 20 | fcontainercapacity | 容器容量 | int4 | 32 |  | √ | 0 | 容器容量 |
| 21 | fownertype | 货主类型 | varchar | 40 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 22 | fpackagetimingid | 包装时机 | int8 | 64 |  | √ | 0 | [包装时机 barcm_packagetiming](../barcm_files/barcm_packagetiming.md) |
| 23 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_packingbill_no |  | fbillno |
| 2 | pk_t_barcm_packingbill |  | fid |

---

## 包装明细-多语言表 t_barcm_packingbillety_l

- **表名称：** 包装明细-多语言表
- **表名：** t_barcm_packingbillety_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_packingbety_l |  | fpkid |
| 2 | idx_barcm_packinbety_l_locale |  | fentryid,flocaleid |

---

## 包装来源单据信息-子表 t_barcm_packsourbillinfo

- **表名称：** 包装来源单据信息-子表
- **表名：** t_barcm_packsourbillinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpacksourcebillid | 包装来源单据ID | int8 | 64 |  | √ | 0 | 包装来源单据ID |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fpacksourcebillno | 包装来源单据编号 | varchar | 255 |  | √ | ' ' | 包装来源单据编号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_packsourbillinfo_fentryid |  | fentryid |
| 2 | idx_barcm_packsourbillinfo_fentryid |  | fentryid |
