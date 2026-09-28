# 条码生成记录-barcm_bcgenerecord

## 条码生成信息-子表 t_barcm_bcgeneinfo

- **表名称：** 条码生成信息-子表
- **表名：** t_barcm_bcgeneinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 3 | fsrcentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 4 | fpackagesizeid | 包装规格 | int8 | 64 |  | √ | 0 | 包装规格 barcm_packagesize |
| 5 | flotnumber | 批号 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 6 | fmaterialid | 物料编号 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fbarcoderuleid | 条码规则 | int8 | 64 |  | √ | 0 | 条码规则 barcm_barcoderule |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fqtysrcsign | 数量来源字段标识 | varchar | 50 |  | √ | ' ' | 数量来源字段标识 |
| 11 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 12 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 13 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fprinttemplateid | 条码打印模板 | int8 | 64 |  | √ | 0 | 维护打印模板（新） bos_manageprinttpl |
| 15 | fbillrownum | 单据行号 | varchar | 80 |  | √ | ' ' | 单据行号 |
| 16 | fbillnum | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | flotnumbertext | 批号文本 | varchar | 50 |  | √ | ' ' | 批号文本 |
| 18 | fbcqtygenerated | 已生成条码数量 | numeric | 23 | 10 | √ | 0 | 已生成条码数量 |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 21 | fname | 基础资料名称 | varchar | 255 |  | √ | ' ' | 基础资料名称 |
| 22 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 23 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fsrcsubentryid | 来源单据子分录ID | int8 | 64 |  | √ | 0 | 来源单据子分录ID |
| 25 | fsrcunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 26 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 27 | fmainorgid | 主业务组织 | int8 | 64 |  | √ | 0 | 主业务组织 |
| 28 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 29 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 30 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 31 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 32 | fbcqtysingle | 单个条码数量 | numeric | 23 | 10 | √ | 0 | 单个条码数量 |
| 33 | ftotalgenqty | 本次生成条码总数量 | numeric | 23 | 10 | √ | 0 | 本次生成条码总数量 |
| 34 | fbccount | 条码个数 | int4 | 32 |  | √ | 0 | 条码个数 |
| 35 | fnumber | 基础资料编号 | varchar | 80 |  | √ | ' ' | 基础资料编号 |
| 36 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | ftotalsourceqty | 源单总数量 | numeric | 23 | 10 | √ | 0 | 源单总数量 |
| 39 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_bcgeneinfo |  | fentryid |
| 2 | idx_barcm_bcgni_materialid |  | fmaterialid |

---

## 包装容器信息-子表 t_barcm_pcinfo

- **表名称：** 包装容器信息-子表
- **表名：** t_barcm_pcinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcontainerprinttplid | 条码打印模板 | int8 | 64 |  | √ | 0 | 维护打印模板（新） bos_manageprinttpl |
| 2 | flevel | 层级 | int4 | 32 |  | √ | 1 | 层级 |
| 3 | fcontainerbccount | 容器条码个数 | int4 | 32 |  | √ | 0 | 容器条码个数 |
| 4 | fpcsizeentryid | 包装规格明细行ID | int8 | 64 |  | √ | 0 | 包装规格明细行ID |
| 5 | fnlevelbccount | 下级条码个数 | int4 | 32 |  | √ | 0 | 下级条码个数 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcontainertypeid | 包装容器类型 | int8 | 64 |  | √ | 0 | 包装容器类型 barcm_containertype_m |
| 8 | fcontainerbcruleid | 条码规则 | int8 | 64 |  | √ | 0 | 条码规则 barcm_barcoderule |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fnextlevelqty | 单层数量 | int4 | 32 |  | √ | 1 | 单层数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_pcinfo_feid |  | fentryid |
| 2 | pk_barcm_pcinfo |  | fdetailid |

---

## 条码生成记录-主表 t_barcm_bcgenerecord

- **表名称：** 条码生成记录-主表
- **表名：** t_barcm_bcgenerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbizobjid | 业务对象 | int8 | 64 |  | √ | 0 | 条码业务对象白名单 barcm_bizobjwhitelist |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_bcgenerecord_fbillno |  | fbillno |
| 2 | pk_barcm_bcgenerecord |  | fid |

---

## 条码清单-子表 t_barcm_bcinventory

- **表名称：** 条码清单-子表
- **表名：** t_barcm_bcinventory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 3 | fsrcentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 4 | fprintstatus | 打印状态 | bpchar | 1 |  | √ | ' ' | 打印状态,枚举: N :空 P :待打印 S :成功 F :失败 |
| 5 | fmaterialid | 物料编号 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fgenmainfiledesc | 生成主档异常描述 | varchar | 2000 |  | √ | ' ' | 生成主档异常描述 |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 10 | fsrcbillrecord | fsrcbillrecord | int8 | 64 |  | √ | 0 |  |
| 11 | fiscanceled | 已作废 | bpchar | 1 |  | √ | ' ' | 已作废 |
| 12 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fprinttemplateid | 条码打印模板 | int8 | 64 |  | √ | 0 | 维护打印模板（新） bos_manageprinttpl |
| 14 | fsncomment | fsncomment | varchar | 255 |  | √ | ' ' |  |
| 15 | fbcstatus | 生成主档状态 | bpchar | 1 |  | √ | ' ' | 生成主档状态,枚举: N :空 P :待生成 S :成功 F :失败 |
| 16 | fprintmode | 打印模式 | bpchar | 1 |  | √ | ' ' | 打印模式,枚举: A :连续打印 B :成套打印 |
| 17 | flotnumbertext | 批号文本 | varchar | 50 |  | √ | ' ' | 批号文本 |
| 18 | fprintdate | 打印时间 | timestamp | 0 |  |  | null | 打印时间 |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fbcauxqtysingle | 单个条码辅助数量 | numeric | 23 | 10 | √ | 0 | 单个条码辅助数量 |
| 23 | fsrcsubentryid | 来源单据子分录ID | int8 | 64 |  | √ | 0 | 来源单据子分录ID |
| 24 | fbcauxqtysingle2 | 单个条码辅助数量(2) | numeric | 23 | 10 | √ | 0 | 单个条码辅助数量(2) |
| 25 | fbarcodemainfileid | 条码主档ID | int8 | 64 |  | √ | 0 | 条码主档 barcm_barcodemainfile |
| 26 | fbcqtysingle | 单个条码数量 | numeric | 23 | 10 | √ | 0 | 单个条码数量 |
| 27 | fprintexcedesc | 打印异常描述 | varchar | 255 |  | √ | ' ' | 打印异常描述 |
| 28 | fsnnumberid | 序列号 | int8 | 64 |  | √ | 0 | 序列号主档 bd_snmainfile |
| 29 | fbarcodevalue | 条码 | varchar | 255 |  | √ | ' ' | 条码 |
| 30 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_bcinventory |  | fentryid |
| 2 | idx_barcm_bcinventory_bcvalue |  | fbarcodevalue |
