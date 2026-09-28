# 认筹邀约活动-ocdbd_olinvitate

## 渠道分类-多选基础资料表 t_ocdbd_olinvitatechan

- **表名称：** 渠道分类-多选基础资料表
- **表名：** t_ocdbd_olinvitatechan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_olinvitatechan |  | fpkid |
| 2 | idx_ocdbd_olinvitatechan_id |  | fid |

---

## 券类型选择-子表 t_ocdbd_olinvitateticket

- **表名称：** 券类型选择-子表
- **表名：** t_ocdbd_olinvitateticket

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | ftickettypeid | 券类型 | int8 | 64 |  | √ | 0 | 优惠券类型 rtvip_ticketstype |
| 4 | fsaleamount | 售券金额 | numeric | 23 | 10 | √ | 0 | 售券金额 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_olinvitateticket |  | fentryid |
| 2 | idx_ocdbd_olinvitateticket_id |  | fid |

---

## 认筹邀约活动-主表 t_ocdbd_olinvitate

- **表名称：** 认筹邀约活动-主表
- **表名：** t_ocdbd_olinvitate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fgifttotal | 赠送礼品总数 | int4 | 32 |  | √ | 0 | 赠送礼品总数 |
| 4 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 5 | fcontrolmode | 控制方式 | bpchar | 1 |  | √ | '0' | 控制方式,枚举: 0 :适用所有门店 2 :适用指定门店 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fdescription_tag | 认筹邀约海报_详情 | text | 0 |  |  | null | 认筹邀约海报_详情 |
| 11 | fgiftradiogroup | 单选按钮组 | bpchar | 1 |  | √ | '0' | 单选按钮组,枚举: 1 :相同商品送赠品 0 :范围内商品送赠品 |
| 12 | fisagencyinvitate | 是否代认筹 | bpchar | 1 |  | √ | '0' | 是否代认筹 |
| 13 | ftickettotalprice | 券总售价 | numeric | 23 | 10 | √ | 0 | 券总售价 |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fapprovedate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 18 | fisgroupticket | 是否组合券 | bpchar | 1 |  | √ | '0' | 是否组合券 |
| 19 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | factivitystatus | 活动状态 | bpchar | 1 |  | √ | '2' | 活动状态,枚举: 0 :已失效 1 :已生效 2 :未生效 |
| 22 | fsubjectpic | 主题图 | varchar | 255 |  | √ | ' ' | 主题图 |
| 23 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fdescription | 认筹邀约海报 | varchar | 255 |  | √ | ' ' | 认筹邀约海报 |
| 25 | fstarttime | 活动开始日期 | timestamp | 0 |  |  | null | 活动开始日期 |
| 26 | factivitytype | 活动类型 | bpchar | 1 |  | √ | 'A' | 活动类型,枚举: A :现金券 B :礼品券 C :现金券+指定礼品 D :现金券+礼品券 |
| 27 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 29 | fendtime | 活动结束日期 | timestamp | 0 |  |  | null | 活动结束日期 |
| 30 | factivateamount | 激活金额 | numeric | 23 | 10 | √ | 0 | 激活金额 |
| 31 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 32 | fisallgoods | 是否适用所有商品 | bpchar | 1 |  | √ | '0' | 是否适用所有商品 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_olinvitate_num |  | fnumber |
| 2 | pk_ocdbd_olinvitate |  | fid |

---

## 组织范围-多选基础资料表 t_ocdbd_olinvitateorg

- **表名称：** 组织范围-多选基础资料表
- **表名：** t_ocdbd_olinvitateorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_olinvitateorg |  | fpkid |
| 2 | idx_ocdbd_olinvitateorg_fid |  | fid |

---

## 使用条件-子表 t_ocdbd_olinvitateusecod

- **表名称：** 使用条件-子表
- **表名：** t_ocdbd_olinvitateusecod

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fbarcodeid | 商品条形码 | int8 | 64 |  | √ | 0 | [商品条形码 ocdbd_item_barcode](../ocdbd_files/ocdbd_item_barcode.md) |
| 6 | fgoodsprice | fgoodsprice | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_olinvitateusecod |  | fdetailid |
| 2 | idx_ocdbd_olinvitateuscod_eid |  | fentryid |

---

## 礼品选择-子表 t_ocdbd_olinvitategifts

- **表名称：** 礼品选择-子表
- **表名：** t_ocdbd_olinvitategifts

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fgiveqty | 赠送数量 | int4 | 32 |  | √ | 0 | 赠送数量 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fbarcodeid | 商品条形码 | int8 | 64 |  | √ | 0 | [商品条形码 ocdbd_item_barcode](../ocdbd_files/ocdbd_item_barcode.md) |
| 6 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 7 | fgoodsprice | fgoodsprice | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_olinvitategifts_eid |  | fentryid |
| 2 | pk_ocdbd_olinvitategifts |  | fdetailid |

---

## 认筹邀约活动-多语言表 t_ocdbd_olinvitate_l

- **表名称：** 认筹邀约活动-多语言表
- **表名：** t_ocdbd_olinvitate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 标题 | varchar | 100 |  | √ | ' ' | 标题 |
| 3 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_olinvitate_l |  | fpkid |
| 2 | idx_ocdbd_olinvitatel_lid |  | fid,flocaleid |

---

## 适用门店范围-子表 t_ocdbd_olinvitatebranch

- **表名称：** 适用门店范围-子表
- **表名：** t_ocdbd_olinvitatebranch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisapply | 是否适用 | bpchar | 1 |  | √ | '1' | 是否适用 |
| 3 | fbranchid | 门店编码 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 4 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
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
| 1 | idx_ocdbd_olinvitatebranch_id |  | fid |
| 2 | pk_ocdbd_olinvitatebranch |  | fentryid |

---

## 适用导购员范围-子表 t_ocdbd_olinvitatesaler

- **表名称：** 适用导购员范围-子表
- **表名：** t_ocdbd_olinvitatesaler

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsalesmanid | 导购员编码 | int8 | 64 |  | √ | 0 | [渠道用户(已废弃) ocdbd_channeluser](../ocdbd_files/ocdbd_channeluser.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_olinvitatesaler_id |  | fid |
| 2 | pk_ocdbd_olinvitatesaler |  | fentryid |
