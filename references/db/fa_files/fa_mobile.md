# 人人资产首页-fa_mobile

## 人人资产首页-关联追踪表 t_fa_card_real_tc

- **表名称：** 人人资产首页-关联追踪表
- **表名：** t_fa_card_real_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_card_real_tc_tbill |  | ftbillid |
| 2 | t_fa_card_real_tc_pkey |  | fid |
| 3 | idx_fa_card_rtc_sbid |  | fsbillid |
| 4 | idx_fa_card_real_tc_tid |  | ftid |

---

## 关联子实体-子表 t_fa_card_real_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fa_card_real_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fassetqty | 资产数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 资产数量_确认携带值 |
| 7 | fassetqty_old | 资产数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 资产数量_原始携带值 |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_card_real_lk_pkey |  | fpkid |
| 2 | idx_fa_card_rlk_entryid |  | fid |

---

## 人人资产首页-反写记录表 t_fa_card_real_wb

- **表名称：** 人人资产首页-反写记录表
- **表名：** t_fa_card_real_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | bpchar | 1 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_card_rwb_sbid |  | fsbillid |
| 2 | t_fa_card_real_wb_pkey |  | fentryid |

---

## 人人资产首页-主表 t_fa_card_real

- **表名称：** 人人资产首页-主表
- **表名：** t_fa_card_real

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsourceentrysplitseq | 来源分录拆分序号 | int8 | 64 |  | √ | 0 | 来源分录拆分序号 |
| 3 | fpicturepath | 图片 | varchar | 255 |  |  | ' ' | 图片 |
| 4 | fsourceflag | 来源标识 | varchar | 50 |  | √ | 'ADD' | 来源标识,枚举: ADD :新增 PURCHASE :采购转固 INITIAL :初始化 IMPORT :导入 DISPATCH :调拨 SPLIT :拆分 COMBIN :组合 |
| 5 | fsrcbillentityname | fsrcbillentityname | varchar | 30 |  | √ | ' ' |  |
| 6 | fbarcoderecovery | fbarcoderecovery | bpchar | 1 |  | √ | ' ' |  |
| 7 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 8 | fsourceentryid | 来源分录 | int8 | 64 |  | √ | 0 | 来源分录 |
| 9 | fheadusepersonid | 使用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fhasvoucher | fhasvoucher | bpchar | 1 |  | √ | '0' |  |
| 11 | fusestatusid | 使用状态 | int8 | 64 |  | √ | 0 | 使用状态 fa_usestatus |
| 12 | fjustrealcard | fjustrealcard | bpchar | 1 |  | √ | '0' |  |
| 13 | fiscancel | fiscancel | bpchar | 1 |  | √ | '0' |  |
| 14 | fisstoraged | 是否库存 | bpchar | 1 |  | √ | '1' | 是否库存 |
| 15 | fbarcode | 条形码 | varchar | 30 |  | √ | ' ' | 条形码 |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | 存放地点 fa_storeplace |
| 18 | fbillnorecovery | fbillnorecovery | bpchar | 1 |  | √ | ' ' |  |
| 19 | fbillno | 卡片编号 | varchar | 80 |  | √ | ' ' | 卡片编号 |
| 20 | foriginmethodid | 来源方式 | int8 | 64 |  | √ | 0 | 增减方式 fa_changemode |
| 21 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 23 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | 资产类别 fa_assetcategory |
| 24 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fassetqty | 资产数量 | numeric | 23 | 10 | √ | 0 | 资产数量 |
| 26 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 27 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 28 | finitchangeflag | finitchangeflag | int8 | 64 |  | √ | 0 |  |
| 29 | fisinitialcard | 初始化卡片 | bpchar | 1 |  | √ | '0' | 初始化卡片 |
| 30 | fnumber | 资产编码 | varchar | 80 |  | √ | ' ' | 资产编码 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fmodel | 规格型号 | varchar | 255 |  |  | ' ' | 规格型号 |
| 33 | frealaccountdate | 实物入账日期 | timestamp | 0 |  |  | null | 实物入账日期 |
| 34 | fismultidept | fismultidept | varchar | 1 |  | √ | ' ' |  |
| 35 | fmaterialgroupid | fmaterialgroupid | int8 | 64 |  | √ | 0 |  |
| 36 | fbizstatus | 业务状态 | varchar | 50 |  | √ | 'ADD' | 业务状态,枚举: ADD :新增 READY :就绪 CHG_ORIGINALVAL :原值变更 CHG_USEDEPT :变更使用部门 DEPRE :折旧 CLEAR_ALL :完全清理 CLEAR_PART :部分清理 DISPATCH :调拨 SPLIT :拆分 COMBIN :组合 DELETE :作废 CHG_PERIOD :变更使用期间 CHG_ASSETCAT :变更资产类别 TRANSFERING :移交中 DRAWBACKING :退库中 SIGNED :已签收 |
| 37 | foriginaldata | foriginaldata | bpchar | 1 |  | √ | '0' |  |
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
| 49 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 50 | fisfacility | 附属设备 | bpchar | 1 |  | √ | '0' | 附属设备 |
| 51 | fsourcebillnumber | 源单据编码 | varchar | 30 |  | √ | ' ' | 源单据编码 |
| 52 | fisbak | 备份卡片 | bpchar | 1 |  | √ | '0' | 备份卡片 |
| 53 | fmergedcard | fmergedcard | bpchar | 1 |  | √ | '0' |  |

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
