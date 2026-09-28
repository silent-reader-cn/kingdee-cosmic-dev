# 数据资产-fa_data_asset

## 关联子实体-子表 t_fa_data_asset_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fa_data_asset_lk

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
| 1 | pk_fa_data_asset_lk |  | fpkid |
| 2 | idx_fa_data_asset_lk_fk |  | fid |

---

## 单据体-多语言表 t_fa_data_detail_l

- **表名称：** 单据体-多语言表
- **表名：** t_fa_data_detail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fentryremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fentryname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_data_detail_l |  | fpkid |
| 2 | idx_fa_data_detail_l_lid |  | fentryid,flocaleid |

---

## 数据资产-反写记录表 t_fa_data_asset_wb

- **表名称：** 数据资产-反写记录表
- **表名：** t_fa_data_asset_wb

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
| 1 | pk_fa_data_asset_wb |  | fentryid |
| 2 | idx_fa_data_asset_wb_fk |  | fid |

---

## 单据体-子表 t_fa_data_detail

- **表名称：** 单据体-子表
- **表名：** t_fa_data_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvaliddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 3 | feffectuatedate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 4 | fstatus | 状态 | varchar | 10 |  | √ | ' ' | 状态,枚举: 1 :生效 2 :失效 |
| 5 | fentrymodifier | 更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fentryscale | 数据规模 | numeric | 23 | 10 | √ | 0 | 数据规模 |
| 7 | fentrysupplier | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | finvalidtype | 失效类型 | bpchar | 1 |  | √ | '1' | 失效类型,枚举: 1 :手动 2 :完全清理 |
| 11 | fdetailsbillno | 编号 | varchar | 50 |  | √ | ' ' | 编号 |
| 12 | fentryunit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_data_detail |  | fentryid |
| 2 | idx_fa_data_detail_id |  | fid |

---

## 数据资产-关联追踪表 t_fa_data_asset_tc

- **表名称：** 数据资产-关联追踪表
- **表名：** t_fa_data_asset_tc

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
| 1 | idx_fa_data_asset_tc_tbill |  | ftbillid |
| 2 | pk_fa_data_asset_tc |  | fid |
| 3 | idx_fa_data_asset_tc_tid |  | ftid |

---

## 数据资产-主表 t_fa_data_asset

- **表名称：** 数据资产-主表
- **表名：** t_fa_data_asset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fregisterdate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 4 | fmanager | 管理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fregisternumber | 登记编号 | varchar | 50 |  | √ | ' ' | 登记编号 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fsaveformat | 数据存储格式 | varchar | 10 |  | √ | ' ' | 数据存储格式,枚举: 1 :文本 2 :图像 3 :语音 4 :视频 5 :网页 6 :数据库 7 :传感信号 |
| 8 | fassetunitid | 资产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | 存放地点 fa_storeplace |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fheadusedeptid | 管理部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fbusstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: READY :就绪 DELETE :已作废 ADD :新增中 |
| 13 | fupdatefrequency | 更新频率 | varchar | 10 |  | √ | ' ' | 更新频率,枚举: 1 :每天 2 :每周 3 :每月 4 :每季度 5 :每半年 6 :每年 |
| 14 | fbillno | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | foriginmethodid | 数据来源 | int8 | 64 |  | √ | 0 | 增减方式 fa_changemode |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | 资产类别 fa_assetcategory |
| 20 | funitid | 规模单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 23 | ftype | 数据类型 | varchar | 10 |  | √ | ' ' | 数据类型,枚举: 1 :结构化数据 2 :非结构化数据 3 :半结构化数据 |
| 24 | fscale | 数据规模 | numeric | 23 | 10 | √ | 0 | 数据规模 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_data_asset_no |  | fbillno |
| 2 | pk_fa_data_asset |  | fid |

---

## 数据资产-多语言表 t_fa_data_asset_l

- **表名称：** 数据资产-多语言表
- **表名：** t_fa_data_asset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 数据名称 | varchar | 200 |  | √ | ' ' | 数据名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_data_asset_l |  | fpkid |
| 2 | idx_fa_data_asset_l_flid |  | fid,flocaleid |
