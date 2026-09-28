# 产品族定义-mds_productfamily

## 产品族定义-多语言表 t_mds_productfamily_l

- **表名称：** 产品族定义-多语言表
- **表名：** t_mds_productfamily_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_productfamily_l |  | fid,flocaleid |
| 2 | pk_t_mds_productfamily_l |  | fpkid |

---

## 产品族定义-主表 t_mds_productfamily

- **表名称：** 产品族定义-主表
- **表名：** t_mds_productfamily

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproductfamily | 产品族 | varchar | 50 |  | √ | ' ' | 产品族 |
| 3 | fofferingshow | 产品型号 | varchar | 255 |  | √ | ' ' | 产品型号 |
| 4 | fpbomname | fpbomname | varchar | 50 |  | √ | ' ' |  |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | fitemstatus | 物料编码状态 | varchar | 50 |  | √ | ' ' | 物料编码状态 |
| 7 | fpbomnameshow | 计划BOM描述 | varchar | 255 |  | √ | ' ' | 计划BOM描述 |
| 8 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 9 | fgeneraltag | 通用标识 | varchar | 50 |  | √ | ' ' | 通用标识 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fplanusercode | 计划员代码 | varchar | 50 |  | √ | ' ' | 计划员代码 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fmaterialplan | 物料计划信息 | int8 | 64 |  | √ | 0 | [物料计划信息 mpdm_materialplan](../sbd_files/mpdm_materialplan.md) |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fitemnameshow | 物料编码名称 | varchar | 255 |  | √ | ' ' | 物料编码名称 |
| 17 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 18 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 19 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 20 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fmaterielpbom | 产品族 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fplanuser | 计划员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fmaterielitem | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 26 | fbomtype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: PBOM :产品族 MBOM :关联关系 |
| 27 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 28 | fsupmodel | 供应模式 | varchar | 50 |  | √ | ' ' | 供应模式 |
| 29 | fapprovedateshow | 物料编码生效日期 | timestamp | 0 |  |  | null | 物料编码生效日期 |
| 30 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fpbomnameedit | 产品族名称 | varchar | 255 |  | √ | ' ' | 产品族名称 |
| 32 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 33 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_productfamily |  | fid |
| 2 | idx_mds_productfamily_pbom |  | fmaterielpbom |
| 3 | idx_mds_productfamily |  | fmaterielitem |
| 4 | idx_t_mds_productfamily_createorg |  | fcreateorgid |
| 5 | idx_t_mds_productfamily_master |  | fmasterid |
