# 汇率-bd_exrate_tree

## 汇率-多语言表 t_bd_exrate_l

- **表名称：** 汇率-多语言表
- **表名：** t_bd_exrate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_exrate_l_pkey |  | fpkid |
| 2 | idx_t_bd_exrate_l_fid |  | fid,flocaleid |

---

## 汇率-主表 t_bd_exrate

- **表名称：** 汇率-主表
- **表名：** t_bd_exrate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 3 | forgcurid | 原币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fconvertmode | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 1 :直接汇率 2 :间接汇率 |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fexcprecision | fexcprecision | int8 | 64 |  | √ | 0 |  |
| 7 | fcurid | 目标币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 8 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fexctype | 汇率类型 | varchar | 255 |  | √ | ' ' | 汇率类型,枚举: 1 :固定汇率 2 :浮动汇率 |
| 14 | fexrate | 直接汇率值 | numeric | 23 | 10 |  | null | 直接汇率值 |
| 15 | findirectexrate | 间接汇率值 | numeric | 23 | 10 |  | null | 间接汇率值 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fprecision | 显示精度参数 | int8 | 64 |  | √ | 0 | 显示精度参数 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fforeignexcid | 外币牌价 | varchar | 255 |  | √ | ' ' | 外币牌价,枚举: 1 :买入价 2 :中间价 3 :卖出价 |
| 21 | fcomputationrules | 计算规则 | varchar | 64 |  | √ | ' ' | 计算规则 |
| 22 | fexpirydate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fdatasource | 数据源 | varchar | 50 |  | √ | ' ' | 数据源,枚举: FX_001 :人民币中间价 FX_002 :交叉汇率 FX_003 :即时汇率 FX_004 :即时汇率 |
| 25 | fxkissystem | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 26 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_exrate_fcurid |  | fcurid |
| 2 | t_bd_exrate_pkey |  | fid |
| 3 | idx_t_bd_exrate_forgcurid |  | forgcurid |
