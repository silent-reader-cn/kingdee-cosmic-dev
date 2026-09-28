# 条码包装记录-barcm_bcpackagerecord

## 条码包装记录-多语言表 t_barcm_bcpackagerecord_l

- **表名称：** 条码包装记录-多语言表
- **表名：** t_barcm_bcpackagerecord_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 3 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_bcpackagerecord_l |  | fpkid |

---

## 条码包装记录-主表 t_barcm_bcpackagerecord

- **表名称：** 条码包装记录-主表
- **表名：** t_barcm_bcpackagerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flinkpacksrcentryid | 关联明细装箱单行ID | int8 | 64 |  | √ | 0 | 关联明细装箱单行ID |
| 3 | flinkpacksrcid | 关联明细装箱单ID | int8 | 64 |  | √ | 0 | 关联明细装箱单ID |
| 4 | fsnnumbertext | 序列号文本 | varchar | 255 |  | √ | ' ' | 序列号文本 |
| 5 | fbarcodeobjectid | 条码对象 | int8 | 64 |  | √ | 0 | 条码对象 barcm_barcodeobject |
| 6 | flotnumber | 批号 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 7 | fpacksrcbizobjectid | 包装来源单据类型 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 8 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 9 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fbarcoderuleid | 条码规则 | int8 | 64 |  | √ | 0 | 条码规则 barcm_barcoderule |
| 11 | fprepackagebillid | 上级装箱单ID | int8 | 64 |  | √ | 0 | 上级装箱单ID |
| 12 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | fruletype | 规则类型 | bpchar | 1 |  | √ | ' ' | 规则类型,枚举: A :主档对照 B :定长解析 C :分段解析 |
| 14 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 15 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 16 | flinkpacklistnum | 关联明细装箱单单号 | varchar | 80 |  | √ | ' ' | 关联明细装箱单单号 |
| 17 | fpacksrcid | 包装来源单据ID | int8 | 64 |  | √ | 0 | 包装来源单据ID |
| 18 | fmodifytime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 19 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fsncomment | 序列号备注 | varchar | 255 |  | √ | ' ' | 序列号备注 |
| 22 | fownertype | 货主类型 | varchar | 40 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 23 | fauxunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fpacksrcbillnum | 包装来源单据编号 | varchar | 80 |  | √ | ' ' | 包装来源单据编号 |
| 25 | flotnumbertext | 批号文本 | varchar | 50 |  | √ | ' ' | 批号文本 |
| 26 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fbcmainfileid | 条码主档 | int8 | 64 |  | √ | 0 | 条码主档 barcm_barcodemainfile |
| 28 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 29 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 30 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 32 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 33 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 34 | fmainbizentitymark | 主业务实体标识 | varchar | 255 |  | √ | ' ' | 主业务实体标识 |
| 35 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 36 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 37 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 39 | foperaterid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: A :作为上级容器使用 B :作为上级容器撤销使用 C :作为明细条码包装 D :作为明细条码包装拆出 |
| 41 | fsnnumberid | 序列号 | int8 | 64 |  | √ | 0 | 序列号主档 bd_snmainfile |
| 42 | fbarcodevalue | 条码 | varchar | 255 |  | √ | ' ' | 条码 |
| 43 | fprecontainerbcid | 上级容器条码 | int8 | 64 |  | √ | 0 | 条码主档 barcm_barcodemainfile |
| 44 | fpacksrcentryid | 包装来源单据行ID | int8 | 64 |  | √ | 0 | 包装来源单据行ID |
| 45 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 46 | fprepackagebillno | 上级装箱单编号 | varchar | 255 |  | √ | ' ' | 上级装箱单编号 |
| 47 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_bcpackagerecord |  | fid |
| 2 | idx_barcm_bcpackagerecord |  | fbillno |
