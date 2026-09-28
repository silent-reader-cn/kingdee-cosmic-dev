# 项目数据类型-xkbd_rptitemdatatype

## 项目数据类型-主表 t_xkbd_rptitemdatatype

- **表名称：** 项目数据类型-主表
- **表名：** t_xkbd_rptitemdatatype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproportionbase | 占比基数 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |
| 3 | fcustomformula | 计算公式 | varchar | 2000 |  | √ | ' ' | 计算公式 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fviewcount | fviewcount | bpchar | 1 |  | √ | '0' |  |
| 9 | fdatakind | 数据类型 | bpchar | 1 |  | √ | ' ' | 数据类型,枚举: 0 :期末数 1 :年初数 2 :本期发生数 3 :本年累计数 4 :期初数 |
| 10 | fassociateditemdatatype | 来源项目数据类型 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbd_rptitemdatatype |
| 11 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 12 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fcategory | 数据来源 | bpchar | 1 |  | √ | ' ' | 数据来源,枚举: 1 :默认 2 :外部数据 3 :自动计算 |
| 16 | fproportiontype | 占比取数方式 | bpchar | 1 |  | √ | ' ' | 占比取数方式,枚举: 1 :父级 2 :占比基数 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fautocalctype | 计算方式 | bpchar | 1 |  | √ | ' ' | 计算方式,枚举: 1 :占比 2 :同比 3 :环比 4 :上期数 5 :上年同期数 |
| 19 | fdatadigits | fdatadigits | int4 | 32 |  | √ | 4 |  |
| 20 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 24 | fforbiddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fdatatype | 数据属性 | bpchar | 1 |  | √ | ' ' | 数据属性,枚举: 0 :金额 1 :数量 2 :单价 3 :比率 4 :日期 5 :文本 6 :计数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbd_rit_fnumber |  | fnumber |
| 2 | pk_xkbd_rptitemdatatype |  | fid |

---

## 结转项目-多选基础资料表 t_xkbd_carryforwarditem

- **表名称：** 结转项目-多选基础资料表
- **表名：** t_xkbd_carryforwarditem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 项目数据类型 xkbd_rptitemdatatype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbd_carryforwarditem |  | fid |
| 2 | pk_t_xkbd_carryforwarditem |  | fpkid |

---

## 项目数据类型-多语言表 t_xkbd_rptitemdatatype_l

- **表名称：** 项目数据类型-多语言表
- **表名：** t_xkbd_rptitemdatatype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbd_rptitemdatatype_l |  | fpkid |
| 2 | idx_xkbd_rptitemdatatype_l_fid |  | fid |
