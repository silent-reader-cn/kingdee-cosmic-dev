# 累计促销执行情况-ocdpm_cumulativeprom

## 累计促销执行情况-多语言表 t_ocdpm_cumulprom_l

- **表名称：** 累计促销执行情况-多语言表
- **表名：** t_ocdpm_cumulprom_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | 'zh_CN' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_cumulate_l |  | fid |
| 2 | pk_ocdpm_cumulprom_l |  | fpkid |

---

## 单据体-子表 t_ocdpm_cumulpromentry

- **表名称：** 单据体-子表
- **表名：** t_ocdpm_cumulpromentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fauxpropid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 3 | fenbuyqty | 购买条件数量 | numeric | 23 | 10 | √ | 0 | 购买条件数量 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fenbuyamount | 购买条件金额（含税） | numeric | 23 | 10 | √ | 0 | 购买条件金额（含税） |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | ftotalensaleamt | 累计销售金额 | numeric | 23 | 10 | √ | 0 | 累计销售金额 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | ftotalensaleqty | 累计销售数量 | numeric | 23 | 10 | √ | 0 | 累计销售数量 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fitemid | 商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_cumulate_en |  | fid |
| 2 | pk_ocdpm_cumulpromentry |  | fentryid |

---

## 累计促销执行情况-主表 t_ocdpm_cumulprom

- **表名称：** 累计促销执行情况-主表
- **表名：** t_ocdpm_cumulprom

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsettlementtime | 结算时间 | timestamp | 0 |  |  | null | 结算时间 |
| 3 | fpromobjectid | 促销类别 | int8 | 64 |  | √ | 0 | [渠道促销类别 ocdpm_promotionobject](../ocdpm_files/ocdpm_promotionobject.md) |
| 4 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | ftotalsaleqty | 累计销售数量/份数 | numeric | 23 | 10 | √ | 0 | 累计销售数量/份数 |
| 10 | forderchannelid | 订货渠道编码 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 11 | funpromamt | 未促销金额 | numeric | 23 | 10 | √ | 0 | 未促销金额 |
| 12 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbuyconditionqty | 购买条件数量/份数 | numeric | 23 | 10 | √ | 0 | 购买条件数量/份数 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fpromotionpolicyid | 促销编码 | int8 | 64 |  | √ | 0 | [促销政策 ocdpm_promotepolicyf7](../ocdpm_files/ocdpm_promotepolicyf7.md) |
| 17 | ftotalsaleamt | 累计销售金额 | numeric | 23 | 10 | √ | 0 | 累计销售金额 |
| 18 | fconditionqty | 最小起买数量/份数 | numeric | 23 | 10 | √ | 0 | 最小起买数量/份数 |
| 19 | funpromqty | 未促销数量/份数 | numeric | 23 | 10 | √ | 0 | 未促销数量/份数 |
| 20 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fhaspromamt | 已促销金额 | numeric | 23 | 10 | √ | 0 | 已促销金额 |
| 22 | fconditionamt | 最小起买金额 | numeric | 23 | 10 | √ | 0 | 最小起买金额 |
| 23 | fprogroupnoid | 促销组号 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fheadunitid | 计量单位（分录冗余） | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fpromrequire | 促销条件 | bpchar | 1 |  | √ | 'A' | 促销条件,枚举: A :按数量 B :按金额 C :按累计数量 D :按累计金额 |
| 27 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 28 | fhaspromqty | 已促销数量/份数 | numeric | 23 | 10 | √ | 0 | 已促销数量/份数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_cumulate_prom |  | fpromotionpolicyid |
| 2 | pk_ocdpm_cumulprom |  | fid |
