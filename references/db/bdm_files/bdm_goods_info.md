# 开票项管理-bdm_goods_info

## 开票项管理-使用范围位图表 t_bdm_goods_info_m

- **表名称：** 开票项管理-使用范围位图表
- **表名：** t_bdm_goods_info_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 2 | fidx | fidx | int8 | 64 |  | √ | 0 |  |
| 3 | fdata | fdata | bytea | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bdm_goods_info_m |  | forgid |

---

## 开票项管理-多语言表 t_bdm_goods_info_l

- **表名称：** 开票项管理-多语言表
- **表名：** t_bdm_goods_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgoodsname | 商品名称 | varchar | 200 |  | √ | ' ' | 商品名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_goods_info |  | fid,flocaleid |
| 2 | pk_t_bdm_goods_info_l |  | fpkid |

---

## 开票项管理-使用范围表 t_bdm_goods_info_u

- **表名称：** 开票项管理-使用范围表
- **表名：** t_bdm_goods_info_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | 0 |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bdm_goods_info_u |  | fdataid,fuseorgid |
| 2 | idx_bdm_goods_info_u |  | fcreateorgid |

---

## 单据体-子表 t_bdm_goods_info_item

- **表名称：** 单据体-子表
- **表名：** t_bdm_goods_info_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialno | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fbaseunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fmaterialtype | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 7 | fsourcetype | 来源类型 | varchar | 10 |  | √ | '0' | 来源类型,枚举: 0 :物料 1 :物料分类 2 :商品 5 :费用项目 |
| 8 | fmodelnumrate | 单位换算率 | varchar | 50 |  | √ | ' ' | 单位换算率 |
| 9 | fmodelnumunit | 商品单位 | varchar | 50 |  | √ | ' ' | 商品单位 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fmaterialname | 物料/商品名称 | varchar | 255 |  | √ | ' ' | 物料/商品名称 |
| 12 | fmaterialmodelnum | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 13 | fbasisuint | fbasisuint | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_goods_info_item |  | fentryid |
| 2 | idx_bdm_goods_info_item |  | fid |

---

## 开票项管理-主表 t_bdm_goods_info

- **表名称：** 开票项管理-主表
- **表名：** t_bdm_goods_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxrate | 税率 | varchar | 30 |  | √ | ' ' | 税率,枚举: 0 :0% 0.01 :1% 0.015 :1.5% 0.03 :3% 0.04 :4% 0.05 :5% 0.06 :6% 0.09 :9% 0.10 :10% 0.11 :11% 0.13 :13% 0.16 :16% 0.17 :17% |
| 3 | fcreated | fcreated | int8 | 64 |  | √ | 0 |  |
| 4 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 6 | fshareorgs | 指定共享数据 | varchar | 2000 |  | √ | ' ' | 指定共享数据 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 9 | fsource | 来源 | int8 | 64 |  | √ | 0 | [企业管理 bdm_org](../bdm_files/bdm_org.md) |
| 10 | fshareorgstext | 指定共享数据 | varchar | 255 |  | √ | ' ' | 指定共享数据 |
| 11 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fdisen | fdisen | varchar | 1 |  | √ | ' ' |  |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fgoodsinfogroupid | 开票项分类 | int8 | 64 |  | √ | 0 | [开票项分类 bdm_goods_info_group](../bdm_files/bdm_goods_info_group.md) |
| 18 | fgoodsname | 商品名称 | varchar | 100 |  | √ | ' ' | 商品名称 |
| 19 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 21 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 22 | ffilter | 匹配规则 | varchar | 255 |  | √ | ' ' | 匹配规则 |
| 23 | fmaterial | fmaterial | int8 | 64 |  | √ | 0 |  |
| 24 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fname | 商品名称(弃用) | varchar | 100 |  | √ | ' ' | 商品名称(弃用) |
| 26 | fprices | 对应单价 | numeric | 23 | 10 | √ | 0.0000000000 | 对应单价 |
| 27 | fprivilegetype | 优惠政策内容 | varchar | 30 |  | √ | ' ' | 优惠政策内容,枚举: 免税 :免税 不征税 :不征税 |
| 28 | ftaxcode | 税收分类名称 | int8 | 64 |  | √ | 0 | [税收分类编码 er_taxclasscode](../basedata_files/er_taxclasscode.md) |
| 29 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fshare | 共享 | bpchar | 1 |  | √ | ' ' | 共享,枚举: 1 :是 0 :否 2 :已更新新版本 |
| 31 | fprivilegeflag | 优惠政策标识 | varchar | 30 |  | √ | ' ' | 优惠政策标识,枚举: 0 :不享受 1 :享受 |
| 32 | ffilter_tag | 匹配规则_详情 | text | 0 |  |  | null | 匹配规则_详情 |
| 33 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 34 | fgoodscode | 商品编码 | varchar | 32 |  | √ | ' ' | 商品编码 |
| 35 | fshareorgstext_tag | 指定共享数据_详情 | text | 0 |  |  | null | 指定共享数据_详情 |
| 36 | fenable | 有效状态 | varchar | 30 |  | √ | '1' | 有效状态,枚举: 0 :禁用 1 :启用 |
| 37 | fnumber | 商品编码(弃用) | varchar | 50 |  | √ | ' ' | 商品编码(弃用) |
| 38 | fspecifications | 规格型号 | varchar | 40 |  | √ | ' ' | 规格型号 |
| 39 | fisinclusive | 单价是否含税 | varchar | 1 |  | √ | ' ' | 单价是否含税,枚举: 1 :含税 0 :不含税 |
| 40 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 41 | funit | 计量单位 | varchar | 32 |  | √ | ' ' | 计量单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_goods_info_masterid |  | fmasterid |
| 2 | idx_bdm_goods_info_createorg1 |  | fcreateorgid |
| 3 | idx_bdm_goods_info_org |  | forg |
| 4 | idx_t_bdm_goods_info_master |  | fmasterid |
| 5 | idx_bdm_goods_info_goodscode |  | fgoodscode |
| 6 | idx_t_bdm_goods_info_createorg |  | fcreateorgid |
| 7 | idx_bdm_goods_info_group_id |  | fgoodsinfogroupid |
| 8 | pk_bdm_goods_info |  | fid |
| 9 | idx_bdm_goods_info_taxcode |  | ftaxcode |
