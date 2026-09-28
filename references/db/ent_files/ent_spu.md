# 商品SPU-ent_spu

## 基本属性单据体-子表 t_mal_spubaseatrentry

- **表名称：** 基本属性单据体-子表
- **表名：** t_mal_spubaseatrentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprodattributeid | 属性名称 | int8 | 64 |  | √ | 0 | [属性映射商品分类 ent_prodattribute](../ent_files/ent_prodattribute.md) |
| 3 | fprodattributevalueid | 属性内容 | int8 | 64 |  | √ | 0 | [属性内容设置 ent_prodattributevalue](../ent_files/ent_prodattributevalue.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_spubaseatrentry_fid_fseq |  | fid,fseq |
| 2 | pk_mal_spubaseatrentry |  | fentryid |

---

## 关联sku单据体-子表 t_mal_spuskumapentry

- **表名称：** 关联sku单据体-子表
- **表名：** t_mal_spuskumapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgoodsid | SKU编码 | int8 | 64 |  | √ | 0 | [商品管理 ent_prodmanage](../ent_files/ent_prodmanage.md) |
| 3 | fatrvaluenumber | 属性内容组合编码 | varchar | 35 |  | √ | ' ' | 属性内容组合编码 |
| 4 | fguarantee_tag | fguarantee_tag | text | 0 |  |  | null |  |
| 5 | fconfirmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :待提交 D :已驳回 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnote | 审批意见 | varchar | 512 |  | √ | ' ' | 审批意见 |
| 8 | ftaxprice | ftaxprice | numeric | 23 | 10 | √ | 0 |  |
| 9 | fpackinglist_tag | fpackinglist_tag | text | 0 |  |  | null |  |
| 10 | fprice | fprice | numeric | 23 | 10 | √ | 0 |  |
| 11 | fentryresult | 审批结果 | bpchar | 1 |  | √ | ' ' | 审批结果,枚举: 1 :同意 0 :不同意 |
| 12 | fspecification | fspecification | text | 0 |  |  | null |  |
| 13 | fthumbnail | fthumbnail | varchar | 255 |  | √ | ' ' |  |
| 14 | ftaxrateid | ftaxrateid | int8 | 64 |  | √ | 0 |  |
| 15 | fspumainprod | SPU主商品 | bpchar | 1 |  | √ | '0' | SPU主商品 |
| 16 | fskuname | fskuname | varchar | 255 |  | √ | ' ' |  |
| 17 | fgoodsdetail | fgoodsdetail | text | 0 |  |  | null |  |
| 18 | fgoodsdetail_tag | fgoodsdetail_tag | text | 0 |  |  | null |  |
| 19 | ftaxtype | ftaxtype | bpchar | 1 |  | √ | ' ' |  |
| 20 | fspecification_tag | fspecification_tag | text | 0 |  |  | null |  |
| 21 | fpackinglist | fpackinglist | text | 0 |  |  | null |  |
| 22 | fatrvaluename | 属性内容组合 | varchar | 512 |  | √ | ' ' | 属性内容组合 |
| 23 | fcurrid | fcurrid | int8 | 64 |  | √ | 0 |  |
| 24 | fpicture4 | fpicture4 | varchar | 255 |  | √ | ' ' |  |
| 25 | fpicture3 | fpicture3 | varchar | 255 |  | √ | ' ' |  |
| 26 | fpicture2 | fpicture2 | varchar | 255 |  | √ | ' ' |  |
| 27 | fpicture1 | fpicture1 | varchar | 255 |  | √ | ' ' |  |
| 28 | fguarantee | fguarantee | text | 0 |  |  | null |  |
| 29 | fspumapids | 属性组合值映射 | varchar | 1000 |  | √ | ' ' | 属性组合值映射 |
| 30 | fskunumber | fskunumber | varchar | 80 |  | √ | ' ' |  |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fdisplaymainprod | 搜索仅显示主商品 | bpchar | 1 |  | √ | '0' | 搜索仅显示主商品 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_skumapentry_fid_fseq |  | fid,fseq |
| 2 | pk_mal_spuskumapentry |  | fentryid |

---

## 商品SPU-主表 t_mal_spu

- **表名称：** 商品SPU-主表
- **表名：** t_mal_spu

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | SPU名称 | varchar | 100 |  | √ | ' ' | SPU名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 审批单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fsupplierid | 所属商家 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 E :已作废 |
| 10 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_goodsclass](../gmc_files/mdr_goodsclass.md) |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | SPU编码 | varchar | 30 |  | √ | ' ' | SPU编码 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mal_spu |  | fid |
| 2 | idx_spu_fnumber |  | fnumber |

---

## 销售属性组合值子单据体-子表 t_mal_spuatrdetailentry

- **表名称：** 销售属性组合值子单据体-子表
- **表名：** t_mal_spuatrdetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprodattributeid | 属性名称 | int8 | 64 |  | √ | 0 | [属性映射商品分类 ent_prodattribute](../ent_files/ent_prodattribute.md) |
| 2 | fprodattributevalueid | 属性内容 | int8 | 64 |  | √ | 0 | [属性内容设置 ent_prodattributevalue](../ent_files/ent_prodattributevalue.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_atdlet_fentryid_fseq |  | fentryid,fseq |
| 2 | pk_mal_spuatrdetailentry |  | fdetailid |

---

## sku销售属性单据体-子表 t_mal_spusaleatrentry

- **表名称：** sku销售属性单据体-子表
- **表名：** t_mal_spusaleatrentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprodattributeid | 属性名称 | int8 | 64 |  | √ | 0 | [属性映射商品分类 ent_prodattribute](../ent_files/ent_prodattribute.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mal_spusaleatrentry |  | fentryid |
| 2 | idx_spusaleatrentry_fid_fseq |  | fid,fseq |

---

## sku属性内容单据体-子表 t_mal_spuatrvalentry

- **表名称：** sku属性内容单据体-子表
- **表名：** t_mal_spuatrvalentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprodattributevalueid | 属性内容 | int8 | 64 |  | √ | 0 | [属性内容设置 ent_prodattributevalue](../ent_files/ent_prodattributevalue.md) |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_atvlet_fentryid_fseq |  | fentryid,fseq |
| 2 | pk__mal_spuatrvalentry |  | fdetailid |

---

## 商品SPU-多语言表 t_mal_spu_l

- **表名称：** 商品SPU-多语言表
- **表名：** t_mal_spu_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | SPU名称 | varchar | 100 |  | √ | ' ' | SPU名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mal_spu_l |  | fpkid |
| 2 | idx_mal_spu_l_fid_flocaleid |  | fid,flocaleid |
