# 限量促销执行情况-ocdpm_limitedquantity

## 限量促销执行情况-多语言表 t_ocdpm_limitedquantity_l

- **表名称：** 限量促销执行情况-多语言表
- **表名：** t_ocdpm_limitedquantity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fcontent | 限量内容 | varchar | 2000 |  | √ | ' ' | 限量内容 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_limitedq_lid |  | fid |
| 2 | pk_ocdpm_limitedquantity_l |  | fpkid |

---

## 限量促销执行情况-主表 t_ocdpm_limitedquantity

- **表名称：** 限量促销执行情况-主表
- **表名：** t_ocdpm_limitedquantity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | frowtype | 行类型 | bpchar | 1 |  | √ | 'A' | 行类型,枚举: A :主产品行 B :赠品行 |
| 6 | flimittype | 限量方式 | int8 | 64 |  | √ | 0 | [限量方式 ocdpm_limittype](../ocdpm_files/ocdpm_limittype.md) |
| 7 | fpromotionpolicyid | 促销编码 | int8 | 64 |  | √ | 0 | [促销政策 ocdpm_promotepolicyf7](../ocdpm_files/ocdpm_promotepolicyf7.md) |
| 8 | fremainderqty | 剩余数量/份数 | numeric | 23 | 10 | √ | 0 | 剩余数量/份数 |
| 9 | flimitqty | 限量数量/份数 | numeric | 23 | 10 | √ | 0 | 限量数量/份数 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fprogroupnoid | 促销组号 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 15 | fpggroupnoid | 主产品组/赠品组号 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 18 | fcontent | 限量内容 | varchar | 2000 |  | √ | ' ' | 限量内容 |
| 19 | fusedqty | 已使用数量/份数 | numeric | 23 | 10 | √ | 0 | 已使用数量/份数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_limitedquantity |  | fid |
| 2 | idx_ocdpm_limitedppid |  | fpromotionpolicyid |

---

## 单据体-子表 t_ocdpm_limiteden

- **表名称：** 单据体-子表
- **表名：** t_ocdpm_limiteden

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fppruleentryid | 关联促销规则分录ID | int8 | 64 |  | √ | 0 | 关联促销规则分录ID |
| 3 | fauxpropid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fentryusedmqty | 已使用份数 | numeric | 23 | 10 | √ | 0 | 已使用份数 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fitemid | 商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 10 | fentryusedqty | 已使用数量 | numeric | 23 | 10 | √ | 0 | 已使用数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_limitenppeid |  | fppruleentryid |
| 2 | pk_ocdpm_limiteden |  | fentryid |
| 3 | idx_ocdpm_limitenfpk |  | fid |
