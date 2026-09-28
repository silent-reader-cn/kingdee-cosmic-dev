# 应答规则设置-cdm_responserule

## 应答规则设置-多语言表 t_cdm_responserule_l

- **表名称：** 应答规则设置-多语言表
- **表名：** t_cdm_responserule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 100 |  | √ | ' ' | 规则名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_responseruleset_l |  | fid |
| 2 | pk_t_cdm_responserule_l |  | fpkid |

---

## 应答规则设置-主表 t_cdm_responserule

- **表名称：** 应答规则设置-主表
- **表名：** t_cdm_responserule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatafilter | 数据过滤条件 | varchar | 255 |  | √ | ' ' | 数据过滤条件 |
| 3 | freleaseofpledge | 质押解除待签收 | bpchar | 1 |  | √ | '0' | 质押解除待签收 |
| 4 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 5 | finvoice | 提示收票待签收 | bpchar | 1 |  | √ | '0' | 提示收票待签收 |
| 6 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 13 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 14 | fpledge | 质押待签收 | bpchar | 1 |  | √ | '0' | 质押待签收 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 17 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fdatafilter_tag | 数据过滤条件_详情 | text | 0 |  |  | null | 数据过滤条件_详情 |
| 19 | fconsentpayoff | 同意清偿待签收 | bpchar | 1 |  | √ | '0' | 同意清偿待签收 |
| 20 | frecite | 背书待签收 | bpchar | 1 |  | √ | '0' | 背书待签收 |
| 21 | fconditiondesc | 适用条件 | varchar | 1000 |  | √ | ' ' | 适用条件 |
| 22 | fpayment | 提示付款待签收 | bpchar | 1 |  | √ | '0' | 提示付款待签收 |
| 23 | fenable | 可用状态 | bpchar | 1 |  | √ | '0' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 规则编码 | varchar | 50 |  | √ | ' ' | 规则编码 |
| 25 | fensure | 保证待签收 | bpchar | 1 |  | √ | '0' | 保证待签收 |
| 26 | facceptance | 提示承兑待签收 | bpchar | 1 |  | √ | '0' | 提示承兑待签收 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_responseruleset |  | fnumber |
| 2 | pk_t_cdm_responserule |  | fid |

---

## 单据体-子表 t_cdm_resprulesetentry

- **表名称：** 单据体-子表
- **表名：** t_cdm_resprulesetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_resprulesetentry |  | fid |
| 2 | pk_t_cdm_resprulesetentry |  | fentryid |
