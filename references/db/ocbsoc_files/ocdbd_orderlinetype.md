# 订单行类型-ocdbd_orderlinetype

## 订单行类型-多语言表 t_ocdbd_orderlinetype_l

- **表名称：** 订单行类型-多语言表
- **表名：** t_ocdbd_orderlinetype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_orderlinetype_l |  | fpkid |
| 2 | idx_ocdbd_orderlinetype_flid |  | fid,flocaleid |

---

## 商品控制单据体-子表 t_ocdbd_linetypeitem

- **表名称：** 商品控制单据体-子表
- **表名：** t_ocdbd_linetypeitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 7 | flogicalrealtion | 逻辑关系 | bpchar | 1 |  | √ | ' ' | 逻辑关系,枚举: 0 :包含关系 1 :例外排除 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_linetypeitem_fid |  | fid |
| 2 | pk_ocdbd_linetypeitem |  | fentryid |

---

## 订单行类型-主表 t_ocdbd_orderlinetype

- **表名称：** 订单行类型-主表
- **表名：** t_ocdbd_orderlinetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | foffsettype | 资金池抵扣类型 | bpchar | 1 |  | √ | ' ' | 资金池抵扣类型,枚举: 0 :所有账户均可抵扣 1 :按指定账户抵扣 2 :不允许抵扣 |
| 5 | fisrebate | 计返利 | bpchar | 1 |  | √ | '0' | 计返利 |
| 6 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmoneyaccountid | 抵扣资金账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 8 | fissale | 计销量 | bpchar | 1 |  | √ | '0' | 计销量 |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | faccountclass | 账户类别 | bpchar | 1 |  | √ | 'A' | 账户类别,枚举: A :金额账户 B :数量金额账户 |
| 11 | fismoneyoffset | 计资金池抵扣 | bpchar | 1 |  | √ | '1' | 计资金池抵扣 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fisbudget | 计预算 | bpchar | 1 |  | √ | '0' | 计预算 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fissyspreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 20 | fisdefault | 默认类型 | bpchar | 1 |  | √ | '0' | 默认类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_orderlinetype |  | fid |
| 2 | idx_ocdbd_orderlinetype_num |  | fnumber |
