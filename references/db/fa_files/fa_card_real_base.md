# 资产卡片基础资料-fa_card_real_base

## 资产卡片基础资料-多语言表 t_fa_card_real_l

- **表名称：** 资产卡片基础资料-多语言表
- **表名：** t_fa_card_real_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassetname | 资产名称 | varchar | 100 |  | √ | ' ' | 资产名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_card_real_l_pkey |  | fpkid |
| 2 | idx_fa_card_real_l |  | fid,flocaleid |

---

## 资产条码-多选基础资料表 t_fa_card_barcode

- **表名称：** 资产条码-多选基础资料表
- **表名：** t_fa_card_barcode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 条码主档 barcm_barcodemainfile |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_card_barcode |  | fpkid |
| 2 | idx_fa_card_bc_fdetail |  | fid |

---

## 资产卡片基础资料-主表 t_fa_card_real

- **表名称：** 资产卡片基础资料-主表
- **表名：** t_fa_card_real

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsourceentrysplitseq | fsourceentrysplitseq | int8 | 64 |  | √ | 0 |  |
| 3 | fpicturepath | 图片 | varchar | 255 |  |  | ' ' | 图片 |
| 4 | fsourceflag | 来源标识 | varchar | 50 |  | √ | 'ADD' | 来源标识,枚举: ADD :新增 PURCHASE :采购转固 INITIAL :初始化 IMPORT :导入 DISPATCH :调拨 SPLIT :拆分 COMBIN :组合 INVENTORYPROFIT :盘盈 ENGINEERINGTRANS :工程转固 LEASECONTRACT :租赁合同 INVENTORY :盘点 INITLEASECONTRACT :初始化租赁合同 DATAASSET :数据资产 |
| 5 | fsrcbillentityname | 源单据标识 | varchar | 30 |  | √ | ' ' | 源单据标识 |
| 6 | fbarcoderecovery | fbarcoderecovery | bpchar | 1 |  | √ | ' ' |  |
| 7 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fsourceentryid | 来源分录 | int8 | 64 |  | √ | 0 | 来源分录 |
| 9 | fheadusepersonid | 使用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fhasvoucher | fhasvoucher | bpchar | 1 |  | √ | '0' |  |
| 11 | fusestatusid | 使用状态 | int8 | 64 |  | √ | 0 | 使用状态 fa_usestatus |
| 12 | fjustrealcard | 费用化资产 | bpchar | 1 |  | √ | '0' | 费用化资产 |
| 13 | fiscancel | fiscancel | bpchar | 1 |  | √ | '0' |  |
| 14 | fisstoraged | 是否库存 | bpchar | 1 |  | √ | '1' | 是否库存 |
| 15 | fbarcode | 条形码 | varchar | 30 |  | √ | ' ' | 条形码 |
| 16 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 17 | fstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | 存放地点 fa_storeplace |
| 18 | fbillnorecovery | fbillnorecovery | bpchar | 1 |  | √ | ' ' |  |
| 19 | fbillno | 卡片编号 | varchar | 80 |  | √ | ' ' | 卡片编号 |
| 20 | foriginmethodid | 来源方式 | int8 | 64 |  | √ | 0 | 增减方式 fa_changemode |
| 21 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fsrcbillid | 源单据id | int8 | 64 |  | √ | 0 | 源单据id |
| 23 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | 资产类别 fa_assetcategory |
| 24 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fassetqty | 资产数量 | numeric | 23 | 10 | √ | 0 | 资产数量 |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 28 | finitchangeflag | finitchangeflag | int8 | 64 |  | √ | 0 |  |
| 29 | fisinitialcard | 是否初始化卡片 | bpchar | 1 |  | √ | '0' | 是否初始化卡片 |
| 30 | fnumber | 资产编码 | varchar | 80 |  | √ | ' ' | 资产编码 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fmodel | 规格型号 | varchar | 255 |  |  | ' ' | 规格型号 |
| 33 | frealaccountdate | 开始使用日期 | timestamp | 0 |  |  | null | 开始使用日期 |
| 34 | fismultidept | fismultidept | varchar | 1 |  | √ | ' ' |  |
| 35 | fmaterialgroupid | 物料分组 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 36 | fbizstatus | 业务状态 | varchar | 50 |  | √ | 'ADD' | 业务状态,枚举: ADD :新增 READY :就绪 CHG_ORIGINALVAL :原值变更 CHG_USEDEPT :变更使用部门 DEPRE :折旧 CLEAR_ALL :完全清理中 CLEAR_PART :部分清理中 DISPATCH :调拨 SPLIT :拆分 COMBIN :组合 DELETE :作废 CHG_PERIOD :变更使用期间 CHG_ASSETCAT :变更资产类别 TRANSFERING :移交中 DRAWBACKING :退库中 SIGNED :已签收 DEVALUE :减值 DEPREADJUST :折旧调整 COLLECTING :领用中 |
| 37 | foriginaldata | 原始数据 | bpchar | 1 |  | √ | '0' | 原始数据 |
| 38 | fprice | fprice | numeric | 19 | 6 | √ | 0.000000 |  |
| 39 | fassetunitid | 资产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fheadusedeptid | 使用部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fmasterid | 主数据ID | int8 | 64 |  | √ | 0 | 主数据ID |
| 43 | ffinaccountdate | ffinaccountdate | timestamp | 0 |  |  | null |  |
| 44 | fnumberrecovery | fnumberrecovery | bpchar | 1 |  | √ | ' ' |  |
| 45 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 46 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | fassetname | 资产名称 | varchar | 100 |  |  | ' ' | 资产名称 |
| 48 | fusedate | 开始使用日期 | timestamp | 0 |  |  | null | 开始使用日期 |
| 49 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 50 | fisfacility | 附属设备 | bpchar | 1 |  | √ | '0' | 附属设备 |
| 51 | fsourcebillnumber | 源单据编码 | varchar | 30 |  | √ | ' ' | 源单据编码 |
| 52 | fisbak | 备份卡片 | bpchar | 1 |  | √ | '0' | 备份卡片 |
| 53 | fmergedcard | 融合卡片 | bpchar | 1 |  | √ | '0' | 融合卡片 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_card_real_pkey |  | fid |
| 2 | idx_fa_carrea_fnumber |  | fnumber |
| 3 | idx_fa_carrea_billno |  | fbillno |
| 4 | idx_fa_carrea_fmaster |  | fmasterid |
| 5 | idx_fa_carrea_fuseid |  | fheadusepersonid |
| 6 | idx_fa_carrea_faccdate |  | fassetunitid,fisbak,frealaccountdate,fnumber |
| 7 | idx_fa_carrea_fbarcode |  | fbarcode |
| 8 | idx_fa_carrea_ini_sel |  | foriginaldata,fassetunitid,fisinitialcard,fnumber |
| 9 | idx_fa_carrea_org |  | forgid,fisbak,fnumber |
