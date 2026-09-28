# 支付用途银企传值映射-bei_bank_purpose

## 用途设置-子表 t_bei_bank_purpose_e

- **表名称：** 用途设置-子表
- **表名：** t_bei_bank_purpose_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshowname | 显示名称 | varchar | 256 |  | √ | ' ' | 显示名称 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fmapkey | 映射值 | varchar | 256 |  | √ | ' ' | 映射值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_bank_purpose_e |  | fentryid |
| 2 | idx_t_bei_bank_pure |  | fid |

---

## 支付用途银企传值映射-多语言表 t_bei_bank_purpose_l

- **表名称：** 支付用途银企传值映射-多语言表
- **表名：** t_bei_bank_purpose_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 256 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 256 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 256 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_bank_purpose_l |  | fpkid |
| 2 | idx_t_bei_bankpurl_fid |  | fid |

---

## 支付用途银企传值映射-主表 t_bei_bank_purpose

- **表名称：** 支付用途银企传值映射-主表
- **表名：** t_bei_bank_purpose

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 256 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fenabletype | 对私支付用途启用枚举 | varchar | 64 |  | √ | ' ' | 对私支付用途启用枚举,枚举: commonpay :普通支付 agentpay :代发 |
| 6 | fbeitype | 银企对接平台 | varchar | 64 |  | √ | ' ' | 银企对接平台,枚举: 2 :招行CBS 3 :宁波银行财资大管家 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 256 |  | √ | ' ' | 编码 |
| 13 | fbanktype | 付款账户银行类别 | int8 | 64 |  | √ | 0 | [银行类别 bd_bankcgsetting](../basedata_files/bd_bankcgsetting.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_bank_purpose |  | fid |
| 2 | idx_t_bei_bankpurtype |  | fbanktype |
