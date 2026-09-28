# 条码轨迹表-barcm_bcgenesbillrecord

## 条码轨迹表-主表 t_barcm_bcgenesbillrecord

- **表名称：** 条码轨迹表-主表
- **表名：** t_barcm_bcgenesbillrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsnnumbertext | 序列号 | varchar | 255 |  | √ | ' ' | 序列号 |
| 3 | fscanrecordid | 条码扫描记录ID | int8 | 64 |  | √ | 0 | 条码扫描记录ID |
| 4 | fmaterialid | 物料编号 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fqtysrcsign | 数量来源字段标识 | varchar | 50 |  | √ | ' ' | 数量来源字段标识 |
| 6 | fgenqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 7 | fscanrecordnum | 条码扫描记录编号 | varchar | 80 |  | √ | ' ' | 条码扫描记录编号 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fbillrownum | 单据行号 | varchar | 80 |  | √ | ' ' | 单据行号 |
| 13 | fbillnum | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 15 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fbillsubrownum | 单据子行号 | varchar | 80 |  | √ | ' ' | 单据子行号 |
| 18 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fname | 基础资料名称 | varchar | 255 |  | √ | ' ' | 基础资料名称 |
| 21 | fbillsubentryid | 单据子分录ID | int8 | 64 |  | √ | 0 | 单据子分录ID |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fsourcebizobjectid | 业务对象 | int8 | 64 |  | √ | 0 | 条码业务对象白名单 barcm_bizobjwhitelist |
| 24 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 25 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 26 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 29 | fisoutdeductmqty | 出库扣减主档数量 | bpchar | 1 |  | √ | '0' | 出库扣减主档数量 |
| 30 | fbarcodemainfileid | 条码主档ID | int8 | 64 |  | √ | 0 | 条码主档 barcm_barcodemainfile |
| 31 | fbasicdataid | 基础资料ID | int8 | 64 |  | √ | 0 | 基础资料ID |
| 32 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 33 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 34 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: A :生成 B :扫描 C :盘盈 D :盘亏 E :作废 F :反作废 G :更新 |
| 35 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 36 | fsnnumberid | 序列号主档ID | int8 | 64 |  | √ | 0 | 序列号主档 bd_snmainfile |
| 37 | fbarcodevalue | 条码 | varchar | 255 |  | √ | ' ' | 条码 |
| 38 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 39 | fnumber | 基础资料编号 | varchar | 80 |  | √ | ' ' | 基础资料编号 |
| 40 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 41 | fscanmodelid | 条码扫描模型 | int8 | 64 |  | √ | 0 | 条码扫描模型 barcm_scanningmodel |
| 42 | fqtysrc | 数量来源字段 | varchar | 50 |  | √ | ' ' | 数量来源字段 |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_bcgenesbillrecord |  | fid |
| 2 | idx_barcm_bcgnsr_bcvalue |  | fbarcodevalue |

---

## 条码轨迹表-多语言表 t_barcm_bcgenesbillrecord_l

- **表名称：** 条码轨迹表-多语言表
- **表名：** t_barcm_bcgenesbillrecord_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_bcgsr_fidflid |  | fid,flocaleid |
| 2 | pk_barcm_bcgsr_l |  | fpkid |
