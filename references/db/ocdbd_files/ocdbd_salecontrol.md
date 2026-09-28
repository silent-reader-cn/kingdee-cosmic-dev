# 可销控制-ocdbd_salecontrol

## 可销控制-主表 t_ocdbd_item_salectrl

- **表名称：** 可销控制-主表
- **表名：** t_ocdbd_item_salectrl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 6 | fregionid | fregionid | int8 | 64 |  | √ | 0 |  |
| 7 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fitembrandsid | 商品品牌 | int8 | 64 |  | √ | 0 | 商品品牌 mdr_item_brand |
| 9 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 10 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fsupplyrelation | 供货关系 | bpchar | 1 |  | √ | 'A' | 供货关系,枚举: A :组织直供 B :渠道供货 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | forderchannelid | 订货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 17 | fchannelclassid | 订货渠道分类 | int8 | 64 |  | √ | 0 | 渠道分类 ocdbd_channel_class |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fcansale | 可销控制 | bpchar | 1 |  | √ | 'A' | 可销控制,枚举: A :可销可用 C :不可销可用 B :禁用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_item_salectrl |  | fid |
| 2 | idx_ocdbd_isc_schannel |  | fsalechannelid |
| 3 | idx_ocdbd_isc_fregionid |  | fregionid |
| 4 | idx_ocdbd_isc_ochannel |  | forderchannelid |
| 5 | idx_ocdbd_isc_salorg |  | fsaleorgid |
| 6 | idx_ocdbd_isc_cgroup |  | fchannelclassid |

---

## 可销控制-多语言表 t_ocdbd_item_salectrl_l

- **表名称：** 可销控制-多语言表
- **表名：** t_ocdbd_item_salectrl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_itemsalectrll_flid |  | fid,flocaleid |
| 2 | pk_ocdbd_item_salectrl_l |  | fpkid |
