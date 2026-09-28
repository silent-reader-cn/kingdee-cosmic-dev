# 促销方案-ocdpm_promote

## 商品除外清单-子表 t_ocdpm_promoteexitem

- **表名称：** 商品除外清单-子表
- **表名：** t_ocdpm_promoteexitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 3 | fexunitid | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 4 | fextype | 类型 | bpchar | 1 |  | √ | '1' | 类型,枚举: 1 :商品 2 :商品分类 3 :商品品牌 4 :商品标签 5 :综合 |
| 5 | fexitemlabelid | 商品标签 | int8 | 64 |  | √ | 0 | 商品标签 ocdbd_item_label |
| 6 | fexbarcodeid | 商品条形码 | int8 | 64 |  | √ | 0 | 商品条形码 ocdbd_item_barcode |
| 7 | fexmaterielid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fexitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 10 | fexbrandid | 商品品牌 | int8 | 64 |  | √ | 0 | 商品品牌 mdr_item_brand |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_promoteexitem_fid |  | fid |
| 2 | pk_ocdpm_promoteexitem |  | fentryid |

---

## 商品清单单据体-子表 t_ocdpm_promoteitem

- **表名称：** 商品清单单据体-子表
- **表名：** t_ocdpm_promoteitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemlabelid | 商品标签 | int8 | 64 |  | √ | 0 | 商品标签 ocdbd_item_label |
| 3 | fpromoteprice | 促销特价 | numeric | 23 | 10 | √ | 0 | 促销特价 |
| 4 | fsaleattrid | 销售属性(废弃) | int8 | 64 |  | √ | 0 | 商品销售属性 ocdbd_item_saleattr |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fassumecostscale | 费用承担比例 | numeric | 23 | 10 | √ | 0 | 费用承担比例 |
| 8 | fbrandid | 商品品牌 | int8 | 64 |  | √ | 0 | 商品品牌 mdr_item_brand |
| 9 | fstocktypeid | 库存类型(废弃) | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 10 | fquotaamount | 优惠额度 | numeric | 23 | 10 | √ | 0 | 优惠额度 |
| 11 | fselectnum | fselectnum | int4 | 32 |  | √ | 0 |  |
| 12 | fcostassumeobject | 费用承担类型类型 | varchar | 30 |  | √ | ' ' | 费用承担类型类型,枚举: bd_supplier :供应商 bos_org :组织 ocdbd_channel :门店 |
| 13 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 14 | fitemprice | 零售价 | numeric | 23 | 10 | √ | 0 | 零售价 |
| 15 | fdiscountprice | 折后价 | numeric | 23 | 10 | √ | 0 | 折后价 |
| 16 | fcostassumeobjid | 费用承担对象 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 17 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 18 | funitid | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fisdropout | 是否除外 | bpchar | 1 |  | √ | '0' | 是否除外 |
| 20 | fdiscount | 折扣 | numeric | 23 | 10 | √ | 0 | 折扣 |
| 21 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 22 | ftype | 类型 | bpchar | 1 |  | √ | '1' | 类型,枚举: 1 :商品 2 :商品分类 3 :商品品牌 4 :商品标签 5 :综合 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fbarcodeid | 商品条形码 | int8 | 64 |  | √ | 0 | 商品条形码 ocdbd_item_barcode |
| 25 | fassistattid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_promoteitem |  | fentryid |
| 2 | idx_ocdpm_promoteitem_fid |  | fid |

---

## 渠道分类-多选基础资料表 t_ocdpm_promotechannel

- **表名称：** 渠道分类-多选基础资料表
- **表名：** t_ocdpm_promotechannel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 渠道分类 ocdbd_channel_class |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_promotechannel |  | fpkid |
| 2 | idx_ocdpm_promotechannel_fid |  | fid |

---

## 库存类型-多选基础资料表 t_ocdpm_promotestypeo

- **表名称：** 库存类型-多选基础资料表
- **表名：** t_ocdpm_promotestypeo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_promotestypeo_eid |  | fentryid |
| 2 | pk_ocdpm_promotestypeo |  | fpkid |

---

## 销售属性-多选基础资料表 t_ocdpm_promoteattro

- **表名称：** 销售属性-多选基础资料表
- **表名：** t_ocdpm_promoteattro

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 商品销售属性 ocdbd_item_saleattr |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_promoteattro_eid |  | fentryid |
| 2 | pk_ocdpm_promoteattro |  | fpkid |

---

## 适用日期单据体-子表 t_ocdpm_promotedate

- **表名称：** 适用日期单据体-子表
- **表名：** t_ocdpm_promotedate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatetype | 日期类型 | bpchar | 1 |  | √ | '3' | 日期类型,枚举: 1 :选择周 2 :选择星期 3 :选择日期 4 :选择每月某天 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdatetext | 日期 | varchar | 100 |  | √ | ' ' | 日期 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_promotedate_fid |  | fid |
| 2 | pk_ocdpm_promotedate |  | fentryid |

---

## 适用门店单据体-子表 t_ocdpm_promotebranch

- **表名称：** 适用门店单据体-子表
- **表名：** t_ocdpm_promotebranch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisexecute | 是否执行 | bpchar | 1 |  | √ | '0' | 是否执行 |
| 3 | fapplyorgid | 组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fbranchid | 门店编码 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_promotebranch |  | fentryid |
| 2 | idx_ocdpm_promotebranch_fid |  | fid |

---

## 促销方案-分表 t_ocdpm_promote_o

- **表名称：** 促销方案-分表
- **表名：** t_ocdpm_promote_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemselected | 商品选择 | bpchar | 1 |  | √ | '1' | 商品选择,枚举: 2 :指定商品 1 :全部商品 |
| 3 | fispointpermit | 允许积分 | bpchar | 1 |  | √ | '0' | 允许积分 |
| 4 | fcostassumeobjid | fcostassumeobjid | int8 | 64 |  | √ | 0 |  |
| 5 | fismanualpromote | 手工改价/打折商品参与促销 | bpchar | 1 |  | √ | '0' | 手工改价/打折商品参与促销 |
| 6 | fcontrolmethod | 控制方式 | bpchar | 1 |  | √ | ' ' | 控制方式,枚举: A :适用所有门店 B :适用指定门店 |
| 7 | fmembergroup | 会员选择组 | bpchar | 1 |  | √ | '1' | 会员选择组,枚举: 1 :全部会员 2 :非会员 3 :指定会员 4 :生日会员 |
| 8 | fpointmutiple | 积分倍数 | int8 | 64 |  | √ | 0 | 积分倍数 |
| 9 | fispossecondscreen | POS副屏播放 | bpchar | 1 |  | √ | '0' | POS副屏播放 |
| 10 | fassumecostscale | fassumecostscale | numeric | 23 | 10 | √ | 0 |  |
| 11 | fisonlinemallprom | 线上商城促销 | bpchar | 1 |  | √ | '0' | 线上商城促销 |
| 12 | fallitemdisco | 全部商品折扣 | numeric | 23 | 10 | √ | 0 | 全部商品折扣 |
| 13 | feffechour | feffechour | int8 | 64 |  | √ | 0 |  |
| 14 | fisonlinestoreprom | 线上门店促销 | bpchar | 1 |  | √ | '0' | 线上门店促销 |
| 15 | finvalidhour | 失效时间 | int8 | 64 |  | √ | 0 | 失效时间 |
| 16 | feffecthour | 生效时间 | int8 | 64 |  | √ | 0 | 生效时间 |
| 17 | fisofflinestoreprom | 线下门店促销 | bpchar | 1 |  | √ | '0' | 线下门店促销 |
| 18 | fisoffstatepromote | 允许门店离线促销 | bpchar | 1 |  | √ | '0' | 允许门店离线促销 |
| 19 | fsuitabledate | 适用日期 | bpchar | 1 |  | √ | ' ' | 适用日期,枚举: 1 :全部日期 2 :指定日期 |
| 20 | fcostassumeobject | fcostassumeobject | varchar | 30 |  | √ | ' ' |  |
| 21 | ftimerange | 时间段 | bpchar | 1 |  | √ | '1' | 时间段,枚举: 1 :24小时 2 :指定时间段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_promote_o |  | fid |
| 2 | idx_ocdpm_promoteo_fobj |  | fcostassumeobjid |

---

## 销售属性-多选基础资料表 t_ocdpm_promoteattr

- **表名称：** 销售属性-多选基础资料表
- **表名：** t_ocdpm_promoteattr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 商品销售属性 ocdbd_item_saleattr |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_promoteattr_eid |  | fentryid |
| 2 | pk_ocdpm_promoteattr |  | fpkid |

---

## 适用会员单据体-子表 t_ocdpm_promotemember

- **表名称：** 适用会员单据体-子表
- **表名：** t_ocdpm_promotemember

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmemberlabelid | 会员标签 | int8 | 64 |  | √ | 0 | 会员档案 ocdbd_user |
| 3 | fdesignation | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fmemberid | 会员 | int8 | 64 |  | √ | 0 | 会员档案 ocdbd_user |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fvipleverid | 会员等级 | int8 | 64 |  | √ | 0 | 会员等级定义 ocdbd_vip_level |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftypetext | 类型 | varchar | 255 |  | √ | ' ' | 业务对象 bos_objecttype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_promotemember |  | fentryid |
| 2 | idx_ocdpm_promotemember_fid |  | fid |

---

## 除外库存类型-多选基础资料表 t_ocdpm_promotestype

- **表名称：** 除外库存类型-多选基础资料表
- **表名：** t_ocdpm_promotestype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_promotestype |  | fpkid |
| 2 | idx_ocdpm_promotestype_eid |  | fentryid |

---

## 组织范围-多选基础资料表 t_ocdpm_promoteorg

- **表名称：** 组织范围-多选基础资料表
- **表名：** t_ocdpm_promoteorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_promoteorg_fid |  | fid |
| 2 | pk_ocdpm_promoteorg |  | fpkid |

---

## 促销方案-主表 t_ocdpm_promote

- **表名称：** 促销方案-主表
- **表名：** t_ocdpm_promote

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpromotionsid | 促销活动 | int8 | 64 |  | √ | 0 | 促销活动 ocdbd_promotion |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fdeptid | 部门 | int8 | 64 |  | √ | 0 | 行政组织（部门） bos_adminorg |
| 5 | fdynamicbill | 促销表单标识 | varchar | 36 |  | √ | ' ' | 促销表单标识 |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fpromoteimageurl | 活动图片 | varchar | 255 |  | √ | ' ' | 活动图片 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fpromotetheme | 促销主题 | varchar | 100 |  | √ | ' ' | 促销主题 |
| 13 | fbillname | 促销方案名称 | varchar | 100 |  | √ | ' ' | 促销方案名称 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 16 | fterminator | 终止人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fterminatortime | 终止时间 | timestamp | 0 |  |  | null | 终止时间 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 20 | fpromotetypeid | 促销类型 | int8 | 64 |  | √ | 0 | 促销类型 ocdbd_promotetype |
| 21 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 22 | fbillno | 促销方案编号 | varchar | 80 |  | √ | ' ' | 促销方案编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fpromotestatus | 促销状态 | bpchar | 1 |  | √ | 'A' | 促销状态,枚举: A :未开始 B :执行中 C :已终止 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_promote_bno |  | fbillno |
| 2 | pk_ocdpm_promote |  | fid |

---

## 费用承担设置-子表 t_ocdpm_promotecost

- **表名称：** 费用承担设置-子表
- **表名：** t_ocdpm_promotecost

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fcostobjecttype | 费用承担类型类型 | varchar | 30 |  | √ | ' ' | 费用承担类型类型,枚举: bd_supplier :供应商 bos_org :组织 ocdbd_channel :门店 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fcostscale | 费用承担比例 | numeric | 23 | 10 | √ | 0 | 费用承担比例 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fcostobject | 费用承担对象 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_promotecost |  | fentryid |
| 2 | idx_ocdpm_promotecost_fid |  | fid |
