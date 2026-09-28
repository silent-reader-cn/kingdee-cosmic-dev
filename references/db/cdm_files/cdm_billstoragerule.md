# 票据入库规则-cdm_billstoragerule

## 资金组织-子表 t_cdm_billstoragerule_org

- **表名称：** 资金组织-子表
- **表名：** t_cdm_billstoragerule_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | forg | 组织名称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_billstoragerule_org |  | fid |
| 2 | pk_t_cdm_billstoragerule_org |  | fentryid |

---

## 票据入库规则-多语言表 t_cdm_billstoragerule_l

- **表名称：** 票据入库规则-多语言表
- **表名：** t_cdm_billstoragerule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 255 |  | √ | ' ' | 规则名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_billstoragerule_l |  | fpkid |
| 2 | idx_cdm_billstoragerule_l |  | fid |

---

## 商票规则-子表 t_cdm_businessstoragerule

- **表名称：** 商票规则-子表
- **表名：** t_cdm_businessstoragerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbusinesswarehousingtype | 入库票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |
| 3 | fbusinessautoautite | 匹配入库后自动完成审批 | bpchar | 1 |  | √ | '0' | 匹配入库后自动完成审批 |
| 4 | fbusinesscondition | 适用条件 | varchar | 600 |  | √ | ' ' | 适用条件 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbusinessrulename | 规则项名称 | varchar | 50 |  | √ | ' ' | 规则项名称 |
| 7 | fbusinessdatafilter_tag | 数据过滤条件_详情 | text | 0 |  |  | null | 数据过滤条件_详情 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fbusinessdatafilter | 数据过滤条件 | text | 0 |  |  | null | 数据过滤条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cdm_businessstoragerule |  | fid |
| 2 | pk_t_cdm_businessstoragerule |  | fentryid |

---

## 票据入库规则-主表 t_cdm_billstoragerule

- **表名称：** 票据入库规则-主表
- **表名：** t_cdm_billstoragerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 4 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 7 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fbusinessbilltype | 默认入库票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |
| 10 | fautoautite | 匹配入库后自动完成审批 | bpchar | 1 |  | √ | '0' | 匹配入库后自动完成审批 |
| 11 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fbankbilltype | 默认入库票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |
| 16 | fautoapprove | 匹配入库后自动完成审批 | bpchar | 1 |  | √ | '0' | 匹配入库后自动完成审批 |
| 17 | fenable | 可用状态 | varchar | 30 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fnumber | 规则编码 | varchar | 80 |  | √ | ' ' | 规则编码 |
| 20 | fstorageac | 财票按照银票入库规则入库 | bpchar | 1 |  | √ | '0' | 财票按照银票入库规则入库 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_billstoragerule |  | fid |
| 2 | idx_cdm_billstoragerule |  | fnumber |

---

## 银票规则-子表 t_cdm_bankrule

- **表名称：** 银票规则-子表
- **表名：** t_cdm_bankrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbankdatafilter_tag | 数据过滤条件_详情 | text | 0 |  |  | null | 数据过滤条件_详情 |
| 3 | fbankwarehousingtype | 入库票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |
| 4 | fbankdatafilter | 数据过滤条件 | text | 0 |  |  | null | 数据过滤条件 |
| 5 | fbankautoapprove | 匹配入库后自动完成审批 | bpchar | 1 |  | √ | '0' | 匹配入库后自动完成审批 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbankrulename | 规则项名称 | varchar | 50 |  | √ | ' ' | 规则项名称 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fbankcondition | 适用条件 | varchar | 600 |  | √ | ' ' | 适用条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_bankrule |  | fid |
| 2 | pk_t_cdm_bankrule |  | fentryid |
